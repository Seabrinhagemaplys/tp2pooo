from peca.cavalo import Cavalo
import utils.utils as ut
from coordenada.coordenada import Coordenada
 
c = Cavalo(ut.EnumCor.BRANCO, Coordenada(7, 5))

print(len(c.lista_de_posssiveis_movimentos))

for i in range(8):
    for j in range(8):
        coordenada: Coordenada = Coordenada(i, j)

        if coordenada in c.lista_de_posssiveis_movimentos:
            print(f"|X|", end="")
        else:
            print("|-|", end="")
    print()