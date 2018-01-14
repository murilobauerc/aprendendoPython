
palavra = input('Informe uma palavra e veja se ela é palíndrome: ')

if palavra == palavra[::-1]:
    print('%s é palíndrome.' %palavra)
else:
    print('A palavra não é palíndrome.')
