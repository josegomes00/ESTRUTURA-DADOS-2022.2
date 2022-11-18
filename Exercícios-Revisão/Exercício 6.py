class Pessoa:
    def __init__(self, idade='', altura=''):
        self.idade = idade
        self.altura = altura
    def __str__(self):
        return f'{self.idade[::-1]},{self.altura[::-1]}'

i1,a1 = input(f'Digite Idade e Altura(cm) da 1º pessoa: ').split()
i2,a2 = input(f'Digite Idade e Altura(cm) da 2º pessoa: ').split()
i3,a3 = input(f'Digite Idade e Altura(cm) da 3º pessoa: ').split()
i4,a4 = input(f'Digite Idade e Altura(cm) da 4º pessoa: ').split()
i5,a5 = input(f'Digite Idade e Altura(cm) da 5º pessoa: ').split()

pessoa1 = Pessoa(i1,a1)
print(pessoa1)
pessoa2 = Pessoa(i2,a2)
print(pessoa2)
pessoa3 = Pessoa(i3,a3)
print(pessoa3)
pessoa4 = Pessoa(i4,a4)
print(pessoa4)
pessoa5 = Pessoa(i4,a4)
print(pessoa5)