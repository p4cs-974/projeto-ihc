# Conclusão natural na Tela 3 (reprodução real até o fim) e retorno da base ao acompanhamento.
import sys,json
from playwright.sync_api import sync_playwright
U='http://localhost:8762/PROTOTIPO_fluxo_highlights.html'; OUT=sys.argv[1] if len(sys.argv)>1 else None
ok=0;n=0
def ck(name,c,info=''):
    global ok,n;n+=1;ok+=bool(c);print(('OK  ' if c else 'FALHA ')+name,info)
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium'); pg=b.new_page(viewport={'width':1280,'height':800})
  errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto(U); pg.click('#use-mock:not([disabled])'); pg.click('#start')
  pg.wait_for_function("done().length>=1",timeout=90000)
  pg.click('#t3-next'); pg.wait_for_selector('#t4:not([hidden])')
  pg.click('#lote [data-go="3"]'); pg.wait_for_selector('#t3:not([hidden])')
  pg.wait_for_timeout(3000)
  ck('Volta ao acompanhamento e a reprodução continua', pg.evaluate("A.state==='running'&&A.slots.some(l=>l&&l.ph==='play'&&!l.el.paused)"))
  pg.wait_for_function("A.state==='done'",timeout=240000); pg.wait_for_timeout(1500)
  ck('Conclusão comunicada no topo', 'Análise concluída' in pg.inner_text('#t3-st'), pg.inner_text('#t3-st'))
  ck('Botão de continuar habilitado', not pg.is_disabled('#t3-next') and pg.inner_text('#t3-next')=='Ver os 8 lances na base →', pg.inner_text('#t3-next'))
  if OUT: pg.screenshot(path=OUT+'/E06-P03_analise_concluida_v2.png')
  pg.click('#t3-next'); pg.wait_for_selector('#t4:not([hidden])')
  ck('Base completa', pg.evaluate("base().length")==8)
  ck('Sem erros de página', not errs, '; '.join(errs))
  b.close()
print('RESUMO',ok,'/',n)
