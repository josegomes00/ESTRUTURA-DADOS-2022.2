import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype= int)

    def __pilha_cheia(self):
        if self.topo == self.capacidade -1:
            return True

        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True

        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("PILHA CHEIA")

        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("PILHA VAZIA")
            return -1

        else:
            valor = self.valores[self.topo]
            self.topo -=1
            return valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def imprimir_inversamente(self):
        pilha_inversa = []
        for i in self.valores[::-1]:
            pilha_inversa.append(i)

        return pilha_inversa

if __name__ == "__main__":
    pilha = Pilha(10)
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    pilha.empilhar(4)
    pilha.empilhar(5)
    pilha.empilhar(6)
    pilha.empilhar(7)
    pilha.empilhar(8)
    pilha.empilhar(9)
    pilha.empilhar(10)

    print(pilha.imprimir_inversamente())