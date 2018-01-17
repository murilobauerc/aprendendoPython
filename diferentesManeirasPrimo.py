# Números primos são numeros que possuem apenas dois divisores: 1 e ele mesmo.

# Com isso, elaborei três formas possiveis formas de realizar a verificação de número primo.

# 1)
num = int(input('Informe um número:'))
contador = 1
div = 0
if num > 1:  # aqui, verifico se o numero digitado é maior que 1, já que não posso validar 1 como número primo. (divide apenas ele)
    while contador <= num: # for contador in range(contador, num + 1)
        if num % contador == 0:
            div += 1
        contador += 1
if div == 2:
    print('%d é numero primo.' %num) # após verificar todos os números de 1 até o numero digitado, se conter apenas dois divisores, imprime aqui.
else:
    print('%d não é numero primo.' %num)

    
'''2) Esse jeito e o próximo é considerando que o número de entrada seja primo, ou seja tenha
dois divisores, e caso divida durante o laço é porque não é primo (pelo menos 3 divisores), uma forma
rápida de descobrir um primo, pois na primeira vez que der resto 0, já cai do laço.'''
num = int(input('Informe um número: '))
numPrimo = 1  # Flag que será utilizada para regular e separar os números primos dos que não são.
if num > 1:
    for count in range(2,num):
        if (num % count == 0):
            print('%d não é primo.' %num)
            numPrimo = 0
            break
else:
    numPrimo = 0
    print('%d não é primo.' %num)
if numPrimo:
    print('%d é primo.' %num)


# 3) Ainda de uma outra forma, utilizando loop for-else (não é necessária a flag)
num = int(input('Informe um número: '))
for contador in range (2,num):
    if num % contador == 0:
        print('Numero não é primo.')
        break
else:
    print('Numero é primo.')

