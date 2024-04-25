import os
os.system("cls || clear")

emailCorreto = "email@gmail"
senhaCorreta = "123"

email = str(input("Digite o seu e-mail: "))
senha = str(input("Digite a sua senha: "))

if (email == emailCorreto and senha == senhaCorreta):
    print("Bem-Vindo")
else:
    print("Login ou senha inválidos.")