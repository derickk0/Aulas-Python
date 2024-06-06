import os
import sys
os.system("cls || clear")

def maiorMenor(n1):
    maiorNumero = 0
    menorNumero = sys.maxsize
        
    maiorNumero = max(n1)
    menorNumero = min(n1)
    print(f"Maior número: {maiorNumero}")
    print(f"Menor número: {menorNumero}")

QUANTIDADE_NUMEROS = 5
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numeros.append(input(f"Digite o {i+1}º número: "))


os.system("cls || clear")
for i in range(QUANTIDADE_NUMEROS):
    print(f"{i+1}º número: {numeros[i]}")

maiorMenor(numeros)