from abc import ABC
import utils.utils as ut

class Peca(ABC):
    def __init__(self, caractere: ut.EnumCaracteres, cor: ut.EnumCor):
        self._caractere = caractere
        self._cor = cor


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