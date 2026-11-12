import sys
from playwright.sync_api import sync_playwright
U='http://localhost:8761/PROTOTIPO_fluxo_highlights.html'; OUT=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium'); pg=b.new_page(viewport={'width':1280,'height':800})
  pg.goto(U+'?tela=3'); pg.wait_for_function("document.querySelector('#k-hl').textContent.length>0"); pg.wait_for_timeout(2500)
  pg.evaluate("()=>{finishAll();buildTracks();paintT3()}"); pg.wait_for_timeout(500)
  pg.screenshot(path=OUT+'/E06-P03_analise_concluida_v1.png')
  pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(600)
  pg.screenshot(path=OUT+'/E06-P04A_busca_v1.png')
  pg.click('[data-vt=B]'); pg.wait_for_timeout(400)
  pg.click('[data-bm=vidal]'); pg.wait_for_timeout(300); pg.click('.pop [data-incl]'); pg.click('[data-close]'); pg.wait_for_timeout(300)
  pg.screenshot(path=OUT+'/E06-P04B_trilhas_v1.png')
  pg.click('[data-vt=C]'); pg.wait_for_timeout(400)
  pg.screenshot(path=OUT+'/E06-P04C_mosaico_v1.png')
  b.close()
