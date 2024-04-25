import os
os.system("cls || clear")

nome = str
primeiraNota = float; segundaNota = float; terceiraNota = float; quartaNota = float
media = float

nome = input("Digite o nome do aluno: ")
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))
terceiraNota = float(input("Digite a terceira nota: "))
quartaNota = float(input("Digite a quarta nota: "))

media = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4

os.system("cls || clear")
print(f"Nome: {nome}")
print(f"Primeira nota: {primeiraNota}")
print(f"Segunda nota: {segundaNota}")
print(f"Terceira nota: {terceiraNota}")
print(f"Quarta nota: {quartaNota}")
print(f"Média: {media}")
print("======================")
if media > 7:
    print("Aprovado")
if media >= 5 and media < 7:
    print("RecuRecu")
if media < 5:
    print("Reprovado")