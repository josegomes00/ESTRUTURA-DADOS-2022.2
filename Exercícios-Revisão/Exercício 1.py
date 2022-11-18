'''''
Questão 1
'''''
a,b,c = map(int,input('Digite as 3 notas: ').split())
media = (a+b+c)/3
if media == 10:
    print('Aprovado com Distinção')

elif media >= 7:
    print('Aprovado')

else:
    print('Reprovado')