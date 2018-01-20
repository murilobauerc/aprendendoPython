''' Funções que retornam MAIOR NÚMERO entre quaisquer dois números reais. Fazem a mesma coisa,
porém, versões diferentes.'''

# 1) Usando variável p/ atribuir o maior número.
def maiorV1(x,y):
    if x > y:
        maior = x
    elif x < y:
        maior = y
    elif x == y:
        maior = x
    return maior
        
# 2) Sem elif's:
def maiorV2(x,y):
    if x > y:
        maior = x
    else:
        maior = y
    return maior

# 3) Sem else, mais comprimida e clara.
def maiorV3(x,y):
    maior = y
    if x > y:
        maior = x
    return maior

# 4) Utilizando apenas o return, sem necessidade de uma váriavel "maior"
def maiorV4(x,y):
    if x > y:
        return x
    return y

# 5) Usando operator ternário em Python, versão mais robusta e apenas em uma linha.
def maiorV5(x,y):
    return (x if x > y else y)

x = int(input('Informe o primeiro numero: '))
y = int(input('Informe o segundo numero: '))
print(maiorV1(x,y))
print(maiorV2(x,y))
print(maiorV3(x,y))
print(maiorV4(x,y))
print(maiorV5(x,y))


    





        

                                                    

    
    
