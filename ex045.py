'''Crie um programa que faça o computador jogar Jokenpô com você'''
import random
from random import randint
import time

linha = '~~'*20
def jogada(a):
    if a == 1:
        return 'pedra'
    elif a == 2:
        return 'papel'
    else:
        return 'tesoura'
# jogador = 0
# pc = 0
print(linha)
nome = 'Isabella'  # input('Digite seu nome: ')
print(linha)
print(f'Olá {nome}, Vamoas jogar Jókempo')
print(linha)
jogador = 0
pc = 0
empate = 0
while True:
    if jogador == 3 or pc == 3:
        break
    print('Escolha sua jogada')
    print(linha)
    escolha = int(input(' 1 - Digite 1 para escolher Pedra \n 2 - Digite 2 para escolher Papel\n 3 - Digite 3 para escolher Tesoura'))
    jogada(escolha)
    print(linha)
    pc = random.randint(1, 3)
    jogada(pc)
    a = jogada(escolha)
    b = jogada(pc)
    print(linha)
    print(f'{nome} SUA ESCOLHA FOI:\n{jogada(escolha).upper().center(40)}')
    print(linha)
    print('~='*20)
    print(f'ESCOLHA DO COMPUTADOR FOI:\n{jogada(pc).upper().center(40)}')
    print('~='*20)
    print('xX'*20)
    if a == 'pedra' and b == 'papel':
        pc += 1
        print('Computador venceu, tente novamente !!!')

    elif a == 'pedra' and b == 'tesoura':
        jogador += 1
        print(f'Parábens {nome}, Você Venceu !!!')

    elif a == 'papel' and b == 'pedra':
        pc += 1
        print(f'Parábens {nome}, Você Venceu !!!')

    elif a == 'papel' and b == 'tesoura':
        pc += 1
        print('Computador venceu, tente novamente !!!')

    elif a == 'tesoura' and b == 'pedra':
        jogador += 1
        print('Computador venceu, tente novamente !!!')

    elif a == 'tesoura' and b == 'papel':
        jogador += 1
        print(f'Parábens {nome}, Você Venceu !!!')

    elif a == b:
        empate += 1
        print('EMPATOU'.center(40))


if jogador > pc:
    print('Você Ganhou!!! PARÁBENS!!!')
    print(f'placar foi:\n{nome} = {jogador}\nX\n Computador {pc}'.center(40))
    print(f'Teve {empate} Empates')

elif pc > jogador:
    print('Você Perdeu!!! Tente Novamente!!!')
    print(f'placar foi:\n{nome}={jogador}\n     X\nComputador={pc}'.center(40))
    print(f'Teve {empate} Empates')

