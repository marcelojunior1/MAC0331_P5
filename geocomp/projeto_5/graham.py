from math import inf

from geocomp.common import control
from geocomp.common.point import Point
from geocomp.common.prim import *
from geocomp.common.segment import Segment


def Graham(l):
    print("\n")

    fila = ordena(l)

    H = [0 for i in range(len(l))]
    H[0] = 0
    H[1] = 1
    H[2] = 2
    h = 2

    p0 = l[fila[H[0]][0]]
    p1 = l[fila[H[1]][0]]
    p2 = l[fila[H[2]][0]]
    S = [(Segment(p0, p1)), (Segment(p1, p2))]

    S[0].hilight()
    S[1].hilight()

    control.sleep()

    for k in range(3, len(fila)):
        j = h
        while not Esquerda(H[j - 1], H[j], k, l, fila):
            j = j - 1

        h = j + 1

        if H[h] != 0:
            p = len(S) - h + 1
            for a in range(p):
                S[len(S)-1].unhilight()
                S.pop()

        H[h] = k

        ponto1 = l[fila[H[h - 1]][0]]
        ponto2 = l[fila[H[h]][0]]

        if len(S) == h - 1:
            S.append(Segment(ponto1, ponto2))
        else:
            S[h - 1] = Segment(ponto1, ponto2)

        S[h - 1].hilight()

        control.sleep()

        if k == len(fila) - 1:
            ponto1 = l[fila[H[h]][0]]
            ponto2 = l[fila[H[0]][0]]

            print(S, len(S), h)

            S.append(Segment(ponto1, ponto2))
            S[h].hilight()


# Cria a fila de pontos
def ordena(l):
    k = posicao_menor(l)
    origem = l[k]
    origem.hilight()
    fila = para_coordenadas_polares(l, origem)
    mergesort(0, len(fila), fila)

    return fila


# Encontra o ponto com menor coordenada Y
def posicao_menor(l):
    p_i = 0
    for i in range(1, len(l)):
        ponto = l[i]
        if ponto.y < l[p_i].y:
            p_i = i
    return p_i


def Esquerda(i, j, k, l, fila):
    A = l[fila[i][0]]
    B = l[fila[j][0]]
    C = l[fila[k][0]]
    det = area2(A, B, C)

    segm = Segment(A, B)
    C.hilight("blue")
    segm.hilight("blue")
    control.sleep()
    segm.unhilight()
    C.unhilight()

    # Colineares
    if det == 0:
        #print("Colineares: ", i, j, k)
        return False

    return det > 0


# Ordena a fila de pontos
def mergesort(p, r, fila):
    if p < (r - 1):
        q = math.floor((p + r) / 2)

        mergesort(p, q, fila)
        mergesort(q, r, fila)
        intercala(p, q, r, fila)


def intercala(p, q, r, fila):
    w = [None for i in range((r - p))]

    for i in range(p, q):
        w[i - p] = fila[i]
    for j in range(q, r):
        w[r - p + q - j - 1] = fila[j]

    i = 0
    j = r - p - 1

    for k in range(p, r):

        y1 = w[i][1]
        y2 = w[j][1]

        cond = y1 < y2

        if cond:
            fila[k] = w[i]
            i += 1
        else:
            fila[k] = w[j]
            j -= 1


# Transforma os pontos em coordenadas polares
def para_coordenadas_polares(l, origem):
    tam_l = len(l)
    fila = []

    for i in range(tam_l):
        p1 = l[i]
        xc = origem.x
        yc = origem.y
        x1 = p1.x
        y1 = p1.y
        r1 = (x1 - xc) ** 2 + (y1 - yc) ** 2

        xt1 = abs(x1 - xc)
        yt1 = abs(y1 - yc)

        if x1 < xc:
            xt1 *= -1
        if y1 < yc:
            yt1 *= -1

        theta_1 = math.atan2(yt1, xt1)

        if theta_1 < 0:
            theta_1 = 2 * math.pi + theta_1

        raio = r1

        fila.append([i, theta_1, raio])

    return fila
