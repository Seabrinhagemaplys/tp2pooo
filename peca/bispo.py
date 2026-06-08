from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada

class Bispo(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada ):
        super().__init__(
            caractere= ut.EnumCaracteres.BISPO_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.BISPO_PRETO,
            cor=cor,
            coordenada=coordenada_inicial
        ) 