#6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
#no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
#são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou
#ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido.
#Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

salHora = int(input('Informe o quanto voce ganha por hora: '))
numHoraTrab = int(input('Informe o numero de horas trabalhadas no dia: '))
salBruto = salHora * numHoraTrab * 30
totalSal = salBruto * 0.89 * 0.92 * 0.95
pagouIR = salBruto * 0.11
pagouINSS = salBruto * 0.08
pagouSindi = salBruto * 0.05
salLiquido = salBruto - (pagouIR + pagouINSS + pagouSindi)

print('a. + Salário Bruto: R$ %5.2f.' %salBruto)
print('b. - IR (11%%): R$ %5.2f.' %pagouIR)
print('c. - INSS (8%%): R$ %5.2f' %pagouINSS)
print('d. - Sindicato (5%%): R$ %5.2f' %pagouSindi)
print('e. = Salário Liquido: R$ %5.2f' %salLiquido)


