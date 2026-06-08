import utils.utils as ut

class Coordenada:
    def __init__(self, linha: int, coluna: int):
        self.linha = linha
        self.coluna = coluna

    @property
    def linha(self):
        return self.__linha
    
    @linha.setter
    def linha(self, nova_linha: int):
        if not ut.checar_instancia_int(nova_linha):
            raise TypeError("Não é um número inteiro!")
        if nova_linha not in range(0, 8):
            raise ValueError("Número fora do tabuleiro!")
        
        self.__linha = nova_linha

    @property
    def coluna(self):
        return self.__coluna
    
    @coluna.setter
    def coluna(self, nova_coluna: int):
        if not ut.checar_instancia_int(nova_coluna):
            raise TypeError("Não é um número inteiro!")
        if nova_coluna not in range(0, 8):
            raise ValueError("Número fora do tabuleiro!")
        
        self.__coluna = nova_coluna
    
    
