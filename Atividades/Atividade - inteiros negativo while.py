import os
os.system("cls || clear")

soma = 0
contador = 0

valores = int(input("Digite o primeiro valor: "))

while (valores >= 0):
    valores = int(input("Digite o próximo número: "))
    if (valores > 0):
        soma+=valores
        contador+=1

media = soma / contador

os.system("cls || clear")
print(f"Média: {media}")