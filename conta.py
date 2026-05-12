from status import SUCESSO, ERRO_SENHA, ERRO_SALDO, ERRO_VALOR

class Conta:
    def __init__(self, senha=1111, numero=0, titular="Nenhum", tipo="Corrente", saldo=0.0):
        self._senha = senha
        self._numero = numero
        self._titular = titular
        self._tipo = tipo
        self._saldo = saldo if saldo >= 0 else 0.0

    def get_numero(self):
        return self._numero

    def get_titular(self):
        return self._titular

    def get_tipo(self):
        return self._tipo

    def get_saldo(self, senha):
        if self.valida_senha(senha):
            return SUCESSO, self._saldo
        else:
            return ERRO_SENHA, 0.0

    def set_senha(self, nova_senha):
        self._senha = nova_senha

    def deposito(self, valor):
        if valor > 0:
            self._saldo += valor
            return SUCESSO
        else:
            return ERRO_VALOR

    def saque(self, senha, valor):
        if not self.valida_senha(senha):
            return ERRO_SENHA
        if valor <= 0:
            return ERRO_VALOR
        if self._saldo < valor:
            return ERRO_SALDO
        
        self._saldo -= valor
        return SUCESSO

    def transferencia(self, destino, senha, valor):
        status = self.saque(senha, valor)
        if status != SUCESSO:
            return status
        
        destino.deposito(valor)
        return SUCESSO

    def valida_senha(self, senha):
        return self._senha == senha
