from abc import ABC, abstractmethod
import utils.utils as ut
from coordenada.coordenada import Coordenada

class Peca(ABC):
    def __init__(self, caractere: ut.EnumCaracteres, cor: ut.EnumCor, coordenada: Coordenada):
        self._caractere = caractere
        self._cor = cor
        self._coordenada_atual = coordenada

        self.lista_de_posssiveis_movimentos: list[Coordenada]
        self.atualizar_lista_de_possiveis_coordenadas()

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

    @abstractmethod
    def atualizar_lista_de_possiveis_coordenadas(self):
        pass