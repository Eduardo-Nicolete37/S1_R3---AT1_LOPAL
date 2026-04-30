import os
os.system('cls')

lista = [5, 7, 2, 9, 4, 1, 3]
print(f"A lista dada é: {lista}")
print("")
lista.sort()

print(f"O tamanho da lista é: {len(lista)}")
print(f"O maior valor da lista é: {max(lista)}")
print(f"O menor valor da lista é: {min(lista)}")
print(f"A soma de todas os valores da lista é: {sum(lista)}")
print(f"A lista em ordem CRESCENTE é {lista}")
lista.sort(reverse=True)
print(f"A lista em ordem CRESCENTE é {lista}")
