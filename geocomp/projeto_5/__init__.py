from . import embrulho_presente
from . import graham

children = [
			['embrulho_presente', 'Embrulho_Presente', 'Embrulho de Presente'],
			['graham', 'Graham', 'Algoritmo de Graham']
			]

__all__ = [a[0] for a in children]
