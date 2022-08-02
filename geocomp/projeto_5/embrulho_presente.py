from math import inf

from geocomp.common.prim import *


def Esquerda(self, i, j):
    A = self.lista[i]
    B = self.lista[j]

    det = area2(A.init, A.to, B.init)

    if A.init.x > B.init.x:
        return not self.Esquerda(j, i)

    if (A.init.x == B.init.x) and (j > i):
        return not self.Esquerda(j, i)

    if det == 0:
        det = area2(A.init, A.to, B.to)

        if det == 0:
            return B.init.x > A.init.x

    return det > 0


def Embrulho_Presente(l):
    print("\n")
    n = len(l)
    h = menor(l)
    i = h + 1
    print("H: ", h)
    while i%n != h:
        print(i)
        i += 1


def menor(l):
    p_i = 0
    for i in range(1, len(l)):
        ponto = l[i]
        if ponto.x < l[p_i].x:
            p_i = i

    return p_i
