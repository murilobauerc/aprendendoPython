
palavra = input('Informe uma palavra e veja se ela é palíndrome: ')

if palavra == palavra[::-1]:
    print('%s é palíndrome.' %palavra)
else:
    print('%s não é palíndrome.' %palavra)

# arara == arara É palíndrome
# murilo != olirum Não é palíndrome
