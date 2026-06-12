from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada

class Bispo(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada ):
        super().__init__(
            caractere= ut.EnumCaracteres.BISPO_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.BISPO_PRETO,
            cor=cor,
            coordenada=coordenada_inicial
        ) 

    def atualizar_lista_de_possiveis_coordenadas(self):
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

        def adicionar_posicao_mais_mais(linha: int, coluna: int):
            """
            Função helper que adiciona todas as coordenadas possíveis na diagonal +/+ utilizando recursividade
            """
            if not dentro_do_tabuleiro(linha, coluna):
                return

            adicionar_posicao_mais_mais(linha + 1, coluna + 1)
            self.tentar_adicionar(linha, coluna)

        def adicionar_posicao_mais_menos(linha: int, coluna: int):
            """
            Função helper que adiciona todas as coordenadas possíveis na diagonal +/- utilizando recursividade
            """
            if not dentro_do_tabuleiro(linha, coluna):
                return

            adicionar_posicao_mais_menos(linha + 1, coluna - 1)
            self.tentar_adicionar(linha, coluna)

        def adicionar_posicao_menos_mais(linha: int, coluna: int):
            """
            Função helper que adiciona todas as coordenadas possíveis na diagonal -/+ utilizando recursividade
            """
            if not dentro_do_tabuleiro(linha, coluna):
                return

            adicionar_posicao_menos_mais(linha - 1, coluna + 1)
            self.tentar_adicionar(linha, coluna)

        def adicionar_posicao_menos_menos(linha: int, coluna: int):
            """
            Função helper que adiciona todas as coordenadas possíveis na diagonal -/- utilizando recursividade
            """
            if not dentro_do_tabuleiro(linha, coluna):
                return

            adicionar_posicao_menos_menos(linha - 1, coluna - 1)
            self.tentar_adicionar(linha, coluna)

        adicionar_posicao_mais_mais(linha_atual, coluna_atual)
        adicionar_posicao_mais_menos(linha_atual, coluna_atual)
        adicionar_posicao_menos_mais(linha_atual, coluna_atual)
        adicionar_posicao_menos_menos(linha_atual, coluna_atual)
            