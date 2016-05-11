def movimento():
    global z,i,c,p;
    z -= 1
    if z == 0:
        i -= 1
        z = 360
    p = XYCirconference([510,500],190,i)
    c =XYCirconference([p[0],p[1]],130,z)

def braccio1():
    global b1
    pygame.draw.polygon(screen,(255,255,0),rectVertex((500,500),200,10,0,10,b1),1)
    
def braccio2():
    global b2
    pygame.draw.polygon(screen,(255,0,255),rectVertex(circlepos(math.radians(b1), 200, (500, 500)),150,10,0,10,b2),1)
