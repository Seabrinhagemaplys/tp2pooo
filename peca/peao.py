from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada



class Peao(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada):
        self.ja_movimentou = False
        super().__init__(
            caractere= ut.EnumCaracteres.PEAO_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.PEAO_PRETO,
            cor=cor,
            coordenada=coordenada_inicial
        )
    
    def atualizar_lista_de_possiveis_coordenadas(self):
        match self.cor:
            case ut.EnumCor.BRANCO:
                self.atualizar_lista_de_possiveis_coordenadas_peao_branco()
            
            case ut.EnumCor.PRETO:
                self.atualizar_lista_de_possiveis_coordenadas_peao_preto()
            
            case _:
                pass

    def tentar_adicionar(self, linha: int, coluna: int):
        """
        Adiciona coordenada à lista somente se for válida no tabuleiro.
        """
        try:
            self.lista_de_posssiveis_movimentos.append(Coordenada(linha, coluna))
        except Exception as e:
            pass

    def atualizar_lista_de_possiveis_coordenadas_peao_branco(self):
        linha_atual = self.coordenada_atual.linha
        coluna_atual = self.coordenada_atual.coluna
        self.lista_de_posssiveis_movimentos = []

        self.tentar_adicionar(linha_atual - 1, coluna_atual)
        self.tentar_adicionar(linha_atual - 1, coluna_atual + 1)
        self.tentar_adicionar(linha_atual - 1, coluna_atual - 1)

        if not self.ja_movimentou:
            self.tentar_adicionar(linha_atual - 2, coluna_atual)

    def atualizar_lista_de_possiveis_coordenadas_peao_preto(self):
        linha_atual = self.coordenada_atual.linha
        coluna_atual = self.coordenada_atual.coluna

        self.lista_de_posssiveis_movimentos = [Coordenada(linha_atual + 1, coluna_atual)]
        
        if not self.ja_movimentou:
            self.lista_de_posssiveis_movimentos.append(Coordenada(linha_atual + 2, coluna_atual))