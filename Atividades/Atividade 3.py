import os
os.system("cls ||clear")

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

media = (primeiraNota + segundaNota) / 2

os.system("cls ||clear")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {primeiraNota}")
print(f"Segunda nota: {segundaNota}")
print(f"Média: {media}")
