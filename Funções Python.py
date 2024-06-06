import os
import sys
os.system("cls || clear")

# Média
def mediar(n1,n2):
    media = n1 / n2
    print(f"Média: {media: .1f}")

# Média com situação
def mediarSituacao(n1,n2):
    media = n1 / n2
    print(f"Média {media: .1f}")
    if (media > 7):
        print("Aprovado")
    if (media < 7 and media >= 5):
        print("Recuperação")
    if(media < 5):
        print("Reprovado")

# Pares e impares
def pareImpares(n1):
    contadorPar = 0
    contadorImpar = 0
    for i in range(X):
        if (n1[i] % 2) == 0:
            contadorPar+=1
        else:
            contadorImpar+=1
    print(f"Quantidade de números pares: {contadorPar}")
    print(f"Quantidade de números ímpares: {contadorImpar}")

# Pares e impares entre x e y
def pareImparesXY(n1,n2):
    contadorPar = 0
    contadorImpar = 0
    for i in range(n1,n2):
        if (i % 2) == 0:
            contadorPar+=1
        else:
            contadorImpar+=1
    print(f"Quantidade de números pares: {contadorPar}")
    print(f"Quantidade de números ímpares: {contadorImpar}")

# Tabuada entre x e y
def tabuadaXY(n1):
    for i in range(10):
        print(f"{n1} x {i+1} = {n1 * (i+1)}")

# MaiorMenor
def maiorMenor(n1):
    maiorNumero = 0
    menorNumero = sys.maxsize

    maiorNumero = max(n1)
    menorNumero = min(n1)
    print(f"Maior número: {maiorNumero}")
    print(f"Menor número: {menorNumero}")