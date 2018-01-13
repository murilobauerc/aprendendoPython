'''3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento'''

# País A = 80.000 hab / taxa de crescimento 3% (2400 hab/ano)
# País B = 200.000 hab / taxa de crescimento 1.5% (3000 hab/ano)

pA = 80000
pB = 200000
anos = 0

while True:
    taxaCrescPA = pA + pA * 0.03
    taxaCrescPB = pB + pB * 0.015
    anos += 1
    if pA == pB or pA >= pB:
        print('Número de anos que levará para a população do país A ultrapasse o país B: %d' %anos)
        break
    else:
        continue



