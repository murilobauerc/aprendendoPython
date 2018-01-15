def ipOk(ip):
    ip = ip.split('.') # split pego cada byte, lembrando que em um endereço IP temos 4 bytes separados por ponto
    for byte in ip:
        if int(byte) > 255:  # 1 byte = 8 bits (máximo valor de 8 bits é 255, ou em binário 11111111)
            return False # caso o byte seja maior que 255, não pode ser um IP válido, ou seja, atribuído.
        return True


arquivo = open('IPS.txt')
validos = open('IPSvalidos.txt')
invalidos = open('Inválidos.txt', 'w')
for linha in arq.readlines(): # passo por elemento de cada linha
        if ipOk(linha): # Chamada de função 'ipOk', se retornar True, ou seja, o byte possuir o valor menor que 255
            validos.write(linha) # Ele escreve no arquivo texto de IPS válidos
        else: # Caso contrário, o byte possui o valor maior que 255, escrevendo em um arquivo texto IPS inválidos
            invalidos.write(linha)
arq.close()
validos.close()
invalidos.close()
