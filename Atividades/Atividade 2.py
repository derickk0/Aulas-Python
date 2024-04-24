import os
os.system("cls ||clear")

primeiroNumero = float (input("Digite o primeiro número: "))
segundoNumero = float (input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero

os.system("cls ||clear")
print(f"Soma: {soma}") 
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")