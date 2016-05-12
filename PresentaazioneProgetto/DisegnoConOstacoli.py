import pygame
import math

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

verticeSx1=[500,490]
verticeDx1=[200,20]
    
verticeSx2=[700,490]
verticeDx2=[150,20]

def circlepos(angle, radius, pos):
    x = math.cos(angle) * radius + pos[0]
    y = math.sin(angle) * radius + pos[1]
    return (x, y)


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

def braccio1():
    global b1
    pygame.draw.polygon(screen,(255,255,0),rectVertex((500,500),200,10,0,10,b1),1)
    
def braccio2():
    global b2
    pygame.draw.polygon(screen,(255,0,255),rectVertex(circlepos(math.radians(b1), 200, (500, 500)),150,10,0,10,b2),1)

def rectVertex(point, la, lb, lc, ld, rot):
    rot = math.radians(rot)
    a = circlepos(rot, la, point)
    b = circlepos(rot - math.pi, lc, point)
    return [circlepos(rot - math.pi / 2, lb, a), circlepos(rot - math.pi / 2, lb, b), circlepos(rot + math.pi / 2, ld, b), circlepos(rot + math.pi / 2, ld, a)]
def movimento():
    global z,i,c,p;
    z -= 1
    if z == 0:
        i -= 1
        z = 360
    p = XYCirconference([510,500],190,i)
    c = XYCirconference([p[0],p[1]],130,z)

try:
    while True:
        screen.fill((0,0,0))                    
        grafica()
        braccio2()
        braccio1()
        ostacoli()
        movimento()
        pygame.display.update()
        clock.tick(200)


finally:
    pygame.quit()
