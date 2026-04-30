import os
os.system('cls')

first = float(input("Por favor, nos diga o 1° digito: "))
second = float(input("Agora, nos diga o 2° digito: "))
third = float(input("E por último, nos diga o 3° digito: "))

if first > third:
    first, third = third, first
elif first > second:
    first, second = second, first
elif second > third:
    second, third = third, second

print(f"O maior dos três é: {third}")
print(f"Já o menor é: {first}")