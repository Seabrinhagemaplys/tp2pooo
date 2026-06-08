from peca.peca import Peca
import utils.utils as ut

class Torre(Peca):
    def __init__(self, cor: ut.EnumCor):
        super().__init__(
            caractere= ut.EnumCaracteres.TORRE_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.TORRE_PRETO,
            cor=cor
        ) 