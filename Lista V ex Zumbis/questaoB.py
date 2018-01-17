''' Questão B. Quantas vezes o trecho de pseudocódigo seguinte imprime 'oi'? (obs: na
nossa pseudo-linguagem, o laço inclui os extremos, ou seja, 1 até 4 significa 1, 2, 3, 4.)'''

para i = 1 até 9 # 1,2,3,4,5,6,7,8,9
 se i != 3, então
 para j = 1 até 6 #1,2,3,4,5,6
 imprime 'oi'

''' for i in range(1,10):  # i = 1,2,3,4,5,6,7,8,9 
        if i != 3:
            for j in range(1,7): # j = 1,2,3,4,5,6
                print('oi')
'''
''' Executará no primeiro laço for e no if (pois na primeira vez 'i' vale 1) e entrará no segundo laço for.
O segundo laço percorre de j=1 até j=6, printando 6 vezes 'oi' (RELEMBRANDO: aqui i = 1)
Retornará para o primeiro laço e agora 'i' valerá 2, novamente entrará no segundo laço, e fará o que foi explicado acima.
Nesse momento foi printado 12 vezes 'oi'.
Na próxima iteração 'i' valerá 3, e não cairá no segundo laço for, dessa forma pulará e executará com 'i' valendo 4... até 9.
De forma resumida:
    i = 1 (printará 6 vezes 'oi')
    i = 2 (printará 6 vezes 'oi')
    i = 3 (não printará nada)
    i = 4 (printará 6 vezes 'oi')
    i = 5 (printará 6 vezes 'oi')
    i = 6 (printará 6 vezes 'oi')
    i = 7 (printará 6 vezes 'oi')
    i = 8 (printará 6 vezes 'oi')
    i = 9 (printará 6 vezes 'oi')'''
    
# Resultado final: 6 x 8 = 48
