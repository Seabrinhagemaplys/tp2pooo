from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tabuleiro.tabuleiro import Tabuleiro
from abc import ABC, abstractmethod
import utils.utils as ut
from coordenada.coordenada import Coordenada

class Peca(ABC):
    def __init__(self, caractere: ut.EnumCaracteres, cor: ut.EnumCor, coordenada: Coordenada, tabuleiro: Tabuleiro):
        self._caractere = caractere
        self._cor = cor
        self._coordenada_atual = coordenada
        self.tabuleiro = tabuleiro

        self.lista_de_posssiveis_movimentos: list[Coordenada] = []

    # PROPRIEDADES

    @property
    def caractere(self):
        return self._caractere
    
    @caractere.setter
    def caractere(self, novo_caractere: ut.EnumCaracteres):
        self._caractere = novo_caractere
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, nova_cor: ut.EnumCor):
        if not isinstance(nova_cor, ut.EnumCor):
            raise TypeError("Tipo invalido para cor!")

        self._cor = nova_cor 

    @property
    def coordenada_atual(self):
        return self._coordenada_atual
    
    @coordenada_atual.setter
    def coordenada_atual(self, nova_coordenada: Coordenada):
        if not isinstance (nova_coordenada, Coordenada):
            raise TypeError("Nao é uma coordenada!")
        
        self._coordenada_atual = nova_coordenada
        
    #METODOS

    def tentar_adicionar(self, linha: int, coluna: int):
        """
        Adiciona coordenada à lista somente se for válida no tabuleiro.
        """
        try:
            coordenada = Coordenada(linha, coluna)
            peca_na_casa = self.tabuleiro.get_peca_na_posicao(coordenada)

            if (
                coordenada not in self.lista_de_posssiveis_movimentos
                and coordenada != self.coordenada_atual
                and (peca_na_casa is None or peca_na_casa.cor != self.cor)
            ):
                self.lista_de_posssiveis_movimentos.append(coordenada)
        except Exception as e:
            pass

    @abstractmethod
    def atualizar_lista_de_possiveis_coordenadas(self):
        pass