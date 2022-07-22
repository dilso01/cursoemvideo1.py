#o mesmo professor do desafio anterior, quer sortear a ordem de apresentação de um trabalho
#dos alunos. Faça um programa que leia os nomes dos quatro alunos e mostre a ordem sorteada

from random import shuffle
alunos = []
for i in range(1, 5):
    al = input('Digite o nome do aluno: ').upper()
    alunos.append(al)
shuffle(alunos)
print('*'*20)
print(alunos)
print('*'*20)