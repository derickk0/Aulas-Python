import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3

soma = 0
contador = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        notas = float(input(f"Digite a {i+1}ª nota: "))
        
        if (notas < 0 or notas > 10):
            print("Nota inválida, tente novamente.")
        else:
            soma+=notas
            break

media = soma / QUANTIDADE_NOTAS

os.system("cls || clear")
print(f"Média: {media: .1f}")
if (media > 7):
    print("Aprovado")
if (media >= 5 and media < 7):
    print("Recuperação")
if (media < 5):
    print("Reprovado")