from peca.rainha import Rainha
import utils.utils as ut
from coordenada.coordenada import Coordenada
 
c = Rainha(ut.EnumCor.BRANCO, Coordenada(3, 0))

print(len(c.lista_de_posssiveis_movimentos))

for i in range(8):
    for j in range(8):
        coordenada: Coordenada = Coordenada(i, j)

        if coordenada in c.lista_de_posssiveis_movimentos:
            print(f"|X|", end="")
        else:
            print("|-|", end="")
    print()