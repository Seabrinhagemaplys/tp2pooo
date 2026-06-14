from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tabuleiro.tabuleiro import Tabuleiro
from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada


class Rainha(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada, tabuleiro: Tabuleiro):
        super().__init__(
            caractere= ut.EnumCaracteres.RAINHA_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.RAINHA_PRETO,
            cor=cor,
            coordenada=coordenada_inicial,
            tabuleiro=tabuleiro
        )
    

    def atualizar_lista_de_possiveis_coordenadas(self):
        def dentro_do_tabuleiro(linha: int, coluna: int):
                """
                Função helper que checa se um part linha e coluna está dentro do tabuleiro
                """
                if ((linha < 0) or (coluna < 0)):
                    return False
                if ((linha > 7) or (coluna > 7)):
                    return False
                
                return True
        def calcular_diagonais(linha, coluna):
            def adicionar_posicao_mais_mais(linha: int, coluna: int):
                """
                Função helper que adiciona todas as coordenadas possíveis na diagonal +/+ utilizando recursividade
                """
                if not dentro_do_tabuleiro(linha, coluna):
                    return

                peca_na_posicao = self.tabuleiro.get_peca_na_posicao(Coordenada(linha, coluna))

                if peca_na_posicao is not None:
                    if peca_na_posicao.cor == self.cor:
                        return
                    else:
                        self.tentar_adicionar(linha, coluna)
                        return

                self.tentar_adicionar(linha, coluna)
                adicionar_posicao_mais_mais(linha + 1, coluna + 1)

            def adicionar_posicao_mais_menos(linha: int, coluna: int):
                """
                Função helper que adiciona todas as coordenadas possíveis na diagonal +/- utilizando recursividade
                """
                if not dentro_do_tabuleiro(linha, coluna):
                    return

                peca_na_posicao = self.tabuleiro.get_peca_na_posicao(Coordenada(linha, coluna))

                if peca_na_posicao is not None:
                    if peca_na_posicao.cor == self.cor:
                        return
                    else:
                        self.tentar_adicionar(linha, coluna)
                        return

                self.tentar_adicionar(linha, coluna)
                adicionar_posicao_mais_menos(linha + 1, coluna - 1)

            def adicionar_posicao_menos_mais(linha: int, coluna: int):
                """
                Função helper que adiciona todas as coordenadas possíveis na diagonal -/+ utilizando recursividade
                """
                if not dentro_do_tabuleiro(linha, coluna):
                    return

                peca_na_posicao = self.tabuleiro.get_peca_na_posicao(Coordenada(linha, coluna))

                if peca_na_posicao is not None:
                    if peca_na_posicao.cor == self.cor:
                        return
                    else:
                        self.tentar_adicionar(linha, coluna)
                        return

                self.tentar_adicionar(linha, coluna)
                adicionar_posicao_menos_mais(linha - 1, coluna + 1)

            def adicionar_posicao_menos_menos(linha: int, coluna: int):
                """
                Função helper que adiciona todas as coordenadas possíveis na diagonal -/- utilizando recursividade
                """
                if not dentro_do_tabuleiro(linha, coluna):
                    return

                peca_na_posicao = self.tabuleiro.get_peca_na_posicao(Coordenada(linha, coluna))

                if peca_na_posicao is not None:
                    if peca_na_posicao.cor == self.cor:
                        return
                    else:
                        self.tentar_adicionar(linha, coluna)
                        return

                self.tentar_adicionar(linha, coluna)
                adicionar_posicao_menos_menos(linha - 1, coluna - 1)

            adicionar_posicao_mais_mais(linha_atual + 1, coluna_atual + 1)
            adicionar_posicao_mais_menos(linha_atual + 1, coluna_atual - 1)
            adicionar_posicao_menos_mais(linha_atual - 1, coluna_atual + 1)
            adicionar_posicao_menos_menos(linha_atual - 1, coluna_atual - 1)
        
        def calcular_linha_e_coluna(linha, coluna):
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
        self.lista_de_posssiveis_movimentos = []
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna

        calcular_diagonais(linha_atual, coluna_atual)
        calcular_linha_e_coluna(linha_atual, coluna_atual)