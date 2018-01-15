
# Gravação de arquivo texto 'normal' (C, Java)
arquivo = open ('números.txt' , 'w')
for linha in range (1,101):
    arquivo.write('%d\n' %linha) # escrevo no arquivo um decimal por linha (1 a 100)
arquivo.close()

arquivo = open('números.txt' , 'r')
for linha in arquivo.readlines(): #readlines gera uma lista onde cada elemento é uma linha lida
    print(linha)
arquivo.close()

# 'Pythonic Way'
with open('arquivoTeste.txt' , 'w') as f:
     f.write('Primeiro arquivo texto do Murilo no estilo Pythonic! Python easy way! :)')
# Nota interessante: não é preciso o 'fclose', o comando 'with' é inteligente o suficiente p/ perceber que
# ao término do bloco de comandos é o final e portanto, o arquivo deve ser fechado.





