class Pessoa():
    import datetime
    objects = [ ]
    qtd = 0
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
    def idade(self):
        import datetime
        delta = datetime.date.today() - self.nascimento
        return int(delta.days/365)
    def __str__(self):
        for i in self.objects:
            print(i[0], i[1])
    def grava(self):
        Pessoa.qtd += 1
        Pessoa.objects.append(['Nome:', nome])
        Pessoa.objects.append(['Idade:', idade])
while True:
    nome = input('Informe um nome:')
    idade = int(input('Informe uma idade:'))
    obj = Pessoa(nome,idade)
    obj.grava()
    print('Deseja inserir mais um colaborador no sistema?\n1 - Inserir\n2 - Encerrar.')
    condicao = int(input('Digite 1 para inserir, 2 para encerrar o programa:'))
    if not condicao == 1:
        print(obj.__str__())
        break

