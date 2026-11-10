import sys
from playwright.sync_api import sync_playwright
U='http://localhost:8762/PROTOTIPO_fluxo_highlights.html';OUT=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium'); pg=b.new_page(viewport={'width':1280,'height':800})
  errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto(U+'?tela=4&variant=B'); pg.wait_for_selector('.vb-card')
  pg.click('[data-bm=vidal]'); pg.click('.pop [data-incl]'); pg.click('.pop [data-close]'); pg.wait_for_timeout(400)
  pg.mouse.move(5,790); pg.evaluate('scrollTo(0,0)'); pg.wait_for_selector('#toast',state='hidden',timeout=8000)
  boxes=pg.evaluate("()=>[...document.querySelectorAll('.bm')].map(e=>{const r=e.getBoundingClientRect();return [e.dataset.bm,r.left,r.right,r.top]})")
  lanes=pg.evaluate("()=>[...document.querySelectorAll('.lane-t')].map(t=>{const a=t.getBoundingClientRect();return [...t.querySelectorAll('.bm')].every(m=>{const r=m.getBoundingClientRect();return r.left>=a.left&&r.right<=a.right})})")
  print('dentro da faixa:',lanes)
  ov=[(a[0],c[0]) for i,a in enumerate(boxes) for c in boxes[i+1:] if abs(a[3]-c[3])<5 and a[1]<c[2] and c[1]<a[2]]
  print('etiquetas:',len(boxes),'sobreposições:',ov,'| erros:',errs)
  pg.screenshot(path=OUT+'/E06-P04B_trilhas_v2.png')
  b.close()
