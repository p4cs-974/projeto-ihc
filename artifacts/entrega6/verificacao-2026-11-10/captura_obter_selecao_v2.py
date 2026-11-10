import sys
from playwright.sync_api import sync_playwright
U='http://localhost:8762/PROTOTIPO_fluxo_highlights.html';OUT=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium'); pg=b.new_page(viewport={'width':1280,'height':800})
  errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto(U+'?tela=4&variant=A'); pg.wait_for_selector('[data-row=suarez]')
  pg.wait_for_selector('#toast',state='hidden',timeout=8000)
  pg.click('[data-row=suarez] [data-incl]'); pg.click('[data-row=bravo] [data-incl]')
  pg.click('#dl'); pg.wait_for_selector('.obt'); pg.wait_for_timeout(600); pg.mouse.move(5,790)
  pg.screenshot(path=OUT+'/E06-P04S_obter_selecao_v2.png')
  print('erros:',errs)
  b.close()
