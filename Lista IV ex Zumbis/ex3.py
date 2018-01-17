# Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
num = input('Informe um número: ') # aqui a sacada é tratar o número como se fosse string, para que eu possa inverter
num = num[::-1] # do final do número até o inicio, andando -1 casa.
print (num)
