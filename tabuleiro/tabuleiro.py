import utils.utils as ut
from peca.peca import Peca

class Tabueiro:
    def __init__(self):
        self.matriz_casas: list[list[str]] = self.gerar_matriz_tabuleiro()

        ##self.matriz_pecas: list[list[Peca]] = self.gerar_configuracao_inicial()

        for linha in self.matriz_casas:
            print(linha)

    def gerar_matriz_tabuleiro(self):

        matriz_tabuleiro = [['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
                            ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
                            ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
                            ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
                            ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
                            ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],
                            ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],
                            ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜']]
        
        return matriz_tabuleiro

tb = Tabueiro()
