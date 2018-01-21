'''Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995'''

# Transformar para texto e usar o operador 'in'
numSortudo = 0
for i in range(18644, 33088):
    i = str(i)
    if '7' not in i and '2' in i:
        numSortudo+= 1
print(numSortudo)
    
  
        
