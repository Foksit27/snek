import pygame as py
import random as r

pix = 50
col_a = 1
fps = 4
is_m_a= False
one = 1

a_a = py.image.load("apple.png")
a_ff_a = py.image.load("fastfood appie.png")
a_mk_a = py.image.load("mini apple.png")
a_n_a = py.image.load("nosing apple.png")
a_m_a = py.image.load("much apple.png")
a_a = py.transform.scale(a_a, (pix, pix))
a_ff_a = py.transform.scale(a_ff_a, (pix, pix))
a_mk_a = py.transform.scale(a_mk_a, (pix, pix))
a_n_a = py.transform.scale(a_n_a, (pix, pix))
a_m_a = py.transform.scale(a_m_a, (pix, pix))

pix = 50
res1 = 500
res2 = 700
x = 5 * pix
y = 3 * pix
xa = r.randint(0, (res1 // pix - 1)) * pix
ya = r.randint(0, (res2 // pix - 1)) * pix
xas = r.randint(0, (res1 // pix - 1)) * pix
yas = r.randint(0, (res2 // pix - 1)) * pix
dx = 0
dy = 0
FPS = py.time.Clock()
s = [[5 * pix, 5 * pix], [5 *pix, 4 * pix], [x, y]]
apple_cord = [[xa, ya]]

col = py.Color(0, 170, 176)
py.init()
# a_i = py.transform.scale(a_i,(res, res2))
apple =  r.choice([a_a, a_ff_a, a_mk_a, a_m_a])
# apple_s =  r.choice([a_m_a])

scren = py.display.set_mode([res1, res2])
while True:
    a = py.key.get_pressed()
    if a[py.K_w]:
        dx = 0
        dy = -1
    elif a[py.K_s]:
        dx = 0
        dy = 1
    elif a[py.K_a]:
        dx = -1
        dy = 0
    elif a[py.K_d]:
        dx = 1
        dy = 0
    # рисуем поле
    for i in range(res1 // pix):
        for o in range(res2 // pix):
            py.draw.rect(scren,py.Color(107, 255, 114) if  (i + o) % 2 == 0 else py.Color(43, 110, 48), (i * pix, o * pix, pix, pix))
    # рисуем змию
    x = x + dx *pix
    y = y + dy *pix
    # змецка передвигается / растёт
    s.append([x,y])
    print(s)
    if x == xa and y == ya:
        for i in range(len(apple_cord)):
            if apple_cord[i][0] == xa and apple_cord[i][1] == ya:
                apple_cord.pop(i)
                break
        # опредиляем яблоко
        if apple == a_a:
            # перемещаем яблоко
            for i in range(one):
                xa = r.randint(0, (res1 // pix - 1)) * pix
                ya = r.randint(0, (res2 // pix - 1)) * pix
                apple_cord.append([xa, ya])
            apple =  r.choice([a_a, a_ff_a, a_mk_a, a_n_a, a_m_a])
        elif apple == a_ff_a:
            for i in range(one):
                xa = r.randint(0, (res1 // pix - 1)) * pix
                ya = r.randint(0, (res2 // pix - 1)) * pix
                apple_cord.append([xa, ya])
            s.append([x,y])
            apple =  r.choice([a_a, a_ff_a, a_m_a]) 
        elif apple == a_mk_a:
            for i in range(one):
                xa = r.randint(0, (res1 // pix - 1)) * pix
                ya = r.randint(0, (res2 // pix - 1)) * pix
                apple_cord.append([xa, ya])
            s.pop(0)
            apple =  r.choice([a_ff_a, a_mk_a, a_m_a]) 
        elif apple == a_n_a:
            for i in range(one):
                xa = r.randint(0, (res1 // pix - 1)) * pix
                ya = r.randint(0, (res2 // pix - 1)) * pix
                apple_cord.append([xa, ya])
            s.pop(0)
            apple =  r.choice([a_a, a_ff_a, a_mk_a, a_n_a, a_m_a])
        elif apple == a_m_a:
            for i in range(one):
                xa = r.randint(0, (res1 // pix - 1)) * pix
                ya = r.randint(0, (res2 // pix - 1)) * pix
                apple_cord.append([xa, ya])
            is_m_a = True
            one += 1
            apple =  r.choice([a_a, a_ff_a, a_mk_a, a_n_a, a_m_a])
    else:
        s.pop(0)
    # if x == xas and y == yas:
    #     fps =- 3
    #     xas = r.randint(0, (res1 // pix - 1)) * pix
    #     yas = r.randint(0, (res2 // pix - 1)) * pix
    #     apple_s =  r.choice([a_m_a])
    # else:
    #     s.pop(0)
    for x, y in s:
        py.draw.rect(scren, col, (x, y, pix, pix))
    FPS.tick(fps)
    # рисуем яблоки
    for i in range(len(apple_cord)):
        scren.blit(apple, (apple_cord[i][0], apple_cord[i][1]))
    # scren.blit(a_i,(0,0))
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    py.display.flip()