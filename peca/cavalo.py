from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tabuleiro.tabuleiro import Tabuleiro

from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada

class Cavalo(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada, tabuleiro: Tabuleiro):
        super().__init__(
            caractere= ut.EnumCaracteres.CAVALO_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.CAVALO_PRETO,
            cor=cor,
            coordenada=coordenada_inicial,
            tabuleiro=tabuleiro
        ) 

    def atualizar_lista_de_possiveis_coordenadas(self):
        self.lista_de_posssiveis_movimentos = []
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna

        self.tentar_adicionar(linha_atual + 1, coluna_atual - 2)
        self.tentar_adicionar(linha_atual + 2, coluna_atual - 1)
        self.tentar_adicionar(linha_atual + 2, coluna_atual + 1)
        self.tentar_adicionar(linha_atual + 1, coluna_atual + 2)
        self.tentar_adicionar(linha_atual - 1, coluna_atual + 2)
        self.tentar_adicionar(linha_atual - 2, coluna_atual + 1)
        self.tentar_adicionar(linha_atual - 2, coluna_atual - 1)
        self.tentar_adicionar(linha_atual - 1, coluna_atual - 2)
