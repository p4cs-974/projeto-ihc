#!/usr/bin/env python3
"""Gera um HTML com os diffs de uma rodada de feedback.

Arquivos de texto saem em visão dividida pelo @pierre/diffs, com o realçador
Highlights. Imagens e SVGs continuam lado a lado. Cada commit aparece com o
trecho literal do parecer do professor que o motivou.

Uso (na raiz do repositório):
    python3 .agents/skills/aplicar-feedback-professor/scripts/gerar_diffs.py spec.json saida.html

Formato do spec.json: veja references/diff-html.md. Requer `pip install markdown`
para as citações e `npm install` em `.agents/skills/pierre-diff` para o diff.
Se o realçador não puder rodar, o arquivo correspondente vira um diff unificado em texto.
"""
import base64, difflib, html, json, os, re, subprocess, sys, tempfile
from pathlib import Path
import markdown

SPEC_PATH, OUT = sys.argv[1:3]
SPEC = json.load(open(SPEC_PATH, encoding='utf-8'))
REPO = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip() or '.'
BASE = SPEC['base']
TITLE = SPEC.get('titulo', 'Diffs do feedback')


def _gh_base():
    url = subprocess.run(['git', '-C', REPO, 'remote', 'get-url', 'origin'], capture_output=True, text=True).stdout.strip()
    m = re.search(r'github\.com[:/]+([^/]+/[^/]+?)(?:\.git)?$', url)
    if m:
        return f'https://github.com/{m.group(1)}/commit/'
    m = re.search(r'/git/([^/]+/[^/]+?)(?:\.git)?$', url)
    return f'https://github.com/{m.group(1)}/commit/' if m else ''


GH = _gh_base()


