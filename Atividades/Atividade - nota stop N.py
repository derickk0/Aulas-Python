import os
os.system("cls || clear")

opcao = "S"
soma = 0
contador = 0

notas = float(input("Digite a primeira nota: "))
soma+=notas
contador+=1

while (opcao == "S"):
    opcao = str(input("Deseja inserir outra nota? ('S' para sim | 'N' para não) "))
    opcao = opcao.upper()

    if (opcao == "S"):
        notas = float(input("Digite a próxima nota: "))
        soma+=notas
        contador+=1
    if (opcao == "N"):
        os.system("cls || clear")
        media = soma / contador
        print(f"Média:{media: .1f}")
        print(f"Quantidade de loops: {contador - 1}")
        break
    if (opcao != "S" and opcao != "N"):
        print("Opção inválida")
        opcao = "S"