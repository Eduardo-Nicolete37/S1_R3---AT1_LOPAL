import os
os.system('cls')

name = input("Por favor, escreva seu nome: ")

for i in range(1, len(name) + 1):
    print(name[:i])
