'''4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.'''

i = 0
a = 1
b = 1
print('Fibonacci!')
num = int(input('Informe um número: '))
while i < num:
    print(a,b, end =' ')
    a = a + b
    b = a + b
    i+= 1

