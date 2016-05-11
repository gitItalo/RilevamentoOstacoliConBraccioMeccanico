def collisione(q,p,z):
    Qx=q[0];Qy=q[1]
    Px=p[0];Py=p[1]
    Zx=z[0];Zy=z[1]
    return (Py-Qy)*Zx+(Qx-Px)*Zy+(Px*Qy-Qx*Py) >= 0
