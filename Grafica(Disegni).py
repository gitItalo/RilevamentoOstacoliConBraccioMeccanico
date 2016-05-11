def grafica():
    global verticeSx1, verticeDx2,verticeDx1,verticeSx2
    
    pygame.draw.rect(screen,(255,255,0),(verticeSx1[0],verticeSx1[1],verticeDx1[0],verticeDx1[1]),2)
    pygame.draw.rect(screen,(255,0,255),(verticeSx2[0],verticeSx2[1],verticeDx2[0],verticeDx2[1]),2)
    pygame.draw.circle(screen,(255,255,255),(500,500),200,2)
    pygame.draw.circle(screen,(255,255,255),(500,500),350,2)
    pygame.draw.circle(screen,(255,255,255),(500,500),2,2)

