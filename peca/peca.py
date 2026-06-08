from abc import ABC
import utils.utils as ut

class Peca(ABC):
    def __init__(self, caractere: str):
        self.caractere = caractere


    @property
    def caractere(self):
        return self._caractere
    
    @caractere.setter
    def caractere(self, novo_caractere: str):
        if not ut.validar_string(novo_caractere):
            self._caractere = novo_caractere
    