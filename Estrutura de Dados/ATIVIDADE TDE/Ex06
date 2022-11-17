import numpy as np

class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade 
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print("Lista vazia!!")
        else:
            for i  in range(self.ultima_posicao +1):
                print(f"{i} -> {self.valores[i]}")

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print("Capacidade máxima atingida!!")
        else:
            self.ultima_posicao +=1
            self.valores[self.ultima_posicao] = valor

    def pesquisa_pos(self,valor):
        for i  in range(self.ultima_posicao +1):
            if valor == self.valores[i]:
                return i
            
        return -1

    def excluir(self, valor):
        posicao = self.pesquisa_pos(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]      
            self.ultima_posicao -= 1

    def pesquisa_num(self,valor):
        for i  in range(self.ultima_posicao +1):
            if valor == self.valores[i]:
                return f"O número {valor} pertence a lista"
            
        return f"O número {valor} não pertence a lista"
            
    
if __name__ == "__main__":

    lista = ListaSequencial(3)
    lista.insere(3)
    lista.insere(8)
    lista.insere(7)
    lista.imprime()
    print(lista.pesquisa_num(3))
    lista.excluir(3)
    lista.imprime()
    print(lista.pesquisa_num(3))
    
