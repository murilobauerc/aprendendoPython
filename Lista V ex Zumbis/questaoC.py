'''Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7?'''


quantNum = 0
for i in range(1067,3628):
    if i % 2 == 0 and i % 7 == 0:
        quantNum += 1

print(quantNum)
# Resposta: 183 números são pares e são divisíveis por 7 entre o intervalo  [1067,3627]

    
