# -*- coding: utf-8 -*-

"""Algoritmos de Geometria Computacional

Sub-modulos:
- closest: algoritmos para encontar o par de pontos mais próximo
- lineintersections: algoritmos para encontrar todas as intersecções de segmentos

- common:     classes e operacoes usadas por diversos algoritmos
- gui:        implementacoes das operacoes graficas
"""

from . import closest
from . import lineintersections
from . import projeto_5

from .common.guicontrol import init_display
from .common.guicontrol import plot_input
from .common.guicontrol import run_algorithm
from .common.guicontrol import open_file
from .common.prim import get_count
from .common.prim import reset_count

children = (   ( 'lineintersections',  None, 'Interseção de Todos os  Segs - Beatriz & Igor' ),
               ( 'closest',  None, 'Par Mais Prox -  Gabriel & Luis' ),
               ('projeto_5', None, 'Projeto 5')

	)

__all__ = [p[0] for p in children]
