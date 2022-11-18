'''''
Questão 2
'''''
x = input('Digite uma NOTA entre 0 e 10\n')

while not x.isdigit():
    print('Apenas Números!!')
    x = input('Digite uma NOTA entre 0 e 10\n')

x = int(x)

while x < 0 or x > 10:
    print('NOTA INVÁLIDA!!')
    x = int(input('Digite uma NOTA entre 0 e 10\n'))

print('Nota Válida!!')