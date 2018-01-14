# Números primos são numeros que possuem apenas dois divisores: 1 e ele mesmo.

# Com isso, elaborei duas possiveis formas de realizar a verificação de número primo.

num = int(input('Informe um número: '))
numPrimo = 1  # Flag que será utilizada para regular e separar os números primos dos que não são.
for count in range(2,num):
    if (num % count == 0):
        print('%d não é primo.' %num)
        numPrimo = 0
        break
if numPrimo:
    print('%d é primo.' %num)

# 3) Ainda de uma outra forma, utilizando loop for-else (não é necessária a flag)
num1 = int(input('Informe um número: '))
for contador in range (2,num1):
    if num1 % contador == 0:
        print('Numero não é primo.')
        break
else:
    print('Numero é primo.')

