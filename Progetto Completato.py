import pygame
import math
from PIL import Image

width = 1000
height = 1000

pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Gioco!')
clock = pygame.time.Clock()

i = 360
z=360
b1 = 360
b2 = 360

#======================================
verticeSx1=[500,490]
verticeDx1=[200,20]
    
verticeSx2=[700,490]
verticeDx2=[150,20]
def collisione(q,p,z):
    Qx=q[0];Qy=q[1]
    Px=p[0];Py=p[1]
    Zx=z[0];Zy=z[1]
    return (Py-Qy)*Zx+(Qx-Px)*Zy+(Px*Qy-Qx*Py) >= 0
def verificaintersezioni(lista3punti,Z):
    A = lista3punti[0]
    B = lista3punti[1]
    C = lista3punti[2]
    Avalid = collisione(A,B,Z)
    Bvalid = collisione(B,C,Z)
    Cvalid = collisione(C,A,Z)
    return Avalid and Bvalid and Cvalid
def controllotriangoli(triangolo1,triangolo2):
    A = triangolo2[0]
    B = triangolo2[1]
    C = triangolo2[2]
    verifica1 = verificaintersezioni(triangolo1,A)
    if verifica1:
        return verifica1
    verifica2 = verificaintersezioni(triangolo1,B)
    if verifica2:
        return verifica2
    verifica3 = verificaintersezioni(triangolo1,C)
    if verifica3:
        return verifica3
    D = triangolo1[0]
    E = triangolo1[1]
    F = triangolo1[2]
    verifica4 = verificaintersezioni(triangolo2,D)
    if verifica4:
        return verifica4
    verifica5 = verificaintersezioni(triangolo2,E)
    if verifica5:
        return verifica5
    verifica6 = verificaintersezioni(triangolo2,F)
    if verifica6:
        return verifica6
    
def grafica():
    global verticeSx1, verticeDx2,verticeDx1,verticeSx2
    
    pygame.draw.rect(screen,(255,255,0),(verticeSx1[0],verticeSx1[1],verticeDx1[0],verticeDx1[1]),2)
    pygame.draw.rect(screen,(255,0,255),(verticeSx2[0],verticeSx2[1],verticeDx2[0],verticeDx2[1]),2)
    pygame.draw.circle(screen,(255,255,255),(500,500),200,2)
    pygame.draw.circle(screen,(255,255,255),(500,500),350,2)
    pygame.draw.circle(screen,(255,255,255),(500,500),2,2)
    
    
def ostacoli():
    pygame.draw.polygon(screen,(0,255,255),[[550,300],[550,350],[500,325]],2)
    pygame.draw.polygon(screen,(0,255,255),[[200,500],[200,550],[150,525]],2)
    pygame.draw.rect(screen,(255,232,76),(0,800,1000,200),2)
def XYCirconference(center, radius, angle):
    global xcenter
    rad = math.radians(angle)
    xcenter = center[0]; ycenter = center[1]
    x = xcenter + radius * math.cos(rad)
    y = ycenter + radius * math.sin(rad)
    return [x,y]
def movimento():
    global z,i,c,p;
    z -= 1
    if z == 0:
        i -= 1
        z = 360
    p = XYCirconference([510,500],190,i)
    c =XYCirconference([p[0],p[1]],130,z)
    
def circlepos(angle, radius, pos):
    x = math.cos(angle) * radius + pos[0]
    y = math.sin(angle) * radius + pos[1]
    return (x, y)

def rectVertex(point, la, lb, lc, ld, rot):
    rot = math.radians(rot)
    a = circlepos(rot, la, point)
    b = circlepos(rot - math.pi, lc, point)
    return [circlepos(rot - math.pi / 2, lb, a), circlepos(rot - math.pi / 2, lb, b), circlepos(rot + math.pi / 2, ld, b), circlepos(rot + math.pi / 2, ld, a)]

def braccio1():
    global b1
    pygame.draw.polygon(screen,(255,255,0),rectVertex((500,500),200,10,0,10,b1),1)
    
def braccio2():
    global b2
    pygame.draw.polygon(screen,(255,0,255),rectVertex(circlepos(math.radians(b1), 200, (500, 500)),150,10,0,10,b2),1)
def primobraccio():
    global b1
    a,b,c,d = rectVertex((500,500),200,10,0,10,b1)
    triangolo1=[a,b,c]
    triangolo2=[a,d,c]
    return [triangolo1,triangolo2]
def secondobraccio():
    global b2
    a,b,c,d = rectVertex(circlepos(math.radians(b1), 200, (500, 500)),150,10,0,10,b2)    
    triangolo1=[a,b,c]
    triangolo2=[a,d,c]
    return [triangolo1,triangolo2]
#======================================

jpg = Image.new("RGB",(360,360))
x=0
y=0
done = False

ostacolo1 = [[550,300],[550,350],[500,325]]
ostacolo2 = [[200,500],[200,550],[150,525]]
ostacolo3 = [[0,800],[0,1000],[1000,800]]
ostacolo4 = [[0,1000],[1000,1000],[1000,800]]
l =[ostacolo1,ostacolo2,ostacolo3,ostacolo4]
try:
    while True:
        screen.fill((0,0,0))                    
        movimento()
        grafica()
        braccio2()
        triangolo1,triangolo2 = secondobraccio()
        for i in range(len(l)):
            if controllotriangoli(triangolo1,l[i]):
                jpg.putpixel((x,y),(255,0,0))
                #print(x,y)
            if controllotriangoli(triangolo2,l[i]):
                jpg.putpixel((x,y),(255,0,0))
                #print(x,y)
        b2 -= 1
        if b2 < 0:
            b2 = 360
            b1 -= 1
        braccio1()
        triangolo3,triangolo4 = primobraccio()
        ostacoli()
        pygame.display.update()
        clock.tick(300)
        for i in range(len(l)):
            if controllotriangoli(triangolo3,l[i]):
                jpg.putpixel((x,y),(255,0,0))
                #print(x,y)
            if controllotriangoli(triangolo4,l[i]):
                jpg.putpixel((x,y),(255,0,0))
                #print(x,y)
##        if (controllotriangoli(triangolo1,ostacolo1) or controllotriangoli(triangolo1,ostacolo2) or controllotriangoli(triangolo1,ostacolo3) or
##            controllotriangoli(triangolo1,ostacolo4) or controllotriangoli(triangolo2,ostacolo1) or controllotriangoli(triangolo2,ostacolo2) or
##            controllotriangoli(triangolo2,ostacolo3) or controllotriangoli(triangolo2,ostacolo4) or controllotriangoli(triangolo3,ostacolo1) or
##            controllotriangoli(triangolo3,ostacolo2) or controllotriangoli(triangolo3,ostacolo3) or controllotriangoli(triangolo3,ostacolo4) or
##            controllotriangoli(triangolo4,ostacolo1) or controllotriangoli(triangolo4,ostacolo2) or controllotriangoli(triangolo4,ostacolo3) or
##            controllotriangoli(triangolo4,ostacolo4)):
##               jpg.putpixel((x,y),(255,0,0))
##               print(x,y)
        x+=1
        if x == 359:
            x=0
            y+=1
            if y == 359:
                break
        

    
finally:
    pygame.quit()
    jpg.save("foto.jpg")
