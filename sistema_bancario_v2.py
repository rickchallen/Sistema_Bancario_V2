from datetime import datetime

def menu():
  texto = """\n\t=============== Menu ===============

    [1] -->>> Depósito
    [2] -->>> Saque
    [3] -->>> Extrato Bancário
    [4] -->>> Criar Usuário
    [5] -->>> Criar Conta
    [6] -->>> Listar Contas
    [0] -->>> Sair Do ProGrama
    Escolha Uma Opção: 
  """

  return int(input(texto))

def depositar(saldo, valor, extrato, /):  #Função depósito pode receber argumentos apenas por posição: sugestão de argumentos
  #do depósito: saldo ,valor e extrato  >>> Sugestão de retorno: Saldo e extrato
    saldo += valor
    hora_deposito = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"\n Depósito: {valor:.2f} - {hora_deposito}")
    print("Depósito Efetuado com Sucesso!")
    return saldo,extrato

def sacar(*,saldo,extrato,limite,numero_saques,limite_de_saques): #A função de saque deve receber argumentos apenas por nome

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
def filtrar_usuario(cpf,usuarios):
    user = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return user[0] if user else None

def criar_usuarios(usuarios):
    cpf = input("Digite O CPF Do Usuario ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Esse Usuario Já Existe! O Fluxo de Criação de Usuário Foi encerrado!")
    else:
        nome = input("Digite O Nome Do usuário: ")
        endereco = input("Digite O Endereço no Formato: logradouro, número - bairro - cidade/Sigla estado ")
        data_nascimento = input("Digite a Data de Nascimento No Formato dd-mm-yy: ")
        usuarios.append({"nome": nome, "endereco": endereco, "data_nascimento": data_nascimento, "cpf": cpf})
        print("Usuario Cadastrado Com Sucesso!")

def criar_conta(agencia,n_contas,usuarios,contas):
    cpf = input("Informa o CPF do Usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
      contas.append({"Agência": agencia, "Conta": n_contas, "usuario": usuario})
      print("Conta Criada com Sucesso!")
    else:
        print("Usuário Não Cadastrado! Crie uma Conta Para um Usuário que Já esta cadastrado")

def listar_contas(contas):
  print(f"=============== Contas ===============\n")
  if not contas:
      print("Ainda Não Foram Criadas Contas! ")
  else:
      for conta in contas:
          print(f"\n\tAgência: {conta["Agência"]} \n \tConta: {conta["Conta"]} \n \tNome: {conta["usuario"]["nome"]}")



def main():

    LIMITE_DE_SAQUE = 3
    AGENCIA = "0001"
    saldo = 0.0
    contas = []
    usuarios = []
    numero_contas = 0
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
                    saldo,extratos ,numero_saques = sacar(saldo=saldo,extrato=extratos,limite=limite,numero_saques=numero_saques,limite_de_saques=LIMITE_DE_SAQUE)

                case 3:
                    extrato(saldo, extrato=extratos)
                case 4:
                    criar_usuarios(usuarios)
                case 5:
                  numero_contas = len(contas)
                  numero_contas +=1
                  criar_conta(AGENCIA, numero_contas, usuarios,contas)

                case 6:
                    listar_contas(contas)
                case 0:
                    parada = False

            if parada == False:
                break

        except ValueError: #aqui ele verifica se foi clicado a tecla enter
            print("Digite Uma Opção Válida ")
main()

