'''''
Questão 5
'''''
x = int(input('Digite um Número: '))
aux = []
for i in range(1,x+1):
    mult = 0
    for j in range(1,i+1):
        if i % j == 0:
            mult += 1
    if mult == 2:
        aux.append(i)
   
print('Os números primos são')
for i in aux:
    print(i)