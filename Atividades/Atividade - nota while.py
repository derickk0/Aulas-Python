import os
os.system("cls || clear")

nota = float(input("Digite a nota: "))

while (nota < 0 or nota > 10):
    os.system("cls || clear")
    nota = 0
    print("Nota inválida")
    nota = float(input("Digite uma nota válida: "))

os.system("cls || clear")
print(f"Nota: {nota}")

nota: int = 0