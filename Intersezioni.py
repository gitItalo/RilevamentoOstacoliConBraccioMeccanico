def verificaintersezioni(lista3punti,Z):
    A = lista3punti[0]
    B = lista3punti[1]
    C = lista3punti[2]
    Avalid = collisione(A,B,Z)
    Bvalid = collisione(B,C,Z)
    Cvalid = collisione(C,A,Z)
    return Avalid and Bvalid and Cvalid
