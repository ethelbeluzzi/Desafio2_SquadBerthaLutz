"""
Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.
"""

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Infrome o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"O maior número é o {numero1}.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O maior número é o {numero2}.")
else:
    print(f"O maior número é o {numero3}.")