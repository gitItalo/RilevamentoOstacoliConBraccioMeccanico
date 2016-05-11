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
