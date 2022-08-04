from math import inf

from geocomp.common import control
from geocomp.common.prim import *
from geocomp.common.segment import Segment


def Embrulho_Presente(l):
    print("\n")
    n = len(l)
    h = 0
    pos_menor = posicao_menor(l)
    S = [None for i in range(len(l))]

    l[pos_menor].hilight()

    H = [pos_menor]
    cond = True

    control.sleep()

    while cond:

        i = (H[h] % n) + 1
        if i == n:
            i = 0

        for j in range(0, n):
            ponto_t = l[j]
            segm_t = Segment(l[H[h]], l[i])
            segm_t.hilight()
            ponto_t.hilight()

            if i != j and j != H[h] and not Esquerda(H[h], i, j, l):
                if S[i] is not None:
                    S[i].hilight("blue")
                i = j

            control.sleep()

            segm_t.hilight("blue")
            ponto_t.hilight("blue")

        h += 1
        H.append(i)

        cond = (i != H[0])

        for k in range(0, len(S)):
            segm_t = S[k]

            if segm_t is not None:
                if k != len(H) - 1:
                    segm_t = Segment(l[H[k]], l[H[k + 1]])
                else:
                    segm_t = Segment(l[H[k]], l[H[0]])

                segm_t.hilight()

        control.sleep()
    print(H)


# Encontra o ponto com a menor coordenada X.
def posicao_menor(l):
    p_i = 0
    for i in range(1, len(l)):
        ponto = l[i]
        if ponto.x < l[p_i].x:
            p_i = i
    return p_i


# Teste de esquerda entre um segmento (i, j) e o ponto(k)
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
