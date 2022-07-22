# escreva um programa que faça o computador 'pensar' em numero inteiro entre 0 e 5
# e paçe para o usuario tentar descobrir qual foi o número escolhido
# pelo computador.
# > o programa deverá escrever na tela se o usuário venceu ou perdeu
import random
num = int(input('Digite um número entre 0 e 5: '))
sorteado = [random.randint(0, 5)]
if num == sorteado:
    print('PARABENS VOCÊ GANHOU')
else:
    print('TENTE NOVAMENTE')
print(sorteado)