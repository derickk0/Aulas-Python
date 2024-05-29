import os
os.system("cls || clear")


while True:
    os.system("cls || clear")
    print("1 - Picanha - 25 conto")
    print("2 - Lasanha - 20 conto")
    print("3 - Strogonoff - 18 conto")
    print("4 - Bife Acebolado - 15 conto")
    print("5 - Pão com ovo - 5 conto")
    opcao = int(input("Digite número correspondente ao prato desejado: "))
    
    match(opcao):
        case 1:
            os.system("cls || clear")
            print("Picanha - 25 conto")
            break
        case 2:
            os.system("cls || clear")
            print("Lasanha - 20 conto")
            break
        case 3:
            os.system("cls || clear")
            print("Strogonoff - 18 conto")
            break
        case 4: 
            os.system("cls || clear")
            print("Bife Acebolado - 15 conto")
            break
        case 5:
            os.system("cls || clear")
            print("Pão com ovo - 5 conto")
            break
        case _:
            os.system("cls || clear")
            input("Opção inválida, tente novamente. ")
