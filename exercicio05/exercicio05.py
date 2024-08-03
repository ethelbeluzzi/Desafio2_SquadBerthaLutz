'''
5. Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno. equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
'''

lado1 = float(input("Qual o comprimento do primeiro lado de um triângulo? "))
lado2 = float(input("Qual o comprimento do segundo lado de um triângulo? "))
lado3 = float(input("Qual o comprimento do terceiro lado de um triângulo? "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")