from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tabuleiro.tabuleiro import Tabuleiro
from peca.peca import Peca
import utils.utils as ut
from coordenada.coordenada import Coordenada

class Peao(Peca):
    def __init__(self, cor: ut.EnumCor, coordenada_inicial: Coordenada, tabuleiro: Tabuleiro):
        self.ja_movimentou = False
        self.movimentos_para_tomadas: list[Coordenada] = []
        super().__init__(
            caractere= ut.EnumCaracteres.PEAO_BRANCO if cor == ut.EnumCor.BRANCO else ut.EnumCaracteres.PEAO_PRETO,
            cor=cor,
            coordenada=coordenada_inicial,
            tabuleiro=tabuleiro
        )

    def tentar_adicionar(self, linha: int, coluna: int):
        # Tem que ser sobrecarregado pois como o peão não pode tomar em casas frontais, 
        # a útlima condição é levemente diferente, sendo (peca_na_casa is None) e não (peca_na_casa is None or peca_na_casa.cor != self.cor)
        try:
            coordenada = Coordenada(linha, coluna)
            peca_na_casa = self.tabuleiro.get_peca_na_posicao(coordenada)

            if (
                coordenada not in self.lista_de_posssiveis_movimentos
                and coordenada != self.coordenada_atual
                and (peca_na_casa is None)
            ):
                self.lista_de_posssiveis_movimentos.append(coordenada)
        except Exception as e:
            pass
    
    def atualizar_lista_de_possiveis_coordenadas(self):
        self.lista_de_posssiveis_movimentos = []
        match self.cor:
            case ut.EnumCor.BRANCO:
                self.atualizar_lista_de_possiveis_coordenadas_peao_branco()
            
            case ut.EnumCor.PRETO:
                self.atualizar_lista_de_possiveis_coordenadas_peao_preto()
            
            case _:
                pass

    def atualizar_lista_de_possiveis_coordenadas_peao_branco(self):
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna

        self.tentar_adicionar(linha_atual - 1, coluna_atual)
        if not self.ja_movimentou:
            self.tentar_adicionar(linha_atual - 2, coluna_atual)

    def atualizar_lista_de_possiveis_coordenadas_peao_preto(self):
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna

        self.tentar_adicionar(linha_atual + 1, coluna_atual)
        if not self.ja_movimentou:
            self.tentar_adicionar(linha_atual + 2, coluna_atual)

    def atualizar_lista_de_coordenadas_para_tomada(self):
        self.movimentos_para_tomadas = []
        linha_atual: int = self.coordenada_atual.linha
        coluna_atual: int = self.coordenada_atual.coluna

        match self.cor:
            case ut.EnumCor.BRANCO:
                self.atualizar_lista_de_coordenadas_para_tomada_branca(linha_atual, coluna_atual)
            
            case ut.EnumCor.PRETO:
                self.atualizar_lista_de_coordenadas_para_tomada_preto(linha_atual, coluna_atual)
            
            case _:
                pass

    def tentar_adicionar_tomada(self, linha, coluna):
        """
        Adiciona coordenada à lista somente se for válida no tabuleiro, específico para tomadas do peão
        """
        try:
            coordenada = Coordenada(linha, coluna)
            peca_na_casa = self.tabuleiro.get_peca_na_posicao(coordenada)

            if (
                coordenada not in self.movimentos_para_tomadas
                and coordenada != self.coordenada_atual
                and (peca_na_casa is not None and peca_na_casa.cor != self.cor)
            ):
                self.movimentos_para_tomadas.append(coordenada)
        except Exception as e:
            pass

    def atualizar_lista_de_coordenadas_para_tomada_branca(self, linha_atual: int, coluna_atual: int):
        self.tentar_adicionar_tomada(linha_atual - 1, coluna_atual - 1)
        self.tentar_adicionar_tomada(linha_atual - 1, coluna_atual + 1)

    def atualizar_lista_de_coordenadas_para_tomada_preto(self, linha_atual: int, coluna_atual: int):
        self.tentar_adicionar_tomada(linha_atual + 1, coluna_atual - 1)
        self.tentar_adicionar_tomada(linha_atual + 1, coluna_atual + 1)    