from math import inf

from geocomp.common.prim import *


def Embrulho_Presente(l):
    print("\n")
    n = len(l)
    h = 0
    H = [posicao_menor(l)]
    cond = True

    while cond:
        i = (H[h] % n) + 1

        if i == n:
            i = 0

        for j in range(0, n):
            if i != j and j != H[h] and not Esquerda(H[h], i, j, l):
                i = j

        h += 1
        H.append(i)
        cond = (i != H[0])

    print(H)


def posicao_menor(l):
    p_i = 0
    for i in range(1, len(l)):
        ponto = l[i]
        if ponto.x < l[p_i].x:
            p_i = i
    return p_i


def Esquerda(i, j, k, l):
    A = l[i]
    B = l[j]
    C = l[k]

    det = area2(A, B, C)

    # Colineares
    if det == 0:
        print("Colineares: ", i, j, k)
        return True

    return det > 0
