import os
os.system("cls || clear")

opcao = "S"
soma = 0
contador = 0

notas = float(input("Digite a primeira nota: "))
soma+=notas
contador+=1

while (opcao == "S"):
    os.system("cls || clear")
    print("S - Inserir mais uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular a média aritmética das notas informadas")
    opcao = str(input("Digite a letra correspondente a opção desejada: "))
    opcao = opcao.upper()

    if (opcao == "S"):
        notas = float(input("Digite a próxima nota: "))
        soma+=notas
        contador+=1
    if (opcao == "P"):
        os.system("cls || clear")
        print(f"Quantidade de notas inseridas: {contador}")
        break
    if (opcao == "N"):
        os.system("cls || clear")
        media = soma / contador
        print(f"Média:{media: .1f}")
        break
    if (opcao != "S" and opcao != "N" and notas != "P"):
        print("Opção inválida")
        opcao = "S"