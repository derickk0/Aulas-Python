import os
os.system("cls || clear")

numeros: int = 0
quantidadeDeNumeros: int = 0
soma: int = 0
media: int = 0
i: int = 0

numeros = int(input(f"Digite o primeiro número: "))
if numeros < 0:
    while (numeros < 0):
        soma = 0
        quantidadeDeNumeros = 0

        numeros = int (input("Número inválido, digite um primeiro número positivo: "))
        soma+=numeros
        quantidadeDeNumeros+=1
else: 
    if numeros > 0:
        soma+=numeros
        quantidadeDeNumeros+=1

while (numeros >= 0):
    numeros = int(input(f"Digite o próximo número: "))

    if numeros > 0:
        soma+=numeros
        quantidadeDeNumeros+=1

media = soma / quantidadeDeNumeros

os.system("cls || clear")
print(f"Média: {media}")