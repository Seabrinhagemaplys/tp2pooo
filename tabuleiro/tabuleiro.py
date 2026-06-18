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

class Tabuleiro:
    def __init__(self):
        self.matriz_casas: list[list[str]] = self.gerar_matriz_tabuleiro()
        self.matriz_pecas: list[list[Peca | None]] = self.gerar_configuracao_inicial()

        for i in range(8):
            for j in range(8):
                if self.matriz_pecas[i][j] is not None:
                    self.matriz_pecas[i][j].atualizar_lista_de_possiveis_coordenadas()

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
            [Torre(ut.EnumCor.PRETO, Coordenada(0, 0), self), Cavalo(ut.EnumCor.PRETO, Coordenada(0, 1), self), Bispo(ut.EnumCor.PRETO, Coordenada(0, 2), self), Rainha(ut.EnumCor.PRETO, Coordenada(0, 3), self), Rei(ut.EnumCor.PRETO, Coordenada(0, 4), self), Bispo(ut.EnumCor.PRETO, Coordenada(0, 5), self), Cavalo(ut.EnumCor.PRETO, Coordenada(0, 6), self), Torre(ut.EnumCor.PRETO, Coordenada(0, 7), self)],
            [Peao(ut.EnumCor.PRETO, Coordenada(1, 0), self), Peao(ut.EnumCor.PRETO, Coordenada(1, 1), self), Peao(ut.EnumCor.PRETO, Coordenada(1, 2), self), Peao(ut.EnumCor.PRETO, Coordenada(1, 3), self), Peao(ut.EnumCor.PRETO, Coordenada(1, 4), self), Peao(ut.EnumCor.PRETO, Coordenada(1, 5), self), Peao(ut.EnumCor.PRETO, Coordenada(1, 6), self), Peao(ut.EnumCor.PRETO, Coordenada(1, 7), self)],
            
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            
            [Peao(ut.EnumCor.BRANCO, Coordenada(6, 0), self), Peao(ut.EnumCor.BRANCO, Coordenada(6, 1), self), Peao(ut.EnumCor.BRANCO, Coordenada(6, 2), self), Peao(ut.EnumCor.BRANCO, Coordenada(6, 3), self), Peao(ut.EnumCor.BRANCO, Coordenada(6, 4), self), Peao(ut.EnumCor.BRANCO, Coordenada(6, 5), self), Peao(ut.EnumCor.BRANCO, Coordenada(6, 6), self), Peao(ut.EnumCor.BRANCO, Coordenada(6, 7), self)],
            [Torre(ut.EnumCor.BRANCO, Coordenada(7, 0), self), Cavalo(ut.EnumCor.BRANCO, Coordenada(7, 1), self), Bispo(ut.EnumCor.BRANCO, Coordenada(7, 2), self), Rainha(ut.EnumCor.BRANCO, Coordenada(7, 3), self), Rei(ut.EnumCor.BRANCO, Coordenada(7, 4), self), Bispo(ut.EnumCor.BRANCO, Coordenada(7, 5), self), Cavalo(ut.EnumCor.BRANCO, Coordenada(7, 6), self), Torre(ut.EnumCor.BRANCO, Coordenada(7, 7), self)]
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
            if i == inicio:
                string_tabuleiro += formatar_casa(" ")
                string_tabuleiro += "".join([formatar_casa(char) for char in range(inicio + 1, fim + 1, passo)])
                string_tabuleiro += '\n'
            for j in range(inicio, fim, passo):
                if j == inicio:
                    string_tabuleiro += formatar_casa(i + 1)
                if (self.matriz_pecas[i][j] is not None):
                    string_tabuleiro += formatar_casa(self.matriz_pecas[i][j].caractere.value)
                else:
                    string_tabuleiro += formatar_casa(self.matriz_casas[i][j])
            string_tabuleiro += "\n"

        return string_tabuleiro
    
    def get_peca_na_posicao(self, coordenada: Coordenada) -> Peca | None:
        """
        Retorna a peça que está em uma coordenada ou None
        """
        return self.matriz_pecas[coordenada.linha][coordenada.coluna] 
    
    def mover_peca(self, coordenada_origem: Coordenada, coordenada_destino: Coordenada, simulacao: bool = False) -> Peca | None:
        if self.matriz_pecas[coordenada_origem.linha][coordenada_origem.coluna] is None:
            raise ValueError("Não se pode mexer nada")

        peca_movida = self.matriz_pecas[coordenada_origem.linha][coordenada_origem.coluna]
        peca_tomada = self.matriz_pecas[coordenada_destino.linha][coordenada_destino.coluna]

        self.matriz_pecas[coordenada_origem.linha][coordenada_origem.coluna] = None
        self.matriz_pecas[coordenada_destino.linha][coordenada_destino.coluna] = peca_movida

        peca_movida.coordenada_atual = coordenada_destino

        self.atualizar_todas_as_listas()

        if isinstance(peca_movida, Peao):
            peca_movida.atualizar_lista_de_coordenadas_para_tomada()
            
            if not simulacao:
                peca_movida.ja_movimentou = True

        if isinstance(peca_movida, Peao):
                peca_movida.ja_movimentou = True

        if isinstance(peca_movida, Rei):
            peca_movida.ja_movimentou = True

        return peca_tomada
    
    def voltar_movimento(self, coordenada_origem: Coordenada, coordenada_destino: Coordenada, peca_tomada: Peca | None):
        peca_movimentada = self.get_peca_na_posicao(coordenada_destino)

        self.matriz_pecas[coordenada_destino.linha][coordenada_destino.coluna] = peca_tomada
        self.matriz_pecas[coordenada_origem.linha][coordenada_origem.coluna] = peca_movimentada

        if peca_movimentada is not None:
            peca_movimentada.coordenada_atual = coordenada_origem

        self.atualizar_todas_as_listas()

    def atualizar_todas_as_listas(self):
        for i in range(8):
            for j in range(8):
                peca = self.matriz_pecas[i][j]
                if peca is not None:
                    peca.lista_de_posssiveis_movimentos.clear()
                    peca.atualizar_lista_de_possiveis_coordenadas()

    def get_rei(self, cor: ut.EnumCor) -> Rei:
        """
        Retorna um rei de uma cor
        """
        for i in range(8):
            for j in range(8):
                peca = self.get_peca_na_posicao(Coordenada(i, j))
                if isinstance(peca, Rei) and peca.cor == cor:
                    return peca
                
    def get_rei_preto(self) -> Rei:
        """
        Retorna a instância de rei preto no tabuleiro
        """
        return self.get_rei(ut.EnumCor.PRETO)

    def get_rei_branco(self) -> Rei:
        """
        Retorna a instância de rei branco no tabuleiro
        """
        return self.get_rei(ut.EnumCor.BRANCO)
                
    def get_pecas_de_uma_cor(self, cor: ut.EnumCor):
        lista_de_pecas: list[Peca] = []
        
        for i in range(8):
            for j in range(8):
                possivel_peca: Peca | None = self.get_peca_na_posicao(Coordenada(i, j))

                if possivel_peca is None:
                    continue

                if possivel_peca.cor != cor:
                    continue

                lista_de_pecas.append(possivel_peca)

        return lista_de_pecas
    
    def promocao(self, peca_a_trocar: Peao):
        print("Digite 1 para Promoção à Rainha")
        print("Digite 2 para Promoção à Torre")
        print("Digite 3 para Promoção à Bispo")
        print("Digite 4 para promoção ao Cavalo")

        coordenada_da_peca: Coordenada = peca_a_trocar.coordenada_atual
        cor_da_peca: ut.EnumCor = peca_a_trocar.cor

        entrada = int(input("Insira aqui:"))

        match (entrada):
            case 1:
                nova_peca = Rainha(cor_da_peca, coordenada_da_peca, self)
            case 2:
                nova_peca = Torre(cor_da_peca, coordenada_da_peca, self)
            case 3: 
                nova_peca = Bispo(cor_da_peca, coordenada_da_peca, self)
            case 4:
                nova_peca = Cavalo(cor_da_peca, coordenada_da_peca, self)
            case _:
                pass

        self.matriz_pecas[coordenada_da_peca.linha][coordenada_da_peca.coluna] = nova_peca
        self.atualizar_todas_as_listas()


    def roque(self, peca_torre: Peao, peca_rei: Rei):
        if not(peca_rei.ja_movimentou) and not(peca_torre.ja_movimentou):
            pass
