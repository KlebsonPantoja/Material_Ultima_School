class Cachorro:
    def __init__(self, nome: str, raca: str, comprimento: float, peso: float):
        self.nome = nome
        self.raca = raca
        self.comprimento = comprimento
        self.peso = peso
    def latir(self):
        print(f'Au au! Eu sou o(a) {self.nome}')
    def morder(self):
        print(f'O(a) cachorro(a) {self.nome} te mordeu!')
    def dormir(self):
        print(f'ZzzZzZzZ...')
    def brincar(self):
        print(f'Eu gosto de brincar de bolinha')
    def comer(self):
        print(f'Eu peso {self.peso}kg e presciso comer {self.peso * 1000 * 0.01}g de comida para ficar satisfeito!')
    def status(self):
        return f'{self.nome}, {self.raca}, {self.comprimento}, {self.peso}'

dog1 = Cachorro("Becca", "West", 65, 7)
dog2 = Cachorro("Marley","Pinscher",80, 9 )


