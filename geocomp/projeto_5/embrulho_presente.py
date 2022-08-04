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

    l[pos_menor].hilight("yellow")

    H = [pos_menor]
    cond = True

    control.sleep()

    while cond:

        i = (H[h] % n) + 1
        if i == n:
            i = 0

        for j in range(0, n):

            if i != j and j != H[h] and not Esquerda(H[h], i, j, l):
                i = j

            control.sleep()

        h += 1
        H.append(i)

        segm_t = Segment(l[H[h-1]], l[H[h]])
        segm_t.hilight()

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

    segm = Segment(A, B)
    C.hilight("blue")
    segm.hilight("blue")
    control.sleep()
    segm.unhilight()
    C.unhilight()


    det = area2(A, B, C)

    # Colineares
    if det == 0:
        print("Colineares: ", i, j, k)
        return True

    return det > 0
