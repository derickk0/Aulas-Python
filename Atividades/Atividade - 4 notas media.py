import os
os.system("cls || clear")

soma = 0
contador = 0

for i in range(4):
    notas = float(input(f"Digite o {i+1}º número: "))

    soma+=notas
    contador+=1

media = soma / contador

os.system("cls || clear")
print(f"Média: {media}")