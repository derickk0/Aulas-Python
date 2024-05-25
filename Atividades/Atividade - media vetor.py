import os
os.system("cls || clear")

def mediarSituacao(n1,n2):
    media = n1 / n2
    print(f"Média:{media: .1f}")
    if (media > 7):
        print("Aprovado")
    if (media < 7 and media >= 5):
        print("Recuperação")
    if(media < 5):
        print("Reprovado")

notas: float = []
soma: float = 0
quantidadeNotas = 0

for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))

    soma+=notas[i]
    quantidadeNotas+=1

os.system("cls || clear")
for i in range(4):
    print(f"{i+1}ª nota: {notas[i]}")

mediarSituacao(soma,quantidadeNotas)