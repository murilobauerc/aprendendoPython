# Calcule a média de 5 notas com listas.
notas = [5, 7.6, 2.4, 9, 8.2]
i = 0
soma = 0
while i < 5:
    soma += notas[i]
    i += 1
media = soma / i
print('Media das 5 notas da lista: %5.2f' %media)

i = 0
vetor_num = [ ]
# Utilizando-se de append
while i < 5:
    n = int(input('Informe o numero: '))
    vetor_num.append(n) 
    i += 1
print('Vetor lido: ', vetor_num)

i=0
vetor_reais = [ ]

while i < 10:
    num = float(input('Informe o numero: '))
    vetor_reais.append(num)
    i+= 1
i = 9
while i >= 0:
    print(vetor_reais[i])
    i -= 1



