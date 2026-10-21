/**
 * Gera um diff HTML autocontido com @pierre/diffs e o realçador Highlights.
 *
 * O HTML usa shadow root declarativo (`<diffs-container><template shadowrootmode="open">`),
 * então o tema e o realce aparecem sem JavaScript. Temas claro e escuro seguem o sistema.
 *
 * Uso, na raiz do repositório:
 *   node .agents/skills/pierre-diff/render-diff.mjs \
 *     --before antes.md --after depois.md --name docs/arquivo.md --out saida.html
 *   node .agents/skills/pierre-diff/render-diff.mjs \
 *     --before antes.md --after depois.md --name docs/arquivo.md --fragment
 *   node .agents/skills/pierre-diff/render-diff.mjs --json jobs.json
 *
 * jobs.json: { "files": [{ "id", "name", "before", "after", "lang"? }] }
 * `before` ou `after` null indicam arquivo novo ou removido.
 * A saída de --json é um JSON em stdout: { highlighter, files: [{ id, html, highlighted, error? }] }.
 *
 * Se o realce falhar, cada arquivo volta como diff unificado em <pre> e highlighted fica false.
 */
import { readFileSync, realpathSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { canUseWASM } from '@pierre/diffs';
import { preloadMultiFileDiff } from '@pierre/diffs/ssr';
import { themes as highlightsCatalog } from '@pierre/highlights/themes/loader';

const DIFFS_TAG = 'diffs-container';
const THEME = { dark: 'pierre-dark', light: 'pierre-light' };
const ZED_COLOR_ALIASES = [
  ['editor.lineHighlightBackground', 'editor.active_line.background'],
  ['editor.selectionBackground', 'element.selected'],
  ['editor.findMatchBackground', 'search.match_background'],
  ['editor.findMatchHighlightBackground', 'search.match_background'],
  ['editorBracketMatch.background', 'editor.document_highlight.bracket_background'],
  ['editorError.foreground', 'error'],
  ['editorWarning.foreground', 'warning'],
  ['editorInfo.foreground', 'info'],
  ['editorHint.foreground', 'hint'],
  ['gitDecoration.addedResourceForeground', 'created', 'terminal.ansi.green'],
  ['gitDecoration.deletedResourceForeground', 'deleted', 'terminal.ansi.red'],
  ['gitDecoration.modifiedResourceForeground', 'modified', 'terminal.ansi.blue'],
];

let themesReady = null;

function parseArgs(argv) {
  const out = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (!arg.startsWith('--')) {
      out._.push(arg);
      continue;
    }
    const key = arg.slice(2);
    const next = argv[i + 1];
    if (next == null || next.startsWith('--')) out[key] = true;
    else {
      out[key] = next;
      i++;
    }
  }
  return out;
}

function readText(path) {
  return readFileSync(path, 'utf8');
}

/**
 * @pierre/diffs 1.6.0 pede os temas por um fallbackLoader, mas
 * @pierre/theming 1.0.1 ignora esse argumento. Sem o registro abaixo,
 * pierre-dark/pierre-light disparam UnregisteredThemeError. O objeto
 * registrado segue createHighlightsTheme do próprio diffs.
 */
function createHighlightsTheme(name, raw) {
  const theme = 'themes' in raw ? raw.themes[0] : raw;
  if (theme == null) throw new Error(`Tema "${name}" vazio.`);
  const zed = { ...theme, name };
  const colors = {};
  for (const [key, value] of Object.entries(zed.style)) {
    if (typeof value === 'string') colors[key] = value;
  }
  const player = zed.style.players?.[0];
  if (player?.cursor != null) colors['editorCursor.foreground'] ??= player.cursor;
  if (player?.selection != null) colors['editor.selectionBackground'] ??= player.selection;
  for (const [target, ...sources] of ZED_COLOR_ALIASES) {
    if (colors[target] != null) continue;
    const source = sources.find((key) => colors[key] != null);
    if (source != null) colors[target] = colors[source];
  }
  const type = zed.appearance === 'light' ? 'light' : 'dark';
  return {
    name,
    type,
    colors,
    zed,
    fg: colors['editor.foreground'] ?? colors.text ?? colors.foreground ?? (type === 'light' ? '#333333' : '#bbbbbb'),
    bg: colors['editor.background'] ?? colors.background ?? (type === 'light' ? '#ffffff' : '#1e1e1e'),
  };
}

