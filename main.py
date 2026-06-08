from tabuleiro.tabuleiro import Tabueiro
import utils.utils as ut
from coordenada.coordenada import Coordenada

tb = Tabueiro()
print(tb.gerar_string_tabuleiro(ut.EnumCor.BRANCO))

tb.mover_peca(Coordenada(1,1), Coordenada(2,1))

print(tb.gerar_string_tabuleiro(ut.EnumCor.BRANCO))
print(tb.gerar_string_tabuleiro(ut.EnumCor.PRETO))


