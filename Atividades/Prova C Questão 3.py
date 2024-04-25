import os
os.system("cls || clear")

nome: str
idade: int = 0
email: str
telefone: float = 0
opcao: int = 0

nome = (input("Digite o nome do usuário: "))
idade = int(input("Digite a idade do usuário: "))
email = (input("Digite o e-mail do usuário: "))
telefone = float(input("Digite o telefone do usuário: "))

os.system("cls || clear")
print("1 - Mostar nome e idade")
print("2 - Mostar nome e e-mail")
print("3 - Mostar nome e telefone")
print("4 - Mostar todas as informações")
print("0 - Sair do programa")

opcao = int(input("Digite o número correspondente à opção desejada: "))

match opcao:
    case 1:
        os.system("cls || clear")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
    case 2:
        os.system("cls || clear")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
    case 3:
        os.system("cls || clear")
        print(f"Nome: {nome}")
        print(f"Telefone: {telefone}")
    case 4:
        os.system("cls || clear")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Email: {email}")
        print(f"Telefone: {telefone}")
    case 0:
        print("Encerrando programa")
    case _:
        while (opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 0):
            os.system("cls || clear")
            print("Opção inválida")
            print("1 - Mostar nome e idade")
            print("2 - Mostar nome e e-mail")
            print("3 - Mostar nome e telefone")
            print("4 - Mostar todas as informações")
            print("0 - Sair do programa")
            opcao = int(input("Digite o número correspondente à opção desejada: "))

match opcao:
    case 1:
        os.system("cls || clear")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
    case 2:
        os.system("cls || clear")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
    case 3:
        os.system("cls || clear")
        print(f"Nome: {nome}")
        print(f"Telefone: {telefone}")
    case 4:
        os.system("cls || clear")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Email: {email}")
        print(f"Telefone: {telefone}")
    case 0:
        print("Encerrando programa")