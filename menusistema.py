def mostrar_menu():
    print("==MENU==")
    print("-- 1 - Ver Mensagem ")
    print("-- 0 - Sair ")

mostrar_menu()

def mostrar_mensagem():
    print("Seja Bem Vindo ")

def mensagem_sair():
    print("Encerrando...")

def mensagem_erro():
    print("Opção invalida, entre com uma opção valida ")

opcao = input("Entre com a opcao desejada = ")

if opcao == "1":
    mostrar_mensagem()    

if opcao == "0":
    mensagem_sair()

if opcao != "1" and opcao != "0":
    mensagem_erro()

