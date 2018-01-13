# Resolução da lista de exercicios I em python

# 1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo numero:'))
soma = n1 + n2
print ('A soma dos dois numeros: %d' %soma)

print('\n')
# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
vlr = int(input('Digite um valor em metros e tenha convertido em milímetros:'))
print(vlr * 1000)

print('\n')
# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.
dias = int(input('Digite a qtd de dias: ')) 
horas = int(input('Digite a qtd de horas: ')) 
minutos = int(input('Digite a qtd de minutos: '))
segundos = int(input('Digite a qtd de segundos:'))
total = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos
print('Convertido tudo em segundos: %d' %total)

print('\n')
#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
#a um milhão
a = str(2**10)
len(a)
print(' 2^10 possui %s dígitos.' %a)

print('\n')


