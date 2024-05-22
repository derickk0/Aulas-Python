# Notas indefinidas
# digitar 0 = para e mostrar numeros e maior menor

import os
import sys
os.system("cls || clear")

QUANTIDADE_VALORES = 5
maiorValor = 0
menorValor = sys.maxsize
valores = []
contador = 0

for i in range(QUANTIDADE_VALORES):
    valores.append(float(input(f"Digite o {i+1}º valor: ")))

maiorValor = max(valores)
menorValor = min(valores)

os.system("cls || clear")
for i, valores in enumerate(valores):
    print(f"{i+1}º valor: {valores}")

print(f"Maior número: {maiorValor}")
print(f"Menor número: {menorValor}")
