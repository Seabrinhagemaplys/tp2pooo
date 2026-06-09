from tabuleiro.tabuleiro import Tabueiro

class Controladora:
    def __init__(self):
        self.jogo_em_andamento = True
        self.tabuleiro = Tabueiro()

    def mostrar_opcoes_de_jogo():
        pass

    def iniciar(self):
        while self.jogo_em_andamento:
            self.mostrar_opcoes_de_jogo()
            