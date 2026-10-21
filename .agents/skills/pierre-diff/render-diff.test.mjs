import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';
import { plainDiff, renderFiles } from './render-diff.mjs';

const helper = fileURLToPath(new URL('./render-diff.mjs', import.meta.url));

test('Highlights colore um diff dividido', async () => {
  const result = await renderFiles([{
    id: 'js',
    name: 'nota.js',
    before: 'function saudar(nome) {\n  return "Olá, " + nome;\n}\n',
    after: 'function saudar(nome) {\n  return `Olá, ${nome}!`;\n}\n',
  }]);
  assert.equal(result.highlighter, 'highlights');
  assert.equal(result.files[0].highlighted, true);
  const html = result.files[0].html;
  assert.match(html, /<diffs-container><template shadowrootmode="open">/);
  assert.match(html, /data-diff-span/);
  assert.match(html, /data-diff-type="split"/);
  assert.match(html, /saudar/);
  const colors = [...html.matchAll(/--diffs-token-light:(#[0-9a-fA-F]{6})/g)].map((match) => match[1].toLowerCase());
  assert.ok(colors.some((color) => color !== '#0a0a0a' && color !== '#ffffff' && color !== '#fafafa'));
});

test('markdown da mudança sugerida destaca o título', async () => {
  const result = await renderFiles([{
    id: 'md',
    name: 'docs/03_personas_contexto_jornada.md',
    before: '# Personas\n\nA persona P02 é secundária.\n',
    after: '# Personas\n\nA persona P02 é atendida.\n',
  }]);
  assert.equal(result.files[0].highlighted, true);
  const html = result.files[0].html;
  assert.match(html, /P02 é/);
  assert.match(html, /data-line-type="change-deletion"/);
  assert.match(html, /data-line-type="change-addition"/);
  assert.match(html, /--diffs-token-light:#[0-9a-fA-F]{6}/);
});

test('diff em texto marca linhas removidas e acrescentadas', () => {
  const text = plainDiff('linha antiga\n', 'linha nova\n', 'nota.md');
  assert.match(text, /^-linha antiga/m);
  assert.match(text, /^\+linha nova/m);
});

test('CLI --json devolve o fragmento', () => {
  const dir = mkdtempSync(join(tmpdir(), 'pierre-diff-'));
  const spec = join(dir, 'jobs.json');
  writeFileSync(spec, JSON.stringify({
    files: [{
      id: 't',
      name: 'trecho.md',
      before: '## Antes\n\nO processamento dispensa armazenamento local.\n',
      after: '## Antes\n\nO processamento reduz a CPU local. O arquivo ainda é enviado.\n',
    }],
  }));
  const run = spawnSync(process.execPath, [helper, '--json', spec], { encoding: 'utf8' });
  assert.equal(run.status, 0, run.stderr);
  const parsed = JSON.parse(run.stdout);
  assert.equal(parsed.highlighter, 'highlights');
  assert.equal(parsed.files[0].highlighted, true);
  assert.match(parsed.files[0].html, /shadowrootmode="open"/);
});
