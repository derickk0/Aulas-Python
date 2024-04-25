import os
os.system("cls || clear")

numeros = []
maiorNumero: int = 0
menorNumero: int = 999

for i in range(6):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

for i in range(6):
    if numeros[i] > maiorNumero:
        maiorNumero = numeros[i]
    if numeros[i] < menorNumero:
        menorNumero = numeros[i]

os.system("cls || clear")
for i in range(len(numeros)):
    print(f"{i+1}º número: {numeros[i]}")
print("==================")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")