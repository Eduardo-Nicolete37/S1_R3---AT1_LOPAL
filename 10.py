import os
os.system('cls')

password = "676767"

password_try = input("Por favor, digite a senha: ")

while password_try != password:
    print("ACESSO NEGADO! TENTE NOVAMENTE")
    password_try = input("Por favor, digite a senha: ")

print("ACESSO LIBERADO! Bem vindo!")