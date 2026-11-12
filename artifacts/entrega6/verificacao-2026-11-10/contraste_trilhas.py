# Contraste WCAG 2.x das etiquetas da alternativa B. color-mix(in srgb) = interpolação linear dos canais sRGB.
C={'verde':'#14a37f','azul':'#3b6cf6','âmbar':'#e8a317','vermelho':'#e5484d'}
h=lambda x:[int(x[i:i+2],16)/255 for i in (1,3,5)]
mix=lambda a,b,t:[a[i]*t+b[i]*(1-t) for i in range(3)]
def L(c):
    f=lambda v:v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4
    r,g,b=map(f,c);return .2126*r+.7152*g+.0722*b
def cr(a,b):
    x,y=sorted([L(a),L(b)],reverse=True);return (x+.05)/(y+.05)
W,K,G=h('#ffffff'),h('#000000'),h('#5c6066');T=h('#0a0a0a')
print('| Vídeo | v1 não selecionado | v1 selecionado | v2 não selecionado | v2 selecionado | v2 relógio do jogo |')
print('|---|---:|---:|---:|---:|---:|')
for n,c in C.items():
    c=h(c)
    v1u=cr(mix(c,K,.75),mix(c,W,.12)); v1s=cr(W,c)
    v2u=cr(T,W); v2s=cr(T,mix(c,W,.18)); v2m=min(cr(G,W),cr(G,mix(c,W,.18)))
    print(f'| {n} | {v1u:.1f}:1 | {v1s:.1f}:1 | {v2u:.1f}:1 | {v2s:.1f}:1 | {v2m:.1f}:1 |')
