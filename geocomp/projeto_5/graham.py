from math import inf

from geocomp.common.point import Point
from geocomp.common.prim import *


def Graham(l):
    print("\n")
    H = [0 for i in range(len(l))]
    fila = ordena(l)

    H[0] = 0
    H[1] = 1
    H[2] = 2
    h = 2

    for k in range(3, len(fila)):
        j = h
        while not Esquerda(H[j - 1], H[j], k, l, fila):
            j = j - 1

        h = j + 1
        H[h] = k

    for i in range(len(H)):
        print(l[fila[H[i]][0]])


def ordena(l):
    k = posicao_menor(l)
    origem = l[k]
    fila = para_coordenadas_polares(l, origem)
    mergesort(0, len(fila), fila)

    return fila


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

    # Colineares
    if det == 0:
        print("Colineares: ", i, j, k)
        return True

    return det > 0


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
