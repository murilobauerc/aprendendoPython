#7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
#em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
#para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
#Obs. : somente são vendidos um número inteiro de latas.

# lata de tinta = 18 litros = R$ 80,00
# 1L - 3m²
# 18L - x = 54m²
# 1*x = 3*18= 54m²


tamanhoArea = int(input('Informe o tamanho em m² da área a ser pintada: '))
qtdLitros =  tamanhoArea / 3
lataTinta = 0
if qtdLitros <= 18:
    precoTotal = 80
    lataTinta = 1
elif qtdLitros > 18:
    lataTinta = qtdLitros / 18
    precoTotal = 80 * lataTinta
print('A quantidade de latas de tinta a serem compradas é: %d' %lataTinta)
print('O preço total é: R$ %d' %precoTotal)
