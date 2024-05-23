import os
os.system("cls || clear")

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def quantidadePares(n1):
    contadorPar = 0
    for i in range(6):
        if (n1[i] % 2) == 0:
            contadorPar+=1
    return contadorPar

def quantidadeImpares(n1):
    contadorImpar = 0
    for i in range(6):
        if (n1[i] % 2) != 0:
            contadorImpar+=1
    return contadorImpar

numeros = []
contadorPar = 0
contadorImpar = 0

for i in range(6):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

logoSenai()
contadorPar = quantidadePares(numeros)
contadorImpar = quantidadeImpares(numeros)

print(f"Quantidade de números pares: {contadorPar}")
print(f"Quantidade de números ímpares: {contadorImpar}")