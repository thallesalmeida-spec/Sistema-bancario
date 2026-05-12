from conta import Conta
from status import SUCESSO, ERRO_SENHA, ERRO_CONTA_NAO_ENCONTRADA

class Banco:
    def __init__(self):
        self._senha_funcionario = 9999
        self._contas = [
            Conta(1234, 1, "Joao", "Corrente", 300.0),
            Conta(4567, 2, "Jose", "Poupanca", 800.0),
            Conta(7890, 3, "Maria", "Corrente", 1000.0),
            Conta(8956, 4, "Madalena", "Poupanca", 2000.0)
        ]

    def busca_conta(self, numero):
        for conta in self._contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def cadastrar_conta(self, senha_fun, nova_conta):
        if senha_fun != self._senha_funcionario:
            return ERRO_SENHA
        
        self._contas.append(nova_conta)
        return SUCESSO

    def remove_conta(self, senha_fun, numero):
        if senha_fun != self._senha_funcionario:
            return ERRO_SENHA
        
        conta = self.busca_conta(numero)
        if conta is None:
            return ERRO_CONTA_NAO_ENCONTRADA
        
        self._contas.remove(conta)
        return SUCESSO

    def transferir(self, num_origem, num_destino, senha, valor):
        origem = self.busca_conta(num_origem)
        destino = self.busca_conta(num_destino)

        if origem is None or destino is None:
            return ERRO_CONTA_NAO_ENCONTRADA

        return origem.transferencia(destino, senha, valor)

    def autenticar_funcionario(self, senha):
        if senha != self._senha_funcionario:
            return ERRO_SENHA
        return SUCESSO
