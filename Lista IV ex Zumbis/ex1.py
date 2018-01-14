'''Lista de Exercícios IV'''

'''1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.'''

import random
n_inteiros = random.sample(range(1,100), 10)
maior = n_inteiros[0]
menor = n_inteiros[0]
i = 0
while i < 10:
    if n_inteiros[i] > maior:
        maior = n_inteiros[i]
    if n_inteiros[i] < menor:
        menor = n_inteiros[i]
    i += 1
print('Maior número da lista (entre 0 e 100): %d' %maior)
print('Menor número da lista (entre 0 e 100): %d' %menor)
    
    
