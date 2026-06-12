import utils.utils as ut
from peca.peca import Peca
from peca.peao import Peao
from peca.torre import Torre
from peca.cavalo import Cavalo
from peca.bispo import Bispo
from peca.rainha import Rainha
from peca.rei import Rei
from coordenada.coordenada import Coordenada

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
            [Torre(ut.EnumCor.PRETO, Coordenada(0, 0)), Cavalo(ut.EnumCor.PRETO, Coordenada(0, 1)), Bispo(ut.EnumCor.PRETO, Coordenada(0, 2)), Rainha(ut.EnumCor.PRETO, Coordenada(0, 3)), Rei(ut.EnumCor.PRETO, Coordenada(0, 4)), Bispo(ut.EnumCor.PRETO, Coordenada(0, 5)), Cavalo(ut.EnumCor.PRETO, Coordenada(0, 6)), Torre(ut.EnumCor.PRETO, Coordenada(0, 7))],
            [Peao(ut.EnumCor.PRETO, Coordenada(1, 0)), Peao(ut.EnumCor.PRETO, Coordenada(1, 1)), Peao(ut.EnumCor.PRETO, Coordenada(1, 2)), Peao(ut.EnumCor.PRETO, Coordenada(1, 3)), Peao(ut.EnumCor.PRETO, Coordenada(1, 4)), Peao(ut.EnumCor.PRETO, Coordenada(1, 5)), Peao(ut.EnumCor.PRETO, Coordenada(1, 6)), Peao(ut.EnumCor.PRETO, Coordenada(1, 7))],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Peao(ut.EnumCor.BRANCO, Coordenada(6, 0)), Peao(ut.EnumCor.BRANCO, Coordenada(6, 1)), Peao(ut.EnumCor.BRANCO, Coordenada(6, 2)), Peao(ut.EnumCor.BRANCO, Coordenada(6, 3)), Peao(ut.EnumCor.BRANCO, Coordenada(6, 4)), Peao(ut.EnumCor.BRANCO, Coordenada(6, 5)), Peao(ut.EnumCor.BRANCO, Coordenada(6, 6)), Peao(ut.EnumCor.BRANCO, Coordenada(6, 7))],
            [Torre(ut.EnumCor.BRANCO, Coordenada(7, 0)), Cavalo(ut.EnumCor.BRANCO, Coordenada(7, 1)), Bispo(ut.EnumCor.BRANCO, Coordenada(7, 2)), Rainha(ut.EnumCor.BRANCO, Coordenada(7, 3)), Rei(ut.EnumCor.BRANCO, Coordenada(7, 4)), Bispo(ut.EnumCor.BRANCO, Coordenada(7, 5)), Cavalo(ut.EnumCor.BRANCO, Coordenada(7, 6)), Torre(ut.EnumCor.BRANCO, Coordenada(7, 7))]
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
        inicio: int = 0 if lado == ut.EnumCor.BRANCO else 7
        fim: int = 8 if lado == ut.EnumCor.BRANCO else -1
        passo: int = 1 if lado == ut.EnumCor.BRANCO else -1

        for i in range(inicio, fim, passo):
            for j in range(inicio, fim, passo):
                if (self.matriz_pecas[i][j] is not None):
                    string_tabuleiro += formatar_casa(self.matriz_pecas[i][j].caractere.value)
                else:
                    string_tabuleiro += formatar_casa(self.matriz_casas[i][j])
            string_tabuleiro += "\n"

        return string_tabuleiro
    
    def get_peca_na_posicao(self, coordenada: Coordenada) -> Peca:
        """
        Retorna a peça que está em uma coordenada e lança uma exceção do tipo ValueError caso não haja peça na coordenada passada
        """
        if not self.posicao_esta_ocupada(coordenada):
            raise ValueError("Não há peça na posição")
        
        return self.matriz_pecas[coordenada.linha][coordenada.coluna] 
    
    def posicao_esta_ocupada(self, coordenada: Coordenada) -> bool:
        """
        Verifica se uma casa no tabuleiro está ocupada por uma peça
        """
        if self.matriz_pecas[coordenada.linha][coordenada.coluna] is not None:
            return True
        
        return False
    
    def mover_peca(self, coordenada_origem: Coordenada, coordenada_destino: Coordenada) -> Peca | None:
        """
        Move uma peça no tabuleiro e retorna a peça comida, caso haja e None caso contrário
        """
        if self.matriz_pecas[coordenada_origem.linha][coordenada_origem.coluna] is None:
            raise ValueError("Não se pode mexer nada")

        peca_movida = self.matriz_pecas[coordenada_origem.linha][coordenada_origem.coluna]
        peca_tomada = None if self.matriz_pecas[coordenada_destino.linha][coordenada_destino.coluna] is None else self.matriz_pecas[coordenada_destino.linha][coordenada_destino.coluna]

        self.matriz_pecas[coordenada_origem.linha][coordenada_origem.coluna] = None
        self.matriz_pecas[coordenada_destino.linha][coordenada_destino.coluna] = peca_movida

        return peca_tomada
