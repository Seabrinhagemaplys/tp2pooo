from peca.peca import Peca
import utils.utils as ut

class Bispo(Peca):
    def __init__(self, cor: ut.EnumCor):
        super().__init__(
            caractere= ut.EnumCaracteres.BISPO_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.BISPO_PRETO,
            cor=cor
        ) 