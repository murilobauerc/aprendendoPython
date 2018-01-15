# Este exercício insere um '*' toda vez que encontrar uma vogal na palavra
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


