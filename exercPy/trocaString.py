
palavra =  input('Informe uma palavra: ')
i = 0
troca = ""
while i < len(palavra):
    if  palavra[i] in 'aeiou':
        troca = troca + "*"
    else:
        troca = troca + palavra[i]
    i += 1
    
print('Nova palavra: %s' %troca)


