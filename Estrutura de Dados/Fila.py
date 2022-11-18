import numpy as np

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        if self.numero_elementos == 0:
            return True
        else:
            return False

    def __fila_cheia(self):
        if self.numero_elementos == self.capacidade:
            return True
        else:
            return False

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A FILA ESTÁ CHEIA")
            return

        if self.final == self.capacidade - 1:
            self.final = -1

        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila já está vazia')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade -1:
            self.inicio = 0
        else:
            self.numero_elementos -= 1
            return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        else:
            return self.valores[self.inicio]