# Segunda Versão do Sistema Bancário Para O Bootcamp Engenharia de dados DIO NTTDATA

def menu():
  texto = """\n\t=============== Menu ===============

    [1] -->>> Depósito
    [2] -->>> Saque
    [3] -->>> Extrato Bancário
    [4] -->>> Listar Contas
    [5] -->>> Novo usuário
    [0] -->>> Sair Do ProGrama
  """

  return int(input(texto))

def depositar(saldo, valor, extrato, /):
    saldo += valor
    extrato += f"\n{extrato} "

def sacar():
    pass

def extrato():
    pass
def filtrar_usuario():
    pass

def criar_usuarios(usuarios):
    pass

def criar_conta():
    pass

def main():
    opcao = menu()
    LIMITE_DE_SAQUE = 3
    Saldo = 0.0
    contas = []
    usuarios = []
    numero_conta s = 0
    saques = []
    depositos

main()

