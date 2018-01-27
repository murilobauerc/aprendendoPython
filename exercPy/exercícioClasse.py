class Colaborador:
    def __init__(self, nome, salario,data):
        self.nome = nome
        self.salario = salario
        self.data = data
        self.objects = [ ]
        self.nomes = [ ]
        
    def gravaCustos(self):
        self.objects.append(['INSS: R$ ',  self.INSS()])
        self.objects.append(['SegVida: R$ ', self.segVida()])
        self.objects.append(['VR: R$ ', self.valeRefeicao()])
        self.objects.append(['VT: R$ ', self.valeTransporte()])
        self.objects.append(['CustTotal: R$', self.custTotal()])
        return self.objects

    def gravaRelatorio(self):
        self.objects.append(['Total Impostos: R$',  self.totImpostos()])
        self.objects.append(['Total Salários: R$',  self.totSalarios()])
##        self.objects.append(['Total Geral: R$',  self.totGeral()])
        return self.objects

    def __str__(self):
        self.nomes.append(['Nome: ', self.nome])
        return self.nomes
    
    def INSS(self):
        return float(self.salario * 0.10)

    def segVida(self):
        return float(self.salario * 0.15)

    def valeRefeicao(self):
        return float(self.salario * 0.11)

    def valeTransporte(self):
        return float(self.salario * 0.05)

    def custTotal(self):
        return float(self.salario + self.totImpostos())
    
    def __repr__(self):
        for op in self.objects:
             return ('%s%5.2f' %(op[0], op[1]))

    def totImpostos(self):
        return float(self.INSS() + self.segVida() + self.valeRefeicao() + self.valeTransporte())
        
    def totSalarios(self):
        self.salario += totSalario
        return float(self.salario)

##    def totGeral(self):
##        return float(self.totImpostos() + totSalarios())
 
if __name__ == '__main__':
    totSalario = 0
    while True:
        nome = input('Informe o nome do colaborador: ')
        salario = float(input('Informe o salário: '))
        data = input('Informe a data: ')
        infoCol = Colaborador(nome,salario,data)
        impressaoCustos = infoCol.gravaCustos()
        infoCol.gravaRelatorio()
        nomes = infoCol.__str__()
        totImposto = infoCol.totImpostos()
        totSalario += infoCol.salario
        print('Deseja inserir mais um colaborador no sistema?\n1 - Inserir\n2 - Encerrar.')
        condicao = int(input('Digite 1 para inserir, 2 para encerrar o programa:'))
        print('\n')
        if not condicao == 1:
            for i in nomes:
                print('%s %s' %(i[0], i[1]))
                for op in impressaoCustos:
                    print('%s%5.2f' %(op[0], op[1]))
            break
                  
