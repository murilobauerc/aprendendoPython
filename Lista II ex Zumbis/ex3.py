#3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
#o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
#que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
#faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
#Se houver, gravar na
#variável excesso e na variável multa o valor da multa que João deverá pagar.
#Caso contrário mostrar tais
#variáveis com o conteúdo ZERO.


peso = int(input('Informe o peso de peixes: '))
if peso > 50:
    print('Peso de peixes pescado excedeu segundo o regulamento de pesca de São Paulo.')
    excesso = (peso - 50)
    multa = excesso * 4
else:
    print('Peso de peixes pescado NÃO excedeu segundo o regulamento de pesca de São Paulo.')
    excesso = 0
    multa = 0

print('Peso de peixes pescado: %dkg' %peso)
print('Excesso de peixe pescado (acima de 50kg): %dkg' %excesso)
print('Valor da multa: %5.2f' %multa)
