import os
os.system("cls || clear")

primeiroValor = int(input(f"Digite o primeiro valor: "))
segundoValor = int(input(f"Digite o segundo valor: "))

media = (primeiroValor + segundoValor) / 2
soma = primeiroValor + segundoValor
multiplicacao = primeiroValor * segundoValor

maiorValor = max(primeiroValor, segundoValor)
menorValor = min(primeiroValor, segundoValor)

""" 
if (primeiroValor > segundoValor):
    maiorValor = primeiroValor
    menorValor = segundoValor
else:
    maiorValor = segundoValor
    menorValor = primeiroValor
"""
     
print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {multiplicacao}")
print(f"Maior valor: {maiorValor}")
print(f"Menor valor: {menorValor}")