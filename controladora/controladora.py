from tabuleiro.tabuleiro import Tabuleiro
from coordenada.coordenada import Coordenada
from peca.peca import Peca
from peca.peao import Peao
import utils.utils as ut
from peca.rei import Rei

class Controladora:
    def __init__(self):
        self.jogo_em_andamento = True
        self.lado = ut.EnumCor.BRANCO
        self.tabuleiro = Tabuleiro()
        self.cheque: bool = False
        self.peca_dando_cheque: None | Peca = None
        self.ganhador: ut.EnumCor | None = None

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
        """
        Função que checa se uma jogada é válida ou não
        """
        peca_no_destino = self.tabuleiro.get_peca_na_posicao(coordenada_destino)
        
        peca_a_ser_movida: Peca | None = self.tabuleiro.get_peca_na_posicao(coordenada_origem)
        if peca_a_ser_movida is None:
            print("Não há peça nesse lugar")
            return False            
        
        if peca_no_destino is not None and isinstance(peca_no_destino, Rei):
            print("Impossível tomar! É um rei!")
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
        
        peca_tomada = self.tabuleiro.mover_peca(coordenada_origem, coordenada_destino, simulacao=True)
        meu_rei_em_cheque = self.rei_em_cheque(self.lado)
        self.tabuleiro.voltar_movimento(coordenada_origem, coordenada_destino, peca_tomada)

        if meu_rei_em_cheque:
            print("Essa jogada deixa seu rei em cheque")
            return False
        
        # checagens exclusivas de peão
        # if isinstance(peca_a_ser_movida, Peao):
        #     pass
        
        return True

    def montar_jogada(self):
        """
        Monta uma jogada válida para jogo
        """
        repetir = True

        while repetir:
            try:
                linha_inicial, coluna_inicial = self.coletar_entradas("Insira as coordenadas da peça que quer mover (formato: '[linha] [coluna]', onde linha e coluna são números, de 1 a 8): ")
                linha_final, coluna_final = self.coletar_entradas("Insira as coordenadas de onde você quer mover a peça (formato: '[linha] [coluna]', onde linha e coluna são números, de 1 a 8): ")
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
            # descobrir o lado adversário
            lado_adversario = ut.EnumCor.PRETO if self.lado == ut.EnumCor.BRANCO else ut.EnumCor.BRANCO

            # Mostrar o tabuleiro ao jogador
            self.mostrar_tabuleiro()
            print(f"Cheque: {self.cheque}")

            # Montar a jogada que será realizada e executá-la
            coordenada_origem, coordenada_destino = self.montar_jogada()
            self.tabuleiro.mover_peca(coordenada_origem, coordenada_destino)
            
            tp = self.tabuleiro.get_peca_na_posicao(coordenada_destino)
            if isinstance(tp, Peao):
                print(tp.movimentos_para_tomadas)

            # Averiguar cheque
            self.cheque, self.peca_dando_cheque = self.checar_cheque()

            if self.cheque:
                if self.sem_movimentos_legais(lado_adversario):
                    # Cheque mate, é cheque e não há movimentos legais
                    self.ganhador = self.lado
                    self.jogo_em_andamento = False
            elif self.sem_movimentos_legais(lado_adversario):
                # Afogamento, não é cheque e não há movimentos legais
                self.jogo_em_andamento = False

            self.alterar_lado()

        # Jogo acabou
        self.mostrar_tabuleiro()
        if self.ganhador:
            print(f"CHEQUE MATE, GANHADOR: {self.ganhador.value}")
        else:
            print("Afogou")

    def checar_cheque(self) -> tuple [bool, Peca| None]:
        """
        Checa se algum dos lados está em cheque, retornando a peça que está deixando o rei em cheque além da informação se o cheque ocorre
        """
        coordenadas_rei_branco: Coordenada = self.tabuleiro.get_rei_branco().coordenada_atual
        coordenadas_rei_preto: Coordenada = self.tabuleiro.get_rei_preto().coordenada_atual

        for i in range(8):
            for j in range(8):
                peca = self.tabuleiro.get_peca_na_posicao(Coordenada(i, j))

                if peca is None:
                    continue

                if ((coordenadas_rei_branco in peca.lista_de_posssiveis_movimentos) and (peca.cor == ut.EnumCor.PRETO)) or ((coordenadas_rei_preto in peca.lista_de_posssiveis_movimentos) and (peca.cor == ut.EnumCor.BRANCO)):
                    return True, peca
                    
        return False, None

    def rei_em_cheque(self, lado: ut.EnumCor) -> bool:
        """
        Verifica se o rei de um lado está em chque
        """
        coordenadas_rei = ((self.tabuleiro.get_rei_branco().coordenada_atual) if lado == ut.EnumCor.BRANCO else (self.tabuleiro.get_rei_preto().coordenada_atual))

        for i in range(8):
            for j in range(8):
                peca = self.tabuleiro.get_peca_na_posicao(Coordenada(i, j))

                if peca is None:
                    continue

                if peca.cor == lado:
                    continue

                if coordenadas_rei in peca.lista_de_posssiveis_movimentos:
                    return True

        return False
    
    def sem_movimentos_legais(self, lado: ut.EnumCor) -> bool:
        for peca in self.tabuleiro.get_pecas_de_uma_cor(lado):
            origem = peca.coordenada_atual

            for destino in peca.lista_de_posssiveis_movimentos:
                peca_tomada = self.tabuleiro.mover_peca(origem, destino, simulacao=True)
                continua_em_cheque = self.rei_em_cheque(lado)
                self.tabuleiro.voltar_movimento(origem, destino, peca_tomada)

                if not continua_em_cheque:
                    return False
                
        return True