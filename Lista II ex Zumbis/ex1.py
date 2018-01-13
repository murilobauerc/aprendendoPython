# Lista de exercicios de python II

#1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar
#se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
#se o mesmo é: equilátero, isósceles ou escaleno.


a = int(input('Informe o primeiro lado do triângulo: '))
b = int(input('Informe o segundo lado do triângulo: '))
c= int(input('Informe o terceiro lado do triângulo: '))

if a < b + c and a > b - c:
    if(a == b == c):
        print('As medidas dos lados satisfazem a condição de triângulo equilátero.')
    elif(a == b != c) or (a == c != b):
        print('As medidas dos lados satisfazem a condição de triângulo isósceles.')
    elif(a != b and b != c):
        print('As medidas dos lados satisfazem a condição de triângulo escaleno.')
else:
    print('As medidas dos lados passados não satisfazem a condição de existência de um triângulo.')
