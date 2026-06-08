from peca.peao import Peao
import utils.utils as ut
from peca.cavalo import Cavalo

peao_novo = Peao(ut.EnumCor.PRETO)

cavalo_novo = Cavalo(ut.EnumCor.BRANCO)

print(cavalo_novo.caractere)