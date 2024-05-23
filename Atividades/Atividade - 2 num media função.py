import os
os.system("cls || clear")

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def calculoMedia(n1,n2):
    return (n1 + n2) / 2

primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))

media = calculoMedia(primeiroNumero, segundoNumero)

print(f"Média: {media: .1f}")