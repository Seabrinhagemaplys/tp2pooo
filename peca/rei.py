from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tabuleiro.tabuleiro import Tabuleiro
from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada

class Rei(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada, tabuleiro: Tabuleiro):
        super().__init__(
            caractere= ut.EnumCaracteres.REI_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.REI_PRETO,
            cor=cor,
            coordenada=coordenada_inicial,
            tabuleiro=tabuleiro
        ) 

    def atualizar_lista_de_possiveis_coordenadas(self):
        self.lista_de_posssiveis_movimentos = []
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna

        for i in range(-1, 2):
            for j in range(-1, 2):
                self.tentar_adicionar(linha_atual + i, coluna_atual + j)