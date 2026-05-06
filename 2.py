import os
os.system('cls')

first = float(input("Por favor, nos diga o 1° digito: "))
second = float(input("Agora, nos diga o 2° digito: "))
third = float(input("E por último, nos diga o 3° digito: "))

lista = [first, second, third]


print(f"O maior dos três é: {lista[2]}")
print(f"Já o menor é: {lista[0]}")