async function themeResolver() {
  const entry = fileURLToPath(import.meta.resolve('@pierre/diffs'));
  const href = pathToFileURL(join(dirname(entry), 'highlighter/themes/themeResolver.js')).href;
  const mod = await import(href);
  return mod.createDiffsThemeResolver;
}

async function ensureThemes(backend) {
  if (themesReady === backend) return;
  const createDiffsThemeResolver = await themeResolver();
  const resolver = createDiffsThemeResolver(backend);
  if (backend === 'highlights') {
    for (const name of ['pierre-dark', 'pierre-light']) {
      if (resolver.hasRegisteredTheme(name)) continue;
      const load = highlightsCatalog[name];
      if (load == null) throw new Error(`Tema Highlights ausente: ${name}`);
      resolver.registerTheme(name, async () => createHighlightsTheme(name, (await load()).default));
    }
  } else {
    const { themes } = await import('@pierre/theming/themes');
    const { normalizeTheme, createCssVariablesTheme } = await import('shiki/core');
    for (const name of ['pierre-dark', 'pierre-light']) {
      if (resolver.hasRegisteredTheme(name)) continue;
      resolver.registerTheme(name, async () => {
        const descriptor = themes.getTheme(name);
        if (descriptor == null) throw new Error(`Tema Shiki ausente: ${name}`);
        const result = await descriptor.load();
        const loaded = result.default ?? result;
        if (loaded.cssVariables != null) {
          return { ...loaded, textmate: normalizeTheme(createCssVariablesTheme(loaded.cssVariables)) };
        }
        if (loaded.textmate != null) return { ...loaded, textmate: normalizeTheme(loaded.textmate) };
        const textmate = normalizeTheme(loaded);
        return {
          name: textmate.name,
          type: textmate.type,
          fg: textmate.fg,
          bg: textmate.bg,
          colors: textmate.colors,
          textmate,
        };
      });
    }
  }
  themesReady = backend;
}

const HIGHLIGHTERS = new Set(['highlights', 'shiki-js', 'shiki-wasm']);

export function chooseHighlighter(explicit) {
  const requested = explicit ?? process.env.PIERRE_HIGHLIGHTER;
  if (requested != null && requested !== '') {
    if (!HIGHLIGHTERS.has(requested)) {
      throw new Error(`Realçador desconhecido: ${requested}`);
    }
    return requested;
  }
  return canUseWASM() ? 'highlights' : 'shiki-js';
}

function fileContents(name, contents, lang) {
  const file = { name, contents: contents ?? '' };
  if (lang) file.lang = lang;
  return file;
}

export function wrapDiff(prerenderedHTML) {
  return `<${DIFFS_TAG}><template shadowrootmode="open">${prerenderedHTML}</template></${DIFFS_TAG}>`;
}

export function plainDiff(before, after, name) {
  const a = (before ?? '').replace(/\n$/, '').split('\n');
  const b = (after ?? '').replace(/\n$/, '').split('\n');
  if (a.length * b.length > 250000) {
    return [`--- ${name}`, ...a.map((line) => `-${line}`), `+++ ${name}`, ...b.map((line) => `+${line}`)].join('\n');
  }
  const n = a.length;
  const m = b.length;
  const dp = Array.from({ length: n + 1 }, () => new Uint32Array(m + 1));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }
  const lines = [`--- ${name}`, `+++ ${name}`];
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    if (a[i] === b[j]) {
      lines.push(` ${a[i]}`);
      i++;
      j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) {
      lines.push(`-${a[i]}`);
      i++;
    } else {
      lines.push(`+${b[j]}`);
      j++;
    }
  }
  while (i < n) lines.push(`-${a[i++]}`);
  while (j < m) lines.push(`+${b[j++]}`);
  return lines.join('\n');
}

function escapeHtml(value) {
  return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

export function plainFragment(file) {
  const body = escapeHtml(plainDiff(file.before, file.after, file.name || 'arquivo'));
  return `<pre class="pierre-diff-fallback" style="overflow:auto;padding:12px 14px;border-radius:12px;background:#f6f5f2;color:#1d1d1f;font:12.5px/1.45 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre-wrap">${body}</pre>`;
}

const DIFF_OPTIONS = {
  theme: THEME,
  themeType: 'system',
  diffStyle: 'split',
  overflow: 'wrap',
  lineDiffType: 'word-alt',
  disableFileHeader: false,
};

async function renderOne(file, preferredHighlighter) {
  const oldFile = file.before == null ? null : fileContents(file.name, file.before, file.lang);
  const newFile = file.after == null ? null : fileContents(file.name, file.after, file.lang);
  const result = await preloadMultiFileDiff({
    oldFile,
    newFile,
    options: {
      ...DIFF_OPTIONS,
      preferredHighlighter,
      disableFileHeader: file.header === false,
    },
  });
  return wrapDiff(result.prerenderedHTML);
}

export async function renderFiles(files, options = {}) {
  const preferredHighlighter = chooseHighlighter(options.preferredHighlighter);
  let ready = true;
  let setupError = null;
  try {
    await ensureThemes(preferredHighlighter);
  } catch (error) {
    ready = false;
    setupError = error instanceof Error ? error.message : String(error);
  }
  const rendered = [];
  for (const file of files) {
    if (!ready) {
      rendered.push({ id: file.id, html: plainFragment(file), highlighted: false, error: setupError });
      continue;
    }
    try {
      rendered.push({ id: file.id, html: await renderOne(file, preferredHighlighter), highlighted: true });
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      rendered.push({ id: file.id, html: plainFragment(file), highlighted: false, error: message });
    }
  }
  return { highlighter: ready ? preferredHighlighter : null, files: rendered };
}

export function pageHtml(title, fragments) {
  const body = fragments.map((html) => `<div class="diff">${html}</div>`).join('\n');
  return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${escapeHtml(title)}</title>
<style>
  html,body{margin:0;background:#fafafa;color:#171717}
  @media (prefers-color-scheme: dark){html,body{background:#0a0a0a;color:#fafafa}}
  main{padding:24px;display:flex;flex-direction:column;gap:16px}
  diffs-container{display:block;border-radius:12px;overflow:hidden}
</style></head><body><main>
${body}
</main></body></html>`;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  let files;
  let title = args.title || 'Diff';
  if (args.json) {
    const spec = JSON.parse(readText(args.json));
    files = spec.files;
    if (spec.title) title = spec.title;
  } else if (args.before != null && args.after != null && args.name) {
    files = [{
      id: 'file',
      name: args.name,
      before: readText(args.before),
      after: readText(args.after),
      lang: args.lang,
    }];
  } else {
    console.error('Informe --json jobs.json ou --before, --after e --name.');
    process.exit(2);
  }
  const result = await renderFiles(files);
  for (const file of result.files) {
    if (!file.highlighted) console.error(`Diff em texto para ${file.id}: ${file.error || 'realce indisponível'}`);
  }
  if (args.json && !args.out && !args.fragment) {
    process.stdout.write(JSON.stringify(result));
    return;
  }
  const html = args.fragment
    ? result.files.map((file) => file.html).join('\n')
    : pageHtml(title, result.files.map((file) => file.html));
  if (args.out) {
    writeFileSync(args.out, html);
    console.error(args.out);
  } else {
    process.stdout.write(html);
  }
}

function invokedDirectly() {
  if (!process.argv[1]) return false;
  try {
    return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url));
  } catch {
    return false;
  }
}
if (invokedDirectly()) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.stack || error.message : error);
    process.exit(1);
  });
}
