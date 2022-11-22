import numpy as np

class Aeroporto:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_avioes = 0
        self.avioes = np.empty(self.capacidade, dtype=int)
        self.identificacao_letra = np.chararray(self.capacidade, unicode=True)
        self.identificacao_num = np.chararray(self.capacidade, unicode=True)

    def __pista_vazia(self):
        if self.numero_avioes == 0:
            return True
        else:
            return False

    def __pista_cheia(self):
        if self.numero_avioes == self.capacidade:
            return True
        else:
            return False

    def add_lista_espera(self, aviao, identificacao_letra:str, identificacao_num:str):
        if self.__pista_cheia():
            print("A PISTA ESTÁ CHEIA DE AVIÕES!!")
            return

        if self.final == self.capacidade - 1:
            self.final = -1

        self.final += 1
        self.avioes[self.final] = aviao
        self.identificacao_letra[self.final] = identificacao_letra
        self.identificacao_num[self.final] = identificacao_num
        self.numero_avioes += 1

    def autorizar_decolagem(self):
        if self.__pista_vazia():
            print('TODOS AVIÕES JÁ FORAM DECOLADOS!!')
            return

        temp = self.avioes[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade -1:
            self.inicio = 0
        else:
            self.numero_avioes -= 1
            return temp

    def caracteristicas_primeiro_aviao(self):
        if self.__pista_vazia():
            print("SEM AVIÕES NA FILA!!")
        else:
            primeiro_aviao = self.avioes[self.inicio]
            letra_primeiro_aviao = self.identificacao_letra[self.inicio]
            num_primeiro_aviao = self.identificacao_num[self.inicio]

            print(f"""PRÓXIMO AVIÃO A DECOLAR:{primeiro_aviao}
IDENTIFICAÇÃO LETRA: {letra_primeiro_aviao}
IDENTIFICAÇÃO NUM: {num_primeiro_aviao}\n""")

    def num_avioes(self):
        if self.__pista_vazia():
            print("SEM AVIÕES NA FILA!!")
        else:
            print(f"O NÚMERO DE AVIÕES NA FILA É DE {self.numero_avioes}!!\n")

    def listar_avioes(self):
        for i in range(len(self.avioes)):
            print(f"""FILA DE ESPERA:
AVIAO {self.avioes[i]}\n""")


if __name__ == "__main__":
    a = Aeroporto(10)
    a.add_lista_espera(1,"B","1")
    a.add_lista_espera(2,"C","2")
    a.add_lista_espera(3,"D","3")
    a.add_lista_espera(4,"E","4")
    a.add_lista_espera(5,"F","5")
    a.add_lista_espera(6,"G","6")
    a.add_lista_espera(7,"H","7")
    a.add_lista_espera(8,"I","8")
    a.add_lista_espera(9,"J","9")
    a.add_lista_espera(10,"K","10")

    a.num_avioes()
    a.caracteristicas_primeiro_aviao()
    a.listar_avioes()
    a.autorizar_decolagem()
    a.num_avioes()
