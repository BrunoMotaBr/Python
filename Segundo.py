class contaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    def deposita(self, valor):
        self.saldo += valor
    def __str__(self):
        return "(>>Codigo {} Saldo {}<<)".format(self.codigo, self.saldo)

conta_do_gui = contaCorrente(15)
conta_do_gui.deposita(500)
print(conta_do_gui)
conta_da_dany = contaCorrente(5656)
conta_da_dany.deposita(1000)
print(conta_da_dany)
contas = [conta_do_gui, conta_da_dany]
print(contas)
print(contas[0])

def deposita_para_todas_contas(contas):
    for conta in contas:
        conta.deposita(100)

deposita_para_todas_contas(contas)
print(contas[0])
print(contas[1])
contas.insert(0, 75)
print(contas[0], contas[1], contas[2])

guilherme = ("Guilherme", 37, 1984)
dany = ("Danyela", 43, 1975)
usuarios = [guilherme,dany]