def movimento():
    global z,i,c,p;
    z -= 1
    if z == 0:
        i -= 1
        z = 360
    p = XYCirconference([510,500],190,i)
    c = XYCirconference([p[0],p[1]],130,z)
