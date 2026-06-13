from datetime import datetime, timedelta # utilizado para calcular o tempo de cada jogada

class Jogador:

    def __init__(self, nome: str, id: int):
        self.__nome = nome
        self.__id = id
        self.__lista_pecas = []
        self.__lista_movimentos = []
        self.__tempo_restante = timedelta(minutes=10)  # Exemplo: 10 minutos por jogador
        self.__turno_iniciado_em = None  # para calcular o tempo gasto em cada

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


      # ── tempo ─────────────────────────────────────────────────────────────────

    @property
    def tempo_restante(self) -> timedelta:
        return self.__tempo_restante

    def iniciar_turno(self):
        self.__turno_iniciado_em = datetime.now()

    def encerrar_turno(self):
        if self.__turno_iniciado_em is None:
            raise RuntimeError("Turno não foi iniciado corretamente. Chame iniciar_turno() primeiro.")

        tempo_gasto = datetime.now() - self.__turno_iniciado_em
        self.__tempo_restante -= tempo_gasto

        if self.__tempo_restante < timedelta(0):
            self.__tempo_restante = timedelta(0)

        self.__turno_iniciado_em = None  # reseta para o próximo turno

    def tempo_esgotado(self) -> bool:
        return self.__tempo_restante <= timedelta(0)

    def tempo_formatado(self) -> str:
        total_segundos = int(self.__tempo_restante.total_seconds())
        minutos, segundos = divmod(total_segundos, 60)
        return f"{minutos:02d}:{segundos:02d}"


    # ── Representação ────────────────────────────────────────────────────────

    def __str__(self) -> str:
        return (
            f"Jogador(id={self.__id}, nome='{self.__nome}', "
            f"peças={len(self.__lista_pecas)}, "
            f"movimentos={len(self.__lista_movimentos)})"
        )

    def __repr__(self) -> str:
        return self.__str__()
