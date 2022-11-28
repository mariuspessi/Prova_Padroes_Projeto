from lider import Lider
from interface_jogo import IJogo


class Jogo2(IJogo):
    

    def __init__(self):
        self.lider = Lider()

    def vencedor(self, posicao, nome, pontos, jogadores):
        self.lider.vencedor(posicao, nome, pontos, jogadores)
