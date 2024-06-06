import os
os.system("cls || clear")

def mediarSituacao(n1,n2):
    media = n1 / n2
    print(f"Média {media: .1f}")
    if (media > 7):
        print("Aprovado")
    if (media < 7 and media >= 5):
        print("Recuperação")
    if(media < 5):
        print("Reprovado")

QUANTIDADE_NUMEROS = 4
numeros = []
soma = 0

for i in range(QUANTIDADE_NUMEROS):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))
    if numeros[i] > 0:
        soma+=numeros[i]

os.system("cls || clear")
for i in range(QUANTIDADE_NUMEROS):
    print(f"{i+1}º número: {numeros[i]}")

mediarSituacao(soma,QUANTIDADE_NUMEROS)