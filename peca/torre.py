from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tabuleiro.tabuleiro import Tabuleiro
from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada


class Torre(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada, tabuleiro: Tabuleiro):
        super().__init__(
            caractere= ut.EnumCaracteres.TORRE_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.TORRE_PRETO,
            cor=cor,
            coordenada=coordenada_inicial,
            tabuleiro=tabuleiro
        ) 

    def atualizar_lista_de_possiveis_coordenadas(self):
        self.lista_de_posssiveis_movimentos = []
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna

        def dentro_do_tabuleiro(linha: int, coluna: int):
            """
            Função helper que checa se um part linha e coluna está dentro do tabuleiro
            """
            if ((linha < 0) or (coluna < 0)):
                return False
            if ((linha > 7) or (coluna > 7)):
                return False
            
            return True

        def procurar_linha_esquerda(linha: int, coluna: int):
            if not dentro_do_tabuleiro(linha, coluna):
                return
            
            peca_na_posicao = self.tabuleiro.get_peca_na_posicao(Coordenada(linha, coluna))
            if (peca_na_posicao is not None):
                if peca_na_posicao.cor == self.cor:
                    return
                else:
                    self.tentar_adicionar(linha, coluna)
                    return

            self.tentar_adicionar(linha, coluna)
            procurar_linha_esquerda(linha, coluna - 1)

        def procurar_linha_direita(linha: int, coluna: int):
            if not dentro_do_tabuleiro(linha, coluna):
                return
            
            peca_na_posicao = self.tabuleiro.get_peca_na_posicao(Coordenada(linha, coluna))
            if (peca_na_posicao is not None):
                if peca_na_posicao.cor == self.cor:
                    return
                else:
                    self.tentar_adicionar(linha, coluna)
                    return

            self.tentar_adicionar(linha, coluna)
            procurar_linha_direita(linha, coluna + 1)

        def procurar_coluna_acima(linha: int, coluna: int):
            if not dentro_do_tabuleiro(linha, coluna):
                return
            
            peca_na_posicao = self.tabuleiro.get_peca_na_posicao(Coordenada(linha, coluna))
            if (peca_na_posicao is not None):
                if peca_na_posicao.cor == self.cor:
                    return
                else:
                    self.tentar_adicionar(linha, coluna)
                    return

            self.tentar_adicionar(linha, coluna)
            procurar_coluna_acima(linha -1, coluna)
        
        def procurar_coluna_abaixo(linha: int, coluna: int):
            if not dentro_do_tabuleiro(linha, coluna):
                return
            
            peca_na_posicao = self.tabuleiro.get_peca_na_posicao(Coordenada(linha, coluna))
            if (peca_na_posicao is not None):
                if peca_na_posicao.cor == self.cor:
                    return
                else:
                    self.tentar_adicionar(linha, coluna)
                    return

            self.tentar_adicionar(linha, coluna)
            procurar_coluna_abaixo(linha + 1, coluna)

        procurar_linha_esquerda(linha_atual, coluna_atual - 1)
        procurar_linha_direita(linha_atual, coluna_atual + 1)
        procurar_coluna_acima(linha_atual - 1, coluna_atual)
        procurar_coluna_abaixo(linha_atual + 1, coluna_atual)