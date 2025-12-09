menu = """

 [1] Depositar
 [2] Sacar
 [3] Extrato
 [4] Cadastrar usuário
 [5] Cadastrar conta bancária
 [6] Listar contas
 
 [0] Sair

=> """

def funcaoDepositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def funcaoSacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def funcaoExtrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def funcaoCadastrarUsuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario_existente = [u for u in usuarios if u["cpf"] == cpf]

    if usuario_existente:
        print("⚠️ Já existe um usuário cadastrado com este CPF!")
        return usuarios

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")

    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("UF: ")

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("✔ Usuário cadastrado com sucesso!")

    return usuarios

def funcaoCadastrarConta(contas, usuarios):
    cpf = input("Informe o CPF do usuário para vincular a conta: ")

    filtro_usuario = [u for u in usuarios if u["cpf"] == cpf]

    if filtro_usuario:
        usuario_procurado = filtro_usuario[0]
        
        numero_conta = len(contas) + 1
        
        agencia = "0001"
        
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario_procurado
        }
        
        contas.append(conta)
        print("✔ Conta criada com sucesso!")
        print(f"   Dados: Agência: {agencia} | Conta: {numero_conta} | Titular: {usuario_procurado['nome']}")
    else:
        print("⚠️ Usuário não encontrado! Cadastre o usuário antes de criar a conta.")

    return contas

def listarContas(contas):
    if len(lista_contas) > 0:
        for conta in lista_contas:
            print(f"Ag: {conta['agencia']} | CC: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    else:
        print("Nenhuma conta cadastrada.")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
lista_usuarios = []
lista_contas = []

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        saldo, extrato = funcaoDepositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = funcaoSacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

        if valor <= saldo + valor and valor <= limite and numero_saques < LIMITE_SAQUES:
            numero_saques += 1
        
    elif opcao == "3":
        funcaoExtrato(saldo, extrato=extrato)

    elif opcao == "4":
        funcaoCadastrarUsuario(usuarios)

    elif opcao == "5":
        funcaoCadastrarConta(lista_contas, usuarios)
        
    elif opcao == "6":
        listarContas(lista_contas)

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")