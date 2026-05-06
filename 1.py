import os
os.system('cls')

print("Você quer ver os números pares ou ímpares?")
option = input("(Ímpar - I)/(Par - P): ")

if option == "P" or option == "p":
    print("Números pares: ")
    for i in range(0, 101, 2):
        print(i)
elif option == "I" or option == "i":
    print("Números ímpares: ")
    for i in range(1, 101, 2):
        print(i)
        
