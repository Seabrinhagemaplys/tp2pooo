from tabuleiro.tabuleiro import Tabueiro
from coordenada.coordenada import Coordenada
import utils.utils as ut

class Controladora:
    def __init__(self):
        self.jogo_em_andamento = True
        self.lado = ut.EnumCor.BRANCO
        self.tabuleiro = Tabueiro()

    def mostrar_tabuleiro(self):
        """
        Imprime o tabuleiro no terminal com base no lado que deve jogar
        """
        print(self.tabuleiro.gerar_string_tabuleiro(self.lado))

    def coletar_entradas(self, string: str):
        """
        Pergunta ao jogador o que deve fazer 
        """
        def entrada_valida(entrada: str):
            """
            Valida a entrada do jogador
            """
            lista_entrada: list[str] = entrada.split(" ")
            if not ut.validar_string(entrada):
                return False
            if len(lista_entrada) != 2:
                return False
            for parte_da_entrada in lista_entrada:
                if not parte_da_entrada.isnumeric():
                    return False
                if not int(parte_da_entrada) in range(1, 9):
                    return False
                
            return True
            
        entrada: str = ""
        
        while not entrada_valida(entrada):
            entrada = input(string)

        return int(entrada.split(" ")[0]) - 1, int(entrada.split(" ")[1]) - 1

    def alterar_lado(self):
        """
        Troca o lado que está jogando
        """
        match (self.lado):
            case ut.EnumCor.BRANCO:
                self.lado = ut.EnumCor.PRETO

            case ut.EnumCor.PRETO:
                self.lado = ut.EnumCor.BRANCO

            case _:
                pass

    def validar_jogada(self, coordenada_origem: Coordenada, coordenada_destino: Coordenada):
        if not self.tabuleiro.posicao_esta_ocupada(coordenada_origem):
            return False
        
        if not (self.tabuleiro.get_peca_na_posicao(coordenada_origem).cor == self.lado):
            return False
        
        return True

    def montar_jogada(self):
        repetir = True

        while repetir:
            linha_inicial, coluna_inicial = self.coletar_entradas("Insira as coordenadas da peça que quer mover (formato: '[linha] [coluna]', onde linha e coluna são números, de 1 a 8): ")
            linha_final, coluna_final = self.coletar_entradas("Insira as coordenadas de onde você quer mover a peça (formato: '[linha] [coluna]', onde linha e coluna são números, de 1 a 8): ")
            try:
                coordenada_origem: Coordenada = Coordenada(linha_inicial, coluna_inicial)
                coordenada_destino: Coordenada = Coordenada(linha_final, coluna_final)
                if (self.validar_jogada(coordenada_origem, coordenada_destino)):
                    repetir = False
            except Exception as e:
                pass

        return coordenada_origem, coordenada_destino


    def iniciar(self):
        """
        Inicia o loop de jogo
        """
        contador: int = 0

        while self.jogo_em_andamento:
            self.mostrar_tabuleiro()
            coordenada_origem, coordenada_destino = self.montar_jogada()
            self.tabuleiro.mover_peca(coordenada_origem, coordenada_destino)

            self.alterar_lado()
            