'''5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.'''

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
x, y = a,b
while True:
    if a > 0 and b > 0:
        r = a % b
        a = b
        b = r
        if r == 0:
            break
    else:
        print('Erro! Era p/ ter informado dois números POSITIVOS!')

mdc = a
print('mdc(%d, %d) = %d' %(x,y,mdc))

# mdc (10,2)
# r = 10 % 2 = (r  = 0)
# a = b = (a = 2)
# b = r = (b = 0)


