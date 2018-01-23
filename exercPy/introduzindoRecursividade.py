# Recursividade

def somatorio(n):
    if (n<=0):
        return 0
    return(n + somatorio(n-1) if n else n)


def potencia(x,n):   # Esta função poderia facilmente substituir a operação de exponenciação (**) do Python, já que faz a mesma coisa. Em questão de desempenho, talvez não.
    if(n == 0):            # Recursão é mais lento. Necessário invocar instâncias menores da própria função diversas vezes, daí o conceito de recursividade.
        return 1
    return (x * potencia(x, n-1))

    '''  potencia(3,2) = (3 * potencia(3,1)); // 3 * 3 = 9;
        if ( n <= 0) return 1; // FALSO
        potencia(3,1) = (3 * potencia(3,0)); // 3 * 1 = 3;
        if ( n <= 0) return 1; // FALSO
        potencia(3,0) = 1;
        if ( n <= 0) return 1; // VERDADEIRO
    '''

# Teste
num = int(input('Informe um numero: '))
print('O somatório de %d é: %d\n' %(num, somatorio(num)))

print(potencia(2,3)) 
print(potencia(3,0))
print(potencia(2,5))
print(potencia(1,4))

