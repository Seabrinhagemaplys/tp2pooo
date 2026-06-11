from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada


class Torre(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada):
        super().__init__(
            caractere= ut.EnumCaracteres.TORRE_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.TORRE_PRETO,
            cor=cor,
            coordenada=coordenada_inicial
        ) 

    def atualizar_lista_de_possiveis_coordenadas(self):
        pass