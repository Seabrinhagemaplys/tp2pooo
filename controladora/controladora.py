from tabuleiro.tabuleiro import Tabueiro
import utils.utils as ut

class Controladora:
    def __init__(self):
        self.jogo_em_andamento = True
        self.lado = ut.EnumCor.BRANCO
        self.tabuleiro = Tabueiro()

    def mostrar_tabuleiro(self):
        print(self.tabuleiro.gerar_string_tabuleiro())

    def mostrar_opcoes_de_jogo():
        pass

    def iniciar(self):
        while self.jogo_em_andamento:
            self.mostrar_tabuleiro()
            