from peca.peca import Peca
import utils.utils as ut

class Cavalo(Peca):
    def __init__(self, cor: ut.EnumCor):
        super().__init__(
            caractere= ut.EnumCaracteres.CAVALO_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.CAVALO_PRETO,
            cor=cor
        ) 