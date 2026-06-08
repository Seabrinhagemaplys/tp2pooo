from peca.peca import Peca
import utils.utils as ut

class Rainha(Peca):
    def __init__(self, cor: ut.EnumCor):
        super().__init__(
            caractere= ut.EnumCaracteres.RAINHA_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.RAINHA_PRETO,
            cor=cor
        ) 