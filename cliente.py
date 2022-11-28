from jogo1 import Jogo1
from jogo2 import Jogo2
from jogo3 import Jogo3
from jogo4 import Jogo4
from lider import Lider


jogo1 = Jogo1()
jogo1.vencedor(2, "Suiça", "6", "Xaka, Xakiri, Embolo, Elvedi, Schar")

jogo2 = Jogo2()
jogo2.vencedor(3, "Camarôes", "4", "Onana, Kanu, Mbeumo, Ekambi, Wooh ")

jogo3 = Jogo3()
jogo3.vencedor(1, "Brasil   ", "9", "Fred, Rafinha, Richarlison, Paqueta, Vini")

jogo4 = Jogo4()
jogo4.vencedor(4, "Sérvia ", "1", "Mitrovic ,Savic, Tadic, Jovic,Lukic ")



jogo1.lider.print()
jogo2.lider.print()
jogo3.lider.print()
jogo4.lider.print()