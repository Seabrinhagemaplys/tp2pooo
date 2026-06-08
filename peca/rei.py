from peca.peca import Peca
import utils.utils as ut

class Rei(Peca):
    def __init__(self, cor: ut.EnumCor):
        super().__init__(
            caractere= ut.EnumCaracteres.REI_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.REI_PRETO,
            cor=cor
        ) 