from banco import Banco
from conta import Conta
from status import (
    SUCESSO, ERRO_SENHA, ERRO_SALDO, ERRO_VALOR, 
    ERRO_CONTA_NAO_ENCONTRADA, ERRO_LIMITE_CONTAS
)

class Interface:
    def __init__(self):
        self._banco = Banco()

    def iniciar(self):
        while True:
            self._menu_principal()
            try:
                opcao = int(input("Escolha uma opcao: "))
            except ValueError:
                print("Opcao invalida")
                continue

            if opcao == 1:
                self._operacoes_cliente()
            elif opcao == 2:
                self._operacoes_funcionario()
            elif opcao == 0:
                print("Encerrando...")
                break
            else:
                print("Opcao invalida")

    def _menu_principal(self):
        print("\n--- BANCO ---")
        print("1 - Cliente")
        print("2 - Funcionario")
        print("0 - Sair")

    def _menu_cliente(self):
        print("\n--- CLIENTE ---")
        print("1 - Saque")
        print("2 - Deposito")
        print("3 - Saldo")
        print("4 - Transferencia")
        print("0 - Voltar")

    def _menu_funcionario(self):
        print("\n--- FUNCIONARIO ---")
        print("1 - Cadastrar conta")
        print("2 - Remover conta")
        print("0 - Voltar")

    def _operacoes_cliente(self):
        try:
            num = int(input("Numero da conta: "))
        except ValueError:
            print("Numero invalido")
            return

        conta = self._banco.busca_conta(num)

        if conta is None:
            print("Conta nao encontrada")
            return

        try:
            senha = int(input("Senha: "))
        except ValueError:
            print("Senha invalida")
            return

        if not conta.valida_senha(senha):
            print("Senha invalida")
            return

        while True:
            self._menu_cliente()
            try:
                op = int(input("Escolha uma opcao: "))
            except ValueError:
                print("Opcao invalida")
                continue

            if op == 0:
                break

            if op == 1: # saque
                try:
                    valor = float(input("Digite o valor para saque: "))
                    self._tratar_status(conta.saque(senha, valor))
                except ValueError:
                    print("Valor invalido")

            elif op == 2: # deposito
                try:
                    valor = float(input("Digite o valor para deposito: "))
                    self._tratar_status(conta.deposito(valor))
                except ValueError:
                    print("Valor invalido")

            elif op == 3: # saldo
                status, saldo = conta.get_saldo(senha)
                self._tratar_status(status)
                if status == SUCESSO:
                    print(f"Saldo atual: {saldo:.2f}")

            elif op == 4: # transferencia
                try:
                    destino = int(input("Digite o numero da conta destino: "))
                    valor = float(input("Digite o valor da transferencia: "))
                    self._tratar_status(self._banco.transferir(num, destino, senha, valor))
                except ValueError:
                    print("Entrada invalida")

    def _operacoes_funcionario(self):
        try:
            senha_func = int(input("Senha do funcionario: "))
        except ValueError:
            print("Senha invalida")
            return
        
        if self._banco.autenticar_funcionario(senha_func) != SUCESSO:
            print("Senha de funcionario invalida")
            return

        while True:
            self._menu_funcionario()
            try:
                op = int(input("Escolha uma opcao: "))
            except ValueError:
                print("Opcao invalida")
                continue
            
            if op == 0:
                break
        
            if op == 1:
                try:
                    numero = int(input("Numero da conta: "))
                    senha = int(input("Senha da conta: "))
                    nome = input("Nome do titular: ")
                    tipo = input("Tipo da conta: ")
                    saldo = float(input("Saldo inicial: "))

                    nova_conta = Conta(senha, numero, nome, tipo, saldo)
                    self._tratar_status(self._banco.cadastrar_conta(senha_func, nova_conta))
                except ValueError:
                    print("Entrada invalida")

            elif op == 2:
                try:
                    numero = int(input("Digite o numero da conta que deseja remover: "))
                    self._tratar_status(self._banco.remove_conta(senha_func, numero))
                except ValueError:
                    print("Numero invalido")

    def _tratar_status(self, status):
        if status == SUCESSO:
            print("Operacao realizada com sucesso")
        elif status == ERRO_SENHA:
            print("Erro: senha invalida")
        elif status == ERRO_SALDO:
            print("Erro: saldo insuficiente")
        elif status == ERRO_VALOR:
            print("Erro: valor invalido")
        elif status == ERRO_CONTA_NAO_ENCONTRADA:
            print("Erro: conta nao encontrada")
        elif status == ERRO_LIMITE_CONTAS:
            print("Erro: limite de contas atingido")