def git(*a, binary=False):
    r = subprocess.run(['git', '-C', REPO, *a], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout if binary else r.stdout.decode('utf-8')


def git_text(rev, path):
    data = git('show', f'{rev}:{path}', binary=True)
    if data is None:
        return None
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return None


PIERRE_JOBS = []
PIERRE_HELPER = Path(__file__).resolve().parents[2] / 'pierre-diff' / 'render-diff.mjs'


def queue_pierre(before, after, path):
    jid = f'p{len(PIERRE_JOBS)}'
    PIERRE_JOBS.append({'id': jid, 'name': path, 'before': before, 'after': after, 'header': False})
    return f'<div data-pierre="{jid}"></div>'


def plain_diff_html(job):
    before = job['before'] or ''
    after = job['after'] or ''
    lines = difflib.unified_diff(before.splitlines(), after.splitlines(),
                                 fromfile=job['name'], tofile=job['name'], lineterm='')
    body = html.escape('\n'.join(lines) or '(sem diferença de linhas)')
    return f'<pre class="fallback">{body}</pre>'


def line_changes(before, after):
    sm = difflib.SequenceMatcher(None, (before or '').splitlines(), (after or '').splitlines(), autojunk=False)
    return sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal')


def pierre_html_by_id():
    if not PIERRE_JOBS:
        return {}
    if not PIERRE_HELPER.is_file():
        print(f'Helper ausente: {PIERRE_HELPER}', file=sys.stderr)
        return {}
    fd, spec = tempfile.mkstemp(suffix='.json')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as fh:
            json.dump({'files': PIERRE_JOBS}, fh)
        run = subprocess.run(['node', str(PIERRE_HELPER), '--json', spec], capture_output=True, text=True)
    finally:
        os.remove(spec)
    if run.returncode != 0:
        sys.stderr.write(run.stderr or run.stdout or 'Falha ao renderizar diffs com Pierre.\n')
        return {}
    if run.stderr.strip():
        sys.stderr.write(run.stderr if run.stderr.endswith('\n') else run.stderr + '\n')
    try:
        data = json.loads(run.stdout)
    except json.JSONDecodeError:
        print('Resposta inválida do helper de diffs.', file=sys.stderr)
        return {}
    return {item['id']: item.get('html', '') for item in data.get('files', []) if item.get('html')}


def apply_pierre(page):
    rendered = pierre_html_by_id()
    for job in PIERRE_JOBS:
        frag = rendered.get(job['id']) or plain_diff_html(job)
        token = f'<div data-pierre="{job["id"]}"></div>'
        page = page.replace(token, f'<div class="pierre">{frag}</div>', 1)
    return page


# ---------------------------------------------------------------- citações e imagens
MD = markdown.Markdown(extensions=['tables', 'sane_lists'])


def md(src):
    MD.reset()
    return MD.convert(src)


IMG_IDS = {}


def row_html(L, R, cls):
    lc = 'md old' + ('' if L else ' empty')
    rc = 'md new' + ('' if R else ' empty')
    return f'<div class="r {cls}"><div class="{lc}">{L}</div><div class="{rc}">{R}</div></div>'


# ---------------------------------------------------------------- seções
def changed_files(a, b):
    out = git('diff', '--name-status', a, b)
    res = []
    for ln in out.strip().split('\n'):
        if not ln:
            continue
        st, *ps = ln.split('\t')
        res.append((st[0], ps[-1]))
    return res


def file_section(a, b, st, path):
    title = html.escape(path)
    if not re.search(r'\.(png|jpe?g|gif|webp|svg)$', path, re.I):
        old = git_text(a, path) if st != 'A' else ''
        new = git_text(b, path) if st != 'D' else ''
        if old is None or new is None:
            return f'<section class="file"><header><span class="fname">{title}</span><span class="badge">{st}</span></header></section>'
        before = None if st == 'A' else old
        after = None if st == 'D' else new
        nch = line_changes(old, new)
        body = queue_pierre(before, after, path)
        return (f'<section class="file"><header><span class="fname">{title}</span>'
                f'<span class="badge">{nch} linha{"s" if nch != 1 else ""} alterada{"s" if nch != 1 else ""}</span></header>'
                f'<div class="cols"><div>Antes</div><div>Depois</div></div>{body}</section>')
    if re.search(r'\.(png|jpe?g|gif)$', path, re.I) and st == 'A':
        data = git('show', f'{b}:{path}', binary=True)
        uri = 'data:image/png;base64,' + base64.b64encode(data).decode()
        if uri not in IMG_IDS:
            IMG_IDS[uri] = f'i{len(IMG_IDS)}'
        return (f'<section class="file"><header><span class="fname">{title}</span><span class="badge add">imagem nova</span></header>'
                f'<div class="r add"><div class="md old empty"></div><div class="md new"><p><img data-img="{IMG_IDS[uri]}" alt="{title}"></p></div></div></section>')
    if path.lower().endswith('.svg'):
        cells = []
        for rev, ok in ((a, st != 'A'), (b, st != 'D')):
            data = git('show', f'{rev}:{path}', binary=True) if ok else None
            if not data:
                cells.append('')
                continue
            uri = 'data:image/svg+xml;base64,' + base64.b64encode(data).decode()
            if uri not in IMG_IDS:
                IMG_IDS[uri] = f'i{len(IMG_IDS)}'
            cells.append(f'<p><img data-img="{IMG_IDS[uri]}" alt="{title}"></p>')
        return (f'<section class="file"><header><span class="fname">{title}</span><span class="badge">imagem SVG alterada</span></header>'
                f'<div class="cols"><div>Antes</div><div>Depois</div></div>{row_html(cells[0], cells[1], "mod")}</section>')
    return f'<section class="file"><header><span class="fname">{title}</span><span class="badge">{st}</span></header></section>'


PARECER = ''
if SPEC.get('parecer'):
    PARECER = git('show', f"{SPEC.get('parecer_rev', BASE)}:{SPEC['parecer']}") or ''


def citacao(c):
    """Trecho literal do parecer: de `inicio` até o fim de `fim`, ou a linha que começa em `linha`."""
    if 'linha' in c:
        i = PARECER.index(c['linha']); j = PARECER.find('\n', i)
        return PARECER[i:j if j >= 0 else None].strip()
    i = PARECER.index(c['inicio'])
    j = PARECER.index(c['fim'], i) + len(c['fim']) if c.get('fim') else PARECER.find('\n\n', i)
    return PARECER[i:j].strip()


def resolve(rev, what):
    full = (git('rev-parse', '--verify', '--quiet', f'{rev}^{{commit}}') or '').strip()
    if not full:
        sys.exit(f'Commit não encontrado ({what}): {rev}')
    return full


def conferir_rodada(base, fim, spec_items):
    """Garante que os commits de base..fim e os itens do spec sejam os mesmos e que cada item tenha citação ou nota."""
    erros = []
    commits = (git('rev-list', '--reverse', f'{base}..{fim}') or '').split()
    por_item = {resolve(it['commit'], 'item do spec'): it for it in spec_items}
    sem_item = [c for c in commits if c not in por_item]
    fora = [c for c in por_item if c not in commits]
    sem_origem = [c for c, it in por_item.items() if not it.get('citacoes') and not it.get('nota')]

    def lista(cs):
        return ''.join(f"\n  {c[:7]} {(git('log', '-1', '--format=%s', c) or '').strip()}" for c in cs)
    if sem_item:
        erros.append(f'{len(sem_item)} commit(s) de {base[:7]}..{fim[:7]} sem item no spec '
                     f'(acrescente um item com citação ou nota, ou mude `fim`):{lista(sem_item)}')
    if fora:
        erros.append(f'{len(fora)} item(ns) do spec fora de {base[:7]}..{fim[:7]} '
                     f'(confira `base`, `fim` e o campo `commit`):{lista(fora)}')
    if sem_origem:
        erros.append(f'{len(sem_origem)} item(ns) sem `citacoes` nem `nota`:{lista(sem_origem)}')
    if erros:
        sys.exit('A rodada do spec está inconsistente.\n' + '\n'.join(erros))


TIPOS = {'correcao': 'c', 'recomendacao': 'r', 'registro': 'm', 'pendencia': 'm', 'anotacao': 'm'}
FIM = resolve(SPEC['fim'], '`fim`') if SPEC.get('fim') else resolve(SPEC['itens'][-1]['commit'], 'último item')
if not SPEC.get('fim'):
    print(f'Aviso: spec sem `fim`; o Total termina no último item ({FIM[:7]}).', file=sys.stderr)
BASE = resolve(BASE, '`base`')
conferir_rodada(BASE, FIM, SPEC['itens'])
items = []
for it in SPEC['itens']:
    quotes = []
    for c in it.get('citacoes', []):
        try:
            quotes.append((c['onde'], citacao(c)))
        except ValueError:
            sys.exit(f"Âncora não encontrada no parecer para {it['commit']}: {c}")
    items.append({'h': git('rev-parse', '--short', it['commit']).strip(),
                  'cls': TIPOS.get(it.get('tipo', 'registro'), 'm'),
                  'lbl': it['rotulo'], 'title': it['titulo'],
                  'quotes': quotes, 'note': it.get('nota', '')})
sections = []
nav = []

# total
tot_files = changed_files(BASE, FIM)
stat = git('diff', '--shortstat', BASE, FIM).strip()
sections.append(('total', 'Total', f'Todas as mudanças ({BASE[:7]}..{FIM[:7]})', '',
                 ''.join(file_section(BASE, FIM, st, p) for st, p in tot_files), stat))
nav.append(('total', 'Total', 'Todas as mudanças', 't'))

def why_box(it):
    parts = []
    for where, q in it.get('quotes', []):
        parts.append(f'<div class="src">{html.escape(where)}</div><blockquote class="prof md">{md(q)}</blockquote>')
    if it.get('note'):
        parts.append(f'<p class="note"><b>Nota:</b> {html.escape(it["note"])}</p>')
    if not parts:
        return ''
    head = 'Comentário do professor que motivou esta mudança' if it.get('quotes') else 'Origem desta mudança'
    return f'<section class="why"><h3>💬 {head}</h3>{"".join(parts)}</section>'


index_rows = []
for it in items:
    h, cls, label, title = it['h'], it['cls'], it['lbl'], it['title']
    parent = git('rev-parse', f'{h}^').strip()
    files = changed_files(parent, h)
    body = why_box(it) + ''.join(file_section(parent, h, st, p) for st, p in files)
    st = git('diff', '--shortstat', parent, h).strip()
    sections.append((h, label, title, GH + h if GH else '', body, st))
    nav.append((h, label, title, cls))
    origem = '; '.join(w for w, _ in it.get('quotes', [])) or (it.get('note', '').split(':')[0] if it.get('note') else '')
    index_rows.append(f'<tr><td><a href="#s-{h}">{html.escape(label)}: {html.escape(title)}</a></td><td>{html.escape(origem)}</td><td><code>{h[:7]}</code></td></tr>')

tot = sections[0]
idx = ('<section class="why"><h3>🗺️ Qual comentário levou a cada commit</h3><div class="md"><table><thead><tr><th>Commit</th>'
       '<th>Trecho do parecer</th><th>Hash</th></tr></thead><tbody>' + ''.join(index_rows) + '</tbody></table></div></section>')
sections[0] = (tot[0], tot[1], tot[2], tot[3], idx + tot[4], tot[5])

nav_html = '\n'.join(
    f'<a href="#s-{sid}" class="k-{cls}"><span class="lbl">{html.escape(lbl)}</span>'
    f'<span class="ttl">{html.escape(t)}</span>{"" if sid == "total" else f"<code>{sid[:7]}</code>"}</a>'
    for sid, lbl, t, cls in nav)

sec_html = '\n'.join(
    f'<article id="s-{sid}"><h2><span class="lbl">{html.escape(lbl)}</span> {html.escape(t)}</h2>'
    f'<p class="meta">{"<a target=_blank href=" + url + ">" + sid[:7] + " no GitHub</a> · " if url else ""}{html.escape(st)}</p>{body}</article>'
    for sid, lbl, t, url, body, st in sections)

CSS = r"""
:root{--bg:#fbfaf8;--fg:#1d1d1f;--mut:#6b6b70;--card:#fff;--line:#e4e2dd;--del:#fde7e7;--delfg:#a3202a;--ins:#e3f5e6;--insfg:#17692b;
--delb:#f3b9bc;--insb:#a8dcb3;--acc:#3557d6;--code:#f2f1ee;--th:#f6f5f2}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#141416;--fg:#e8e6e3;--mut:#9a9aa0;--card:#1c1c1f;--line:#2e2e33;
--del:#3a1d20;--delfg:#ff9aa2;--ins:#173222;--insfg:#8be0a0;--delb:#6b2a30;--insb:#2b6a3f;--acc:#8aa4ff;--code:#26262a;--th:#222226}}
:root[data-theme="dark"]{--bg:#141416;--fg:#e8e6e3;--mut:#9a9aa0;--card:#1c1c1f;--line:#2e2e33;
--del:#3a1d20;--delfg:#ff9aa2;--ins:#173222;--insfg:#8be0a0;--delb:#6b2a30;--insb:#2b6a3f;--acc:#8aa4ff;--code:#26262a;--th:#222226}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{display:grid;grid-template-columns:300px 1fr;min-height:100vh}
nav{position:sticky;top:0;height:100vh;overflow:auto;border-right:1px solid var(--line);padding:16px 12px;background:var(--card)}
nav h1{font-size:15px;margin:0 0 4px}
nav p{font-size:12px;color:var(--mut);margin:0 0 12px}
nav a{display:block;padding:7px 8px;border-radius:8px;color:var(--fg);text-decoration:none;font-size:13px;margin-bottom:2px}
nav a:hover{background:var(--code)}
nav .lbl{display:inline-block;font-size:10.5px;font-weight:600;text-transform:uppercase;letter-spacing:.03em;padding:1px 6px;border-radius:999px;margin-right:6px;background:var(--code);color:var(--mut)}
nav .k-c .lbl{background:#fde2c4;color:#8a4a00} nav .k-r .lbl{background:#dde6ff;color:#2a45a8}
nav .k-a .lbl{background:#e8ddff;color:#5b2fb0} nav .k-m .lbl{background:#d9f2e3;color:#1c6b3b} nav .k-t .lbl{background:var(--fg);color:var(--bg)}
nav code{display:block;font-size:11px;color:var(--mut);margin-top:2px}
nav .ttl{display:inline}
main{padding:20px 24px 80px;min-width:0}
.tools{position:sticky;top:0;z-index:5;background:var(--bg);padding:8px 0 10px;border-bottom:1px solid var(--line);margin-bottom:12px}
.tools .leg{font-size:12px;color:var(--mut)}
article{margin:0 0 48px}
article h2{font-size:19px;margin:8px 0 2px}
article h2 .lbl{font-size:11px;vertical-align:middle;padding:2px 7px;border-radius:999px;background:var(--code);color:var(--mut);text-transform:uppercase}
.meta{color:var(--mut);font-size:12.5px;margin:0 0 12px}.meta a{color:var(--acc)}
.file{border:1px solid var(--line);border-radius:12px;background:var(--card);margin:0 0 18px;overflow:hidden}
.file>header{display:flex;justify-content:space-between;align-items:center;padding:9px 14px;border-bottom:1px solid var(--line);background:var(--th)}
.fname{font:600 13px ui-monospace,SFMono-Regular,Menlo,monospace}
.badge{font-size:11.5px;color:var(--mut)}
.cols{display:grid;grid-template-columns:1fr 1fr;font-size:11.5px;font-weight:600;color:var(--mut);text-transform:uppercase;letter-spacing:.04em;border-bottom:1px solid var(--line)}
.cols div{padding:5px 14px}.cols div+div{border-left:1px solid var(--line)}
.r{display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid var(--line)}
.r>.md{padding:6px 14px;min-width:0;overflow-x:auto}
.r>.md+.md{border-left:1px solid var(--line)}
.r.ctx{opacity:.62}.r.ctx .full{grid-column:1/3}
.r.del>.old{background:var(--del);box-shadow:inset 3px 0 var(--delb)}
.r.add>.new{background:var(--ins);box-shadow:inset 3px 0 var(--insb)}
.r.mod>.old{box-shadow:inset 3px 0 var(--delb)}.r.mod>.new{box-shadow:inset 3px 0 var(--insb)}
.md.empty{background:repeating-linear-gradient(135deg,transparent 0 6px,var(--code) 6px 7px)}
del{background:var(--del);color:var(--delfg);text-decoration:line-through;text-decoration-thickness:1px;border-radius:3px}
ins{background:var(--ins);color:var(--insfg);text-decoration:none;border-radius:3px}
.r.del del,.r.add ins{background:none}
details.fold{border-bottom:1px solid var(--line)}
details.fold>summary{cursor:pointer;padding:5px 14px;font-size:12px;color:var(--mut);background:var(--th);list-style:none}
details.fold>summary::-webkit-details-marker{display:none}
details.fold .md{padding:6px 14px;opacity:.75}
.md h1{font-size:20px}.md h2{font-size:18px}.md h3{font-size:16px}.md h4{font-size:15px}
.md h1,.md h2,.md h3,.md h4{margin:8px 0 6px}
.md p{margin:6px 0}.md ul,.md ol{margin:6px 0;padding-left:22px}
.md blockquote{margin:6px 0;padding:2px 12px;border-left:3px solid var(--line);color:var(--fg)}
.md table{border-collapse:collapse;font-size:12.5px;margin:6px 0;width:100%}
.md th,.md td{border:1px solid var(--line);padding:4px 7px;vertical-align:top;min-width:70px;overflow-wrap:anywhere}
.md th{background:var(--th)}
.md code{background:var(--code);padding:1px 4px;border-radius:4px;font-size:12.5px}
.md img{max-width:100%;height:auto;border-radius:6px;border:1px solid var(--line)}
.md a{color:var(--acc)}
.why{border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:12px;background:var(--card);padding:10px 16px 12px;margin:0 0 18px}
.why h3{font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--acc);margin:4px 0 8px}
.why .src{font-size:12.5px;font-weight:600;color:var(--mut);margin:8px 0 4px}
.why blockquote.prof{margin:0 0 6px;padding:4px 14px;border-left:3px solid var(--acc);background:var(--code);border-radius:0 8px 8px 0;font-size:14px}
.why .note{font-size:13px;color:var(--mut);margin:8px 0 2px}
.why table{font-size:12.5px}.why td,.why th{max-width:520px}
.pierre{min-width:0}
.pierre diffs-container{display:block}
.fallback{margin:0;padding:12px 14px;overflow:auto;font:12.5px/1.45 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre-wrap;background:var(--code);color:var(--fg)}
@media (max-width:900px){.wrap{grid-template-columns:1fr}nav{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line)}
main{padding:12px 16px}}
"""

JS = r"""
document.querySelectorAll('img[data-img]').forEach(i=>{i.src=IM[i.dataset.img]});
"""

page = apply_pierre(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title><style>{CSS}</style></head><body>
<div class="wrap"><nav><h1>{html.escape(TITLE)}</h1><p>Diff com Highlights, antes × depois. {html.escape(stat)}</p>{nav_html}</nav>
<main><div class="tools"><span class="leg">À esquerda o texto anterior, à direita o novo. Palavras alteradas ficam destacadas. Trechos iguais longos ficam recolhidos.</span></div>
{sec_html}</main></div><script>const IM={json.dumps({v: k for k, v in IMG_IDS.items()})};{JS}</script></body></html>""")
open(OUT, 'w').write(page)
print(OUT, len(page) // 1024, 'KB')
