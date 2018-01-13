# Resolução da lista de exercicios I em python PARTE 2

#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.
print('Aumento do salario:')
sal = int(input('Valor do salario:'))
porcentagem = int(input('Porcentagem do aumento:'))
vAumento = sal * (porcentagem / 100)
print('Valor do aumento: R$%d' %vAumento)
novoSal = vAumento + sal
print('Novo salario: R$%d' %novoSal)

print('\n')
#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar.

precoMercadoria = int(input('Informe o preço da mercadoria: '))
percentualDesconto = int(input('Informe o percentual de desconto: '))
vDesconto = precoMercadoria * (percentualDesconto / 100)
precoPagamento =  precoMercadoria - vDesconto
print('Valor do desconto: R$%d' %vDesconto)
print('Preço a pagar: R$ %d' %precoPagamento)

print('\n')
#6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem. 
print('Calculando o tempo de uma viagem de carro.')
distPercorrer = int(input('Distância a percorrer (km):  '))
velocMedia = int(input('Velocidade media esperada para a viagem: '))
tempoViagem = distPercorrer / velocMedia
print('O tempo de viagem sera de: %d (horas)' %tempoViagem)
# Aqui foi usado a fórmula na física de velocidade média (vM = Deslocamento / Tempo)    
