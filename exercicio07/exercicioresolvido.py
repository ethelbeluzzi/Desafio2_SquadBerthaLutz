"""
Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
"""
# dado que:
# criança = -11 anos
# adolescente = 12 a 18 anos
# adulto = 19 a 59 anos
# idoso = +60 

idade = int(input("Quantos anos você tem?"))

if idade <= 11:
    print(f"Você tem {idade}. Você é criança!")
elif idade <= 18:
    print(f"Você tem {idade}. Você é adolescente!")
elif idade <= 59:
    print(f"Você tem {idade}. Você é adulto!") 
else:
    print(f"Você tem {idade}. Você é idoso!")