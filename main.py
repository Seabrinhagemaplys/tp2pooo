from peca.bispo import Bispo
from tabuleiro.tabuleiro import Tabuleiro
import utils.utils as ut
from coordenada.coordenada import Coordenada

t = Tabuleiro()

print(t.gerar_string_tabuleiro(ut.EnumCor.BRANCO))
