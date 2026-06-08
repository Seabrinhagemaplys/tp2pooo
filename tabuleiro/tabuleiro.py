import utils.utils as ut
from peca.peca import Peca

class Tabueiro:
    def __init__(self):
        self.matriz_casas: list[list[str]] = [
            (
                ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"] if n % 2 == 0 
                else ["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"]
            ) 
            for n in range(8)
        ]

        self.matriz_pecas: list[list[Peca]] = self.gerar_configuracao_inicial()

        for linha in self.matriz_casas:
            print(linha)

tb = Tabueiro()