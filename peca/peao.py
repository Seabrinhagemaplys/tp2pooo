from peca.peca import Peca
import utils.utils as ut


class Peao(Peca):
    def __init__(self, cor: ut.EnumCor):
        super().__init__(
            caractere= ut.EnumCaracteres.PEAO_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.PEAO_BRANCO,
            cor=cor
        ) 
