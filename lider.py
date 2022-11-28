"A Leaderboard Singleton Class"


class Lider():
    "The Leaderboard as a Singleton"
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        "A class level method"
        print("--- Posição --- ------- País ------- ---- Pontos ---- ------------------------------------- Jogadores -------------------------------------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value[0]}\t|\t{value[1]}\t|\t{value[2]}\t|")
        print()

    @classmethod
    def vencedor(cls, posicao, nome, pontos, jogadores):
        "A class level method"
        cls._table[posicao] = nome, pontos, jogadores
