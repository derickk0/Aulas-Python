import os
os.system("cls || clear")

size: int = 5 ## Variável para definir quantidade de valores ("#define SIZE" em C)

numeros: int = []
contadorPar: int = 0
contadorImpar: int = 0

for i in range(size):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

    if numeros[i] % 2 == 0:
        contadorPar+=1
    else:
        contadorImpar+=1

os.system("cls || clear")

for i in range(size):
    print(f"{i+1}º número: {numeros[i]}")

print("======================================")
print(f"Quantidade de números pares: {contadorPar}")
print(f"Quantidade de números ímpares: {contadorImpar}")

