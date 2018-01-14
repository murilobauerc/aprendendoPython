print('Os 10 primeiros múltiplos de 3: ')
x = 0
contador = 0
while contador <= 10:
        if x % 3 == 0:
            print('%d' %x)
            contador += 1
        x += 1

# SAIDA: 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30

print('Media de 10 numeros inteiros informados pelo usuário: ')
i = 0
soma = 0
while i < 10:
    num = int(input('Informe um numero: ' ))
    soma += num
    i += 1
# fim do while
media = soma / i
print('Media dos 10 numeros informados: %5.2f' %media)
        
