# Notas indefinidas
# digitar 0 = para e mostrar numeros e maior menor

import os
import sys
os.system("cls || clear")

QUANTIDADE_VALORES = 5
maiorValor = 0
menorValor = sys.maxsize
valores = []
valor = 1
enumerar = 0

while (valor != 0):
    enumerar+=1
    valor = float(input(f"Digite o {enumerar}º valor: "))
    if (valor != 0):
        valores.append(float(valor))

        maiorValor = max(valores)
        menorValor = min(valores)

os.system("cls || clear")
for i, valor in enumerate(valores):
    print(f"{i+1}º número: {valor}")

print(f"Maior valor: {maiorValor}")
print(f"Menor valor: {menorValor}")