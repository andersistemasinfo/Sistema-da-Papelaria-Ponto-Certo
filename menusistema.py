def mostrar_menu():
    print("\n== MENU ==")
    print("-- 1 - Cadastrar Produto")
    print("-- 2 - Consultar Produto")
    print("-- 0 - Sair")

def mostrar_mensagem():
    print("Seja Bem-Vindo!")

def mensagem_sair():
    print("Encerrando...")

def mensagem_erro():
    print("Opção inválida, entre com uma opção válida.")

def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco_valido = False
    while not preco_valido:
        preco = float(input("Preço do produto (maior que zero): "))
        if preco > 0:
            preco_valido = True
        else:
            print("Preço inválido. Digite um valor maior que zero.")
    produtos.append((nome, preco))
    print("Produto cadastrado com sucesso!")

def consultar_produto(produtos):
    nome_busca = input("Digite o nome do produto: ")
    encontrado = False
    i = 0
    while i < len(produtos):
        item = produtos[i]
        if item[0] == nome_busca:
            print(f"Produto encontrado: {item[0]} - R$ {item[1]:.2f}")
            encontrado = True
        i += 1
    if not encontrado:
        print("Produto não encontrado.")

mostrar_mensagem()
produtos = []
continuar = True

while continuar:
    mostrar_menu()
    opcao = input("Entre com a opção desejada = ")
    
    if opcao == "1":
        cadastrar_produto(produtos)
    elif opcao == "2":
        consultar_produto(produtos)
    elif opcao == "0":
        mensagem_sair()
        continuar = False
    else:
        mensagem_erro()
