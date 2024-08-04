# Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []

for i in range(5):
    print(f"Aluno {i + 1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    medias.append(media)

alunos_aprovados = len([media for media in medias if media >= 7.0])
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
