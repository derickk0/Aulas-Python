import os
os.system("cls || clear")

nome = input("Digite o nome do indivíduo: ")
os.system("cls || clear")
print("F ou M")
sexo = input("Digite o sexo: ")
os.system("cls || clear")
print("CASADO(A), SOLTEIRO(A) ou VIÚVO(A)")
estadoCivil = input("Digite o seu estado civil: ")

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if (sexo == "F" and estadoCivil == "CASADA"):
    anosCasada = input("Digite quantos anos casada: ")

os.system("cls || clear")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estadoCivil}")

if (sexo == "F" and estadoCivil == "CASADA"):
    print(f"Anos de casada: {anosCasada}")