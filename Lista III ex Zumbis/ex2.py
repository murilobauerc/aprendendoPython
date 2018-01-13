'''2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

while True:
    nome = input('Informe o nome de usuário: ')
    senha = input('Informe sua senha: ')
    if nome != senha:
        print('Nome de usuario e senha aceitos.')
        break
    else:
        print('Erro! Insira as informações novamente.')
