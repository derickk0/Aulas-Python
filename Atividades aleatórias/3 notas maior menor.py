import os
os.system("cls || clear")

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

QUANTIDADE_NOTAS = 3

notas = []
soma = 0
confirmar = 0

for i in range(QUANTIDADE_NOTAS):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))
    if (notas[i] < 0 or notas[i] > 10):
        while (notas[i] < 0 or notas[i] > 10):
            input("Nota inválida, tente novamente")
            os.system("cls || clear")
            notas.append(float(input(f"Digite a {i+1}ª nota: ")))
    else:
        soma+=notas[i]
        

for i in range(QUANTIDADE_NOTAS):
    print(f"{i+1}ª nota: {notas[i]}")

mediarSituacao(soma,QUANTIDADE_NOTAS)