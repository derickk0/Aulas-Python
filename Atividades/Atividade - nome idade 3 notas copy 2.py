import os
os.system("cls || clear")

nome = str
primeiraNota = float
segundaNota = float
terceiraNota = float

print("=== Solicitando dados ===")
nome = str (input("Digite o nome: "))
idade = int (input("Digite a idade: "))
primeiraNota = float (input("Digite a sua Primeira nota: "))
segundaNota = float (input("Digite a sua Segunda nota: "))
terceiraNota = float (input("Digite a sua Terceira nota: "))

media = int (primeiraNota + segundaNota + terceiraNota) / 3

print(f"=== Exibindo Resultados ===")
print(f"Primeira Nota: {primeiraNota}")
print(f"Segunda Nota: {segundaNota}")
print(f"Terceira Nota: {terceiraNota}")
print(f"resultado da média: {media}")

if (media >= 7):
    print("Aprovado")
if (media >= 5 and media < 7):
    print("Recuperação")
if (media < 5):
    print("Reprovado")

print("FIM")