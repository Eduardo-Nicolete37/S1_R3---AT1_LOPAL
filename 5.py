import os
os.system('cls')

name = input("Por favor, digite seu nome: ")
if len(name) < 3:
    os.system('cls')
    print("ERRO! Nome inválido")
    name = input("Por favor, digite seu nome: ")

age = int(input("Agora, digite sua idade: "))
if age < 0 or age > 150:
    os.system('cls')
    print("ERRO! Idade inválida")
    age = int(input("Agora, digite sua idade: "))

wage = float(input("Digite o seu salário mensal: "))
if wage < 0:
    os.system('cls')
    print("ERRO! Salário inválida")
    age = float(input("Digite seu salário mensal: "))

print("Por favor, digite seu gênero")
print("M - Masculino")
print("F - Feminino")
gender = str(input("M/F: "))
while gender == "M" or gender == "m" or gender == "F" or gender == "f":
    break
else:
    os.system('cls')
    print("ERRO! Gênero inválido")
    print("Por favor, digite seu gênero")
    gender = str(input("(Masculino - M)/(Feminino - F): "))

print("E por último, digite seu estado cívil")
print("S - Solteiro")
print("C - Casado")
print("V - Viúvo")
print("D - Divorciado")
state = input("(S/C/V/D): ")
while gender == "s" or gender == "S" or gender == "c" or gender == "C" or gender == "v" or gender == "V" or gender == "d" or gender == "D":
    break
else:
    os.system('cls')
    print("ERRO! Estado cívil inválido")
    print("E por último, digite seu estado cívil")
    print("S - Solteiro")
    print("C - Casado")
    print("V - Viúvo")
    print("D - Divorciado")
    state = input("(S/C/V/D): ")

print("Informações válidas! Muito obrigado por sua atenção")