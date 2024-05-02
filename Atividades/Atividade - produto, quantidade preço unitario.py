import os
os.system("cls || clear")

nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
precoUnitario = float(input("Digite o preço unitário do produto: "))

total = quantidade * precoUnitario

if (quantidade <= 5):
    totalDesconto = total - (total * 0.02)
if (quantidade > 5 and quantidade <= 10):
    totalDesconto = total - (total * 0.03)
if (quantidade > 10):
    totalDesconto = total - (total * 0.05)

print(f"Nome do produto: {nome}")
print(f"Total sem desconto: {total}")
print(f"Total com desconto: {totalDesconto}")