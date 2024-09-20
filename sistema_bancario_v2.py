from datetime import datetime

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

def depositar(saldo, valor, extrato, /):  #Função depósito pode receber argumentos apenas por posição: sugestão de argumentos
  #do depósito: saldo ,valor e extrato  >>> Sugestão de retorno: Saldo e extrato
    saldo += valor
    hora_deposito = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"\n Depósito: {valor:.2f} - {hora_deposito}")
    print("Depósito Efetuado com Sucesso!")
    return saldo,extrato

def sacar(*,saldo,extrato,limite,numero_saques,limite_de_saques,saques): #A função de saque deve receber argumentos apenas por nome

    if numero_saques < limite_de_saques: #verifica se já foi excedido o limite de saque
        valor_saque = float(input("Quanto Deseja Sacar? R$"))
        if valor_saque > 0:#verifica se o valor que o usuario esta colocando é positivo
            if valor_saque <= 500: #verifica se o valor do saque segue a regra de R$500 por saque
                if (saldo - valor_saque) < 0:
                    print("Saldo Insuficiente")
                else:
                    saldo -= valor_saque
                    hora_saque = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    extrato.append(f"\n Saque: {valor_saque:.2f} - {hora_saque}")
                    numero_saques += 1
                    print(f"Quantidade de Saques {numero_saques}")
                    return saldo ,extrato, numero_saques
            else:
                print("Você Não Pode Fazer um Saque acima de R$500")
                return saldo ,extrato, numero_saques
        else:
            print("Erro Na Operação! Digite um Valor positivo!")
            return saldo ,extrato, numero_saques
    else:
        print("Limite de Saque Excedido! Você não Pode fazer mais que três Saques!")
        return saldo ,extrato,numero_saques


def extrato(saldo,/,*,extrato):  #A função de extrato deve receber argumentos por posição e por nome
  #===>>> argumentos posicionais:Saldos , argumentos nomeados: Extratos
    print("=============== Extrato ===============\n")
    if not extrato:
        print("Ainda Não Há Movimentações!")
    else:
        print(f"Saldo: R${saldo:.2f}")
        for operacao in extrato:
            print(operacao)
def filtrar_usuario():
    pass

def criar_usuarios(usuarios):
    pass

def criar_conta():
    pass

def main():

    LIMITE_DE_SAQUE = 3
    saldo = 0.0
    contas = []
    usuarios = []
    numero_contas = 0
    saques = []
    depositos = []
    extratos = []
    limite = 500
    numero_saques = 0

    while True:
        try:

            opcao = menu()
            parada = True
            match(opcao):
                case 1:
                    valor = float(input("Quanto Deseja Depositar? R$"))
                    saldo, extratos = depositar(saldo, valor, extratos)

                case 2:
                    saldo,extratos ,numero_saques = sacar(saldo=saldo,extrato=extratos,limite=limite,numero_saques=numero_saques,limite_de_saques=LIMITE_DE_SAQUE,saques=saques)

                case 3:
                    extrato(saldo,extrato=extratos)
                case 0:
                    parada = False

            if parada == False:
                break

        except ValueError: #aqui ele verifica se foi clicado a tecla enter
            print("Digite Uma Opção Válida ")
main()

