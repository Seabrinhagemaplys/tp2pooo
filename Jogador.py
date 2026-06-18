

class Jogador:

    def __init__(self, nome: str, id: int, desistencia: bool = False):
        self.__nome = nome
        self.__id = id
        self.__lista_pecas = []
        self.__lista_movimentos = []
        self.__desistencia = desistencia

    # ── Getters e Setters: nome ──────────────────────────────────────────────

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome deve ser uma string não vazia.")
        self.__nome = novo_nome.strip()

    # ── Getters e Setters: id ────────────────────────────────────────────────

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, novo_id: int):
        if not isinstance(novo_id, int) or novo_id < 0:
            raise ValueError("O id deve ser um inteiro não negativo.")
        self.__id = novo_id

    # ── Getter: lista_pecas (sem setter direto) ──────────────────────────────

    @property
    def lista_pecas(self) -> list:
        return list(self.__lista_pecas)  # retorna cópia defensiva

    def adicionar_peca(self, peca):
        self.__lista_pecas.append(peca)

    def remover_peca(self, peca):
        if peca in self.__lista_pecas:
            self.__lista_pecas.remove(peca)
        else:
            raise ValueError(f"Peça {peca} não encontrada na lista.")

    # ── Getter: lista_movimentos (sem setter direto) ─────────────────────────

    @property
    def lista_movimentos(self) -> list:
        return list(self.__lista_movimentos)  # retorna cópia defensiva

    def registrar_movimento(self, movimento: str):
        if not isinstance(movimento, str) or not movimento.strip():
            raise ValueError("O movimento deve ser uma string não vazia.")
        self.__lista_movimentos.append(movimento.strip())



    # ── Getter e Setter da Desistência ────────────────────────────────────────────────────────
    @property
    def desistencia(self) -> bool:
        return self.__desistencia   
    
    @desistencia.setter
    def desistencia(self, valor: bool):
        if not isinstance(valor, bool):
            raise ValueError("A desistência deve ser um valor booleano.")
        self.__desistencia = valor


    # ── Representação ────────────────────────────────────────────────────────

    def __str__(self) -> str:
        return (
            f"Jogador(id={self.__id}, nome='{self.__nome}', "
            f"peças={len(self.__lista_pecas)}, "
            f"movimentos={len(self.__lista_movimentos)})"
        )

    def __repr__(self) -> str:
        return self.__str__()
