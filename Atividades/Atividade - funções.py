import os

# Função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

# Funções com retorno
def somar(n1, n2):
    resultado = n1 + n2 # Pode-se utilizar variável ou não.
    return resultado # Váriável recomandada quando a operação é grande

def subtrair(n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

# Chamando as funções 
logoSenai()
primeiroNumero = int(input("Digite o primeiro número: ")) 
logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
subtracao = subtrair(primeiroNumero, segundoNumero)
multiplicacao = multiplicar(primeiroNumero, segundoNumero)
divisao = dividir(primeiroNumero, segundoNumero)

logoSenai()
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")