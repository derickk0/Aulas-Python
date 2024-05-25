import os
import sys
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5

def maiorMenor(n1):
    maiorNumero = 0
    menorNumero = sys.maxsize
    for i in n1:
        maiorNumero = max(n1)
        menorNumero = min(n1)
    print(f"Maior número: {maiorNumero}")
    print(f"Menor número: {menorNumero}")

def pareImparesXY(n1):
    contadorPar = 0
    contadorImpar = 0
    for i in range(5):
        if (n1[i] % 2) == 0:
            contadorPar+=1
        else:
            contadorImpar+=1
    print(f"Quantidade de números pares: {contadorPar}")
    print(f"Quantidade de números ímpares: {contadorImpar}")

numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

os.system("cls || clear")
for i in range(QUANTIDADE_NUMEROS):
    print(f"{i+1}º número: {numeros[i]}")

maiorMenor(numeros)
pareImparesXY(numeros)