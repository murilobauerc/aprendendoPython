# dic.keys() dict_keys(['a', 'g', 'o'])
# dic.values() dict_values('alpha', 'gama', 'omega'])

arquivo = open('alice.txt')
texto = arquivo.read()
texto = texto.lower()
import string
for acento in string.punctuation:
    texto = texto.replace(acento, '  ')
texto = texto.split()

dic = { }
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

print('Alice aparece %s vezes' %dic['alice'])
arquivo.close()
