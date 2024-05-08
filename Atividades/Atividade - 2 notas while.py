import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 2

soma = 0
contador = 0

for i in range(QUANTIDADE_NOTAS):
    notas = float(input(f"Digite a {i+1}ª nota: "))

    while (notas < 0 or notas > 10):
        os.system("cls || clear")
        notas = 0   
        notas = float(input(f"Nota inválida, digite uma nota válida: "))

    soma+=notas

media = soma / QUANTIDADE_NOTAS

print(f"Média: {media: .1f}")