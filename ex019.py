# Um professor que sortear um dos seus quatro alunos para apagar o quadro.
#Faça um prograama que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
laco = 'S'
alunos = []
while True != 'S':
    al = input('Digite o nome do aluno: ').upper()
    alunos.append(al)
    if al == 'S':
        break
aluno = random.choice(alunos)
print(50*'*')
print('O VENCEDOR FOI'.center(50))
print(50*'-')
print(aluno.center(50))
print(50*'-')
print(50*'*')

