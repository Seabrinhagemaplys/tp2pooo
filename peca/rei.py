from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada


class Rei(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada):
        super().__init__(
            caractere= ut.EnumCaracteres.REI_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.REI_PRETO,
            cor=cor,
            coordenada=coordenada_inicial
        ) 

    def atualizar_lista_de_possiveis_coordenadas(self):
        pass