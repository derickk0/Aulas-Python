import os
os.system("cls || clear")

nota = 0
notas = []

for i in range(3):
    nota = input("Digite uma nota: ")
    notas.append(nota)

for i in range(3):
    print(f"Nota {i + 1}: {notas[i]}")