'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com o nome do mês
por extenso'''

dia, mês, ano = input('Informe a sua data de nascimento (dd/mm/aaaa): ').split('/')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
print('Você nasceu em: ')
print('%s de %s de %s' %(dia, meses[int(mês) - 1], ano))
