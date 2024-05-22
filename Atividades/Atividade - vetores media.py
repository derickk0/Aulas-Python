import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
notas = []
media = 0
contador = 0

for i in range(QUANTIDADE_NOTAS):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))

os.system("cls || clear")
media = sum(notas) / QUANTIDADE_NOTAS
"""""
for i in range(QUANTIDADE_NOTAS):
    print(f"{i+1}ª nota: {notas[i]}")
"""""

for notas in notas:
    contador+=1
    print(f"{contador}ª nota: {notas}")

print(f"Média: {media: .1f}")