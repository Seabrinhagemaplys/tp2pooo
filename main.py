from peca.bispo import Bispo
import utils.utils as ut
from coordenada.coordenada import Coordenada
 
b = Bispo(ut.EnumCor.BRANCO, Coordenada(7, 7))

print(b.lista_de_posssiveis_movimentos)

for i in range(8):
    for j in range(8):
        coordenada: Coordenada = Coordenada(i, j)

        if coordenada in b.lista_de_posssiveis_movimentos:
            print(f"|X|", end="")
        else:
            print("|-|", end="")
    print()