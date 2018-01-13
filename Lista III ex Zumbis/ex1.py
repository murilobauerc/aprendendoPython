# Resolução da III lista de exercícios Python

'''1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.'''

while True:
    nota = float(input('Informe uma nota: '))
    if nota >=0 and nota <= 10:
        print('Valor válido! (entre 0 e 10).')
        break
    else:
        print('Valor inválido! Digite novamente. \nDica: de 0 a 10.')
    
