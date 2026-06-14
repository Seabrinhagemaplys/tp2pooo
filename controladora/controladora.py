from tabuleiro.tabuleiro import Tabuleiro
from coordenada.coordenada import Coordenada
from peca.peca import Peca
from peca.peao import Peao
import utils.utils as ut

class Controladora:
    def __init__(self):
        self.jogo_em_andamento = True
        self.lado = ut.EnumCor.BRANCO
        self.tabuleiro = Tabuleiro()

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
            # for parte_da_entrada in lista_entrada:
            #     if not parte_da_entrada.isnumeric():
            #         return False
            #     if not int(parte_da_entrada) in range(1, 9):
            #         return False
                
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


    #
    # VALIDAR DEPENDE DE MUITA COISA PRECISAMOS INCREMENTAR
    #

    def validar_jogada(self, coordenada_origem: Coordenada, coordenada_destino: Coordenada):
        """
        Função que checa se uma jogada é válida ou não
        """
        
        peca_a_ser_movida: Peca | None = self.tabuleiro.get_peca_na_posicao(coordenada_origem)
        if peca_a_ser_movida is None:
            print("Não há peça nesse lugar")
            return False
        
        if not (peca_a_ser_movida.cor == self.lado):
            print(f"A cor da peça é {peca_a_ser_movida.cor} mas é a vez de {self.lado}")
            return False
        
        if not (coordenada_destino in peca_a_ser_movida.lista_de_posssiveis_movimentos):
            print("A coordenada de destino não está na lista de possíveis movimentos da peça")
            return False
        
        if (coordenada_origem == coordenada_destino):
            print("Não se pode mover uma peça para o mesmo lugar")
            return False
        
        # checagens exclusivas de peão
        # if isinstance(peca_a_ser_movida, Peao):
        #     pass
        
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
        while self.jogo_em_andamento:
            self.mostrar_tabuleiro()
            coordenada_origem, coordenada_destino = self.montar_jogada()
            self.tabuleiro.mover_peca(coordenada_origem, coordenada_destino)

            self.alterar_lado()
            