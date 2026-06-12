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
        self.lista_de_posssiveis_movimentos = []
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna
        
        for i in range(0, 8):
            self.tentar_adicionar(i, coluna_atual)

        for j in range(0, 8):
            self.tentar_adicionar(linha_atual, j)
