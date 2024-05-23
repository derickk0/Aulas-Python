import os
os.system("cls || clear")

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def somar(numero):
    for i in range(10):
        print(f"{numero} x {i+1} = {numero * (i+1)}")

numero = float(input("Digite o número desejado: "))

print("=== Soma ===")
somar(numero)