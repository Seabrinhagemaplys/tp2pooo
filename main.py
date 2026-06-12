from peca.torre import Torre
import utils.utils as ut
from coordenada.coordenada import Coordenada
 
c = Torre(ut.EnumCor.BRANCO, Coordenada(5, 3))

print(len(c.lista_de_posssiveis_movimentos))

for i in range(8):
    for j in range(8):
        coordenada: Coordenada = Coordenada(i, j)

        if coordenada in c.lista_de_posssiveis_movimentos:
            print(f"|X|", end="")
        else:
            print("|-|", end="")
    print()