import os
os.system("cls || clear")

def pareImpares(n1):
    contadorPar = 0
    contadorImpar = 0
    for i in range(QUANTIDADE_NUMEROS):
        if (n1[i] % 2) == 0:
            contadorPar+=1
        else:
            contadorImpar+=1
    print(f"Quantidade de números pares: {contadorPar}")
    print(f"Quantidade de números ímpares: {contadorImpar}")

QUANTIDADE_NUMEROS = 6
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

os.system("cls || clear")
for i in range(QUANTIDADE_NUMEROS):
    print(f"{i+1}º número: {numeros[i]}")

pareImpares(numeros)