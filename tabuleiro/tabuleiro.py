import utils.utils as ut
from peca.peca import Peca
from peca.peao import Peao
from peca.torre import Torre
from peca.cavalo import Cavalo
from peca.bispo import Bispo
from peca.rainha import Rainha
from peca.rei import Rei

from typing import Literal

class Tabueiro:
    def __init__(self):
        self.matriz_casas: list[list[str]] = self.gerar_matriz_tabuleiro()
        self.matriz_pecas: list[list[Peca | None]] = self.gerar_configuracao_inicial()

    def gerar_matriz_tabuleiro(self):
        """
        Retorna a disposição de casas do tabuleiro
        """
        return [
            ['/', '-', '/', '-', '/', '-', '/', '-'],
            ['-', '/', '-', '/', '-', '/', '-', '/'],
            ['/', '-', '/', '-', '/', '-', '/', '-'],
            ['-', '/', '-', '/', '-', '/', '-', '/'],
            ['/', '-', '/', '-', '/', '-', '/', '-'],
            ['-', '/', '-', '/', '-', '/', '-', '/'],
            ['/', '-', '/', '-', '/', '-', '/', '-'],
            ['-', '/', '-', '/', '-', '/', '-', '/']
        ]
            
    def gerar_configuracao_inicial(self):
        """
        Retorna a configuração inicial de peças do tabuleiro
        """
        return [
            [Torre(ut.EnumCor.PRETO), Cavalo(ut.EnumCor.PRETO), Bispo(ut.EnumCor.PRETO), Rainha(ut.EnumCor.PRETO), Rei(ut.EnumCor.PRETO), Bispo(ut.EnumCor.PRETO), Cavalo(ut.EnumCor.PRETO), Torre(ut.EnumCor.PRETO)],
            [Peao(ut.EnumCor.PRETO), Peao(ut.EnumCor.PRETO), Peao(ut.EnumCor.PRETO), Peao(ut.EnumCor.PRETO), Peao(ut.EnumCor.PRETO), Peao(ut.EnumCor.PRETO), Peao(ut.EnumCor.PRETO), Peao(ut.EnumCor.PRETO)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Peao(ut.EnumCor.BRANCO), Peao(ut.EnumCor.BRANCO), Peao(ut.EnumCor.BRANCO), Peao(ut.EnumCor.BRANCO), Peao(ut.EnumCor.BRANCO), Peao(ut.EnumCor.BRANCO), Peao(ut.EnumCor.BRANCO), Peao(ut.EnumCor.BRANCO)],
            [Torre(ut.EnumCor.BRANCO), Cavalo(ut.EnumCor.BRANCO), Bispo(ut.EnumCor.BRANCO), Rainha(ut.EnumCor.BRANCO), Rei(ut.EnumCor.BRANCO), Bispo(ut.EnumCor.BRANCO), Cavalo(ut.EnumCor.BRANCO), Torre(ut.EnumCor.BRANCO)]
        ]
    
    def gerar_string_tabuleiro(self, lado: ut.EnumCor) -> str:
        """
        Gera uma string com o tabuleiro em sua posição atual
        """
        def formatar_casa(caractere: str):
            """
            Retorna a string formatada para ser adicionada ao tabuleiro
            """
            return f"|{caractere} |"

        string_tabuleiro: str = ""

        for i in range(8):
            for j in range(8):
                if (self.matriz_pecas[i][j] is not None):
                    string_tabuleiro += formatar_casa(self.matriz_pecas[i][j].caractere.value)
                else:
                    string_tabuleiro += formatar_casa(self.matriz_casas[i][j])
            string_tabuleiro += "\n"

        return string_tabuleiro