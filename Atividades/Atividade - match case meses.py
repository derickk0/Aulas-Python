import os
os.system("cls || clear")

while True:
    numero = int(input("Digite o número desejado: "))

    match(numero):
        case 1:
            os.system("cls || clear")
            print("Janeiro")
            break
        case 2:
            os.system("cls || clear")
            print("Fevereiro")
            break
        case 3:
            os.system("cls || clear")
            print("Março")
            break
        case 4:
            os.system("cls || clear")
            print("Abril")
            break
        case 5:
            os.system("cls || clear")
            print("Maio")
            break
        case 6:
            os.system("cls || clear")
            print("Junho")
            break
        case 7:
            os.system("cls || clear")
            print("Julho")
            break
        case 8:
            os.system("cls || clear")
            print("Agosto")
            break
        case 9:
            os.system("cls || clear")
            print("Setembro")
            break
        case 10:
            os.system("cls || clear")
            print("Outubro")
            break
        case 11:
            os.system("cls || clear")
            print("Novembro")
            break
        case 12:
            os.system("cls || clear")
            print("Dezembro")
            break
        case _:
            os.system("cls || clear")
            input("Número inválido, tente novamente.")