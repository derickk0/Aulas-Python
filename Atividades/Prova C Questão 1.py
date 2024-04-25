import os
os.system("cls || clear")

numeros = []
contadorPar: int = 0
contadorImpar: int = 0

for i in range(6):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))
    if numeros[i] % 2 == 0:
        contadorPar+=1
    else:
        contadorImpar+=1

os.system("cls || clear")
for i in range(len(numeros)):
    print(f"{i+1}º número: {numeros[i]}")
print("=========================")
print(f"Quantidade de números pares: {contadorPar}")
print(f"Quantidade de números ímpares: {contadorImpar}")