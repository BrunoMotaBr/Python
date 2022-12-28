import array as arr
##import numpy as np
from abc import ABCMeta,abstractmethod

class conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    def deposita(self, valor):
        self._saldo += valor
    @abstractmethod
    def passa_um_mes(self):
        pass
    def __str__(self):
        return "(>>Codigo {} Saldo {}<<)".format(self._codigo, self._saldo)

class contaCorrente(conta):
    def passa_um_mes(self):
        self._saldo -= 2

class contaPoupaca(conta):
    def passa_um_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class contaIvestimento(conta):
    pass


conta16 = contaCorrente(16)
conta16.deposita(1000)
conta16.passa_um_mes()
print(conta16)
conta18 = contaPoupaca(18)
conta18.deposita(1000)
conta18.passa_um_mes()
print(conta18)
contas = [conta16,conta18]
for conta in contas:
    conta.passa_um_mes()
    print(conta)

#conta8 = contaIvestimento(752)


##arr.array('d',[1,3.5])

##numeros = np.array([1,3.5])

