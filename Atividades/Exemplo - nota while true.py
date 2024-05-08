import os
os.system("cls || clear")

while True:
    nota = float(input("Digite a nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida. A nota deve estar entre 0 e 10, tente novamente.")
    else:
        print("Nota válida: ", nota)
        break