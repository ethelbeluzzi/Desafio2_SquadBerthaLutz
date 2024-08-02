# 1. Faça um Programa que peça dois números e imprima o maior deles.
# Pedir ao usuário para inserir o primeiro número
while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")

# Pedir ao usuário para inserir o segundo número
while True:
    try:
        numero2 = int(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")

# Comparar os números e imprimir o maior
if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os números são iguais.")
