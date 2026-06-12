from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada


class Rainha(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada):
        super().__init__(
            caractere= ut.EnumCaracteres.RAINHA_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.RAINHA_PRETO,
            cor=cor,
            coordenada=coordenada_inicial
        ) 

    def atualizar_lista_de_possiveis_coordenadas(self):
        def calcular_diagonais(linha, coluna):
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

            adicionar_posicao_mais_mais(linha, coluna)
            adicionar_posicao_mais_menos(linha, coluna)
            adicionar_posicao_menos_mais(linha, coluna)
            adicionar_posicao_menos_menos(linha, coluna)
        
        def calcular_linha_e_coluna(linha, coluna):
            for i in range(0, 8):
                self.tentar_adicionar(i, coluna)

            for j in range(0, 8):
                self.tentar_adicionar(linha, j)
        self.lista_de_posssiveis_movimentos = []
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna

        calcular_diagonais(linha_atual, coluna_atual)
        calcular_linha_e_coluna(linha_atual, coluna_atual)