import os
os.system("cls || clear")

operador = 0

numero = input("Digite o número correspondente ao dia desejado: ")

while ():
    match (numero):
        case 1:
            operador = 1
            print("1 - Domingo")
        case 2:
            print("2 - Segunda")
            operador = 1
        case 3:
            print("3 - Terça")
            operador = 1
        case 4:
            print("4 - Quarta")
            operador = 1
        case 5:
            print("5 - Quinta")
            operador = 1
        case 6:
            print("6 - Sexta")
            operador = 1
        case 7:
            print("7 - Sábado")
            operador = 1
        case _:
            os.system("cls || clear")
            print("Número inválido")
            numero = input("Digite um número correspondente ao dia desejado: ")