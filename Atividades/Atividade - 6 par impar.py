import os
import sys
os.system("cls || clear")

QUANTIDADE_VALORES = 6
maiorValor = 0
menorValor = sys.maxsize
valores = []
contadorPar = 0
contadorImpar = 0

for i in range(QUANTIDADE_VALORES):
    valores.append(float(input(f"Digite o {i+1}º valor: ")))

    if (valores[i] % 2) == 0:
        contadorPar+=1
    else:
        contadorImpar+=1

os.system("cls || clear")
for i, valores in enumerate(valores):
    print(f"{i+1}º valor: {valores}")

print(f"Quantidade de números pares: {contadorPar}")
print(f"Quantidade de números ímpares: {contadorImpar}")

