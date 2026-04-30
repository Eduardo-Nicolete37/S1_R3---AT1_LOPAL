import os
os.system('cls')

limite = int(input("Quantos números da Sequência de Fibonacci você quer ver: "))

anterior = 0
atual = 1
count = 0
while count != limite:
    count += 1
    if count == 1:
        anterior += atual
        atual = anterior
        print("O 1° valor da Sequência de Fibonacci é igual a 1")
    elif count == 2:
        print(f"O 2° valor da Sequência de Fibonacci é igual a {atual}")
    else:
        proximo = anterior + atual
        anterior = atual
        atual = proximo
        print(f"O {count}° valor da Sequência de Fibonacci é igual a {atual}")

