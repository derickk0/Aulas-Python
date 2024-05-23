import os
os.system("cls || clear")

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def inflacao10(n1):
    valorFinal = (n1 * 0.10) + n1
    return valorFinal

def inflacao20(n1):
    valorFinal = (n1 * 0.20) + n1
    return valorFinal

logoSenai()
valor = float(input("Digite o valor do produto: "))

if valor < 100:
    valorFinal = inflacao10(valor)
else:
    valorFinal = inflacao20(valor)

logoSenai()
print(f"Valor final: {valorFinal}")