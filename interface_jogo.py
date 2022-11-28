from abc import ABCMeta, abstractmethod


class IJogo(metaclass=ABCMeta):
   
    @staticmethod
    @abstractmethod
    def vencedor(posicao, nome, pontos, jogadores):
        "Vencedores"
