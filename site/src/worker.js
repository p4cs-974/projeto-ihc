const LIMITE = 20_000;

const json = (dados, status = 200) =>
  new Response(JSON.stringify(dados), { status, headers: { 'content-type': 'application/json' } });

export default {
  async fetch(req, env) {
    const { pathname } = new URL(req.url);
    if (pathname !== '/api/feedback') return env.ASSETS.fetch(req);
    if (req.method !== 'POST') return json({ erro: 'use POST' }, 405);

    const texto = await req.text();
    if (texto.length > LIMITE) return json({ erro: 'corpo grande demais' }, 413);

    let corpo;
    try { corpo = JSON.parse(texto); } catch { return json({ erro: 'JSON inválido' }, 400); }

    // campo escondido no formulário: só robôs preenchem
    if (corpo.site) return json({ ok: true }, 201);

    const { respostas } = corpo;
    if (!respostas || typeof respostas !== 'object' || Array.isArray(respostas))
      return json({ erro: 'respostas ausentes' }, 400);

    await env.DB.prepare('INSERT INTO feedback (versao, respostas) VALUES (?, ?)')
      .bind(String(corpo.versao ?? '').slice(0, 20), JSON.stringify(respostas))
      .run();
    return json({ ok: true }, 201);
  },
};
