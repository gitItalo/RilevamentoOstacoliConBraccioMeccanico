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
