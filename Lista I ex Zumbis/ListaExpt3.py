# Resolução da lista de exercicios I em python PARTE 3

#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
print('Conversao Celsius -> Fahrenheit')
temp = int(input('Informe um temperatura em CELSIUS: '))
converte = 9*temp/5 + 32
print('A temperatura, em Fahrenheit é: %d' %converte)

print('\n')
#8) Faça agora o contrário, de Fahrenheit para Celsius.
print('Conversao Fahrenheit -> Celsius')
temp = int(input('Informe uma temperatura em FAHRENHEIT: '))      
converte = (temp - 32) * (5/9)
print('A temperatura, em Celsius é: %d' %converte)
    
#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

qtdKmPercorrido = int(input('Informe a quantidade de km percorridos: '))
qtdDias = int(input('Informe a quantidade de dias que o carro foi alugado: '))
precoPagar =  (qtdDias * 60) + (qtdKmPercorrido * 0.15)
print('Preço a pagar pelos km percorridos e pelos dias alugados do carro é de: R$ %d' %precoPagar)
    
#10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.
print('Reducao de tempo de vida de um fumante')
qtdeCigarrosDia = int(input('Informe a quantidade de cigarros fumados por dia: '))
qtdeAnosFumou = int(input('Informe a quantidade de anos que fumou:'))
perdaMin = (qtdeCigarrosDia * 10) / 60
print('O total de dias perdidos por consequencia de fumar é de: %d' %perdaMin)
