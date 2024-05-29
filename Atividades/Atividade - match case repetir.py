import os
os.system("cls || clear")

resultado = 0

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
operador = input("Digite o operador (+ - * /): ")

while (resultado == 0):

    match(operador):
        case "+":
            resultado = a + b
        case "-":
            resultado = a - b
        case "*":
            resultado = a * b
        case "/":
            resultado = a / b
        case _:
            os.system("cls || clear")
            print("Operador inválido")
            operador = input("Digite um operador válido (+ - * /): ")

os.system("cls || clear")
print(f"Resultado: {resultado}")