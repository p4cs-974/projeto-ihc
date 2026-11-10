import sys
from playwright.sync_api import sync_playwright
U='http://localhost:8762/';OUT=sys.argv[1];SP=sys.argv[2]
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium'); pg=b.new_page(viewport={'width':1280,'height':800})
  errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto(U+'PROTOTIPO_fluxo_highlights.html?tela=4&variant=C'); pg.wait_for_selector('.vc-row')
  pg.wait_for_selector('#toast',state='hidden',timeout=8000); pg.mouse.move(5,790)
  pg.screenshot(path=OUT+'/E06-P04C_mosaico_v2.png')
  pg.goto(U+'prototipo_fluxo_01.svg'); pg.set_viewport_size({'width':1120,'height':730}); pg.screenshot(path=SP+'/svg.png')
  print('erros:',errs)
  b.close()
