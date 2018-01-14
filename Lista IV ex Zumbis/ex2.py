'''2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas'''

import random
vetor = [ ]
for k in range (20):
    vetor.append(random.randint(1,100))

pares = [ ]
impares = [ ]
for x in vetor:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print( ' Vetor ', vetor)
print(' Pares ', pares)
print(' Ímpares ', impares)

