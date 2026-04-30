import os
os.system('cls')
tabuada = int(input("Escolha uma tabuada de 1 a 10: "))
os.system('cls')
for i in range(1, 11):
    tabuada_new = i * tabuada
    print(f"O {i}° número dessa tabuada é {tabuada_new}") 