import os
import sys
import time
os.system("cls || clear")

valorProduto = float(input("Digite o valor do produto: "))

while True:
    formaPagamento = input("Digite a forma de pagamento desejada (pix ou crédito): ")

    if formaPagamento != "pix" and formaPagamento != "credito":
        os.system("cls || clear")
        input("Opção inválida, digite uma das opções apresentadas ")
    else:
        break

if formaPagamento == "pix":
    valorFinal = valorProduto - (valorProduto * 0.10)
if formaPagamento == "credito":
    parcelas = int(input("Digite a quantidade de parcelas: "))
    valorPorParcela = valorProduto / parcelas

if formaPagamento == "pix":
    print(f"Valor do produto: {valorProduto}")
    print(f"Forma de pagamento: {formaPagamento}")
    print(f"Valor do desconto: {valorProduto * 0.10}")
    print(f"Total: {valorFinal}")

if formaPagamento == "CREDITO":
    print(f"Valor do produto: {valorProduto}")
    print(f"Forma de pagamento: {formaPagamento}")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor por parcela: {valorPorParcela}")
    print(f"Total: {valorProduto}")
