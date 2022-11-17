import numpy as np

class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype = int)
        
    def imprime(self):
        if self.ultima_posicao == -1:
            print("A LISTA ESTÁ VAZIA")
            
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, " - ", self.valores[i])
                
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("CAPACIDADE MAXIMA ATINGIDA")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
            
    def pesquisar(self, valor):
                
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i

        return "Número não encontrado"
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
                
        self.ultima_posicao -=1
            
l = ListaSequencial(6)
l.insere(5)
l.insere(7)
l.insere(22)
l.insere(13)
l.insere(16)
l.insere(18)
l.imprime()
print(l.pesquisar(22))
l.excluir(18)
l.imprime()