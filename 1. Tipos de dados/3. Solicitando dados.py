# Solicitando dados para o usuário
import os

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

os.system('clear')
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")
print(f"Altura: {altura}")

