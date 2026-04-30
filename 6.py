number = int(input("Qual o número que deseja analisar: "))

number_save = number
if number < 0 or number == 1:
    print("Por definição, seu número NÃO é PRIMO")
else:
    rest = 2
    while number != 1:
        number = number % rest
        rest += 1
    if rest != number_save:
        print(f"Seu número não é PRIMO, ele é divisível por {rest}")
    else:
        print("Seu número é PRIMO, sendo somente dívisivel por ele mesmo e 1!")