import os
os.system('cls')

number = int(input("Digite o número que deseja ver o fatorial: "))
fat = 1
for i in range(1, number + 1):
    fat *= i

print(f"O fatorial de {number} é: {fat}")