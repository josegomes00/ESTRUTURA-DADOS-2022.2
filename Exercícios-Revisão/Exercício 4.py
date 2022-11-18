'''''
Questão 4
'''''
x = input('Digite um ANO: ')
for i in x:
    i = int(i)
    var = 0
    var += i

var = var%4
if var == 0:
    print("BISSEXTO")

else:
    print("NÃO É BISSEXTO")