from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
laco = 'S'
while laco == 'S':
    if laco != 'S':
        break
    computador = randint(0, 2)
    print('''Escolha:
    \033[0::33m[ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2] TESOURA\033[0::33m''')
    jogador = int(input('Digite sua escolha: '))
    print('\033[0::35mJO\033[0::35m')
    sleep(1)
    print('   \033[0::35mKEN\033[0::35m')
    sleep(1)
    print('       \033[0::35mPO!!!\033[0::35m')
    sleep(0.5)
    print(f'O computador jogou {itens[computador]}')
    print(f'jogador jogou {itens[jogador]}')
    if computador == 0:
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('\033[0::36mJogador VENCE\033[0::36m')
        elif jogador == 2:
            print('\033[0::31mjogador PERDEU\033[0::31m')
        else:
            print('Jogada Inválida')

    elif computador == 1:
        if jogador == 0:
            print('\033[0::31mjogador PERDEU\033[0::31m')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('\033[0::36mJogador VENCE\033[0::36m')
        else:
            print('Jogada Inválida')

    elif computador == 2:
        if jogador == 0:
            print('\033[0::36mJogador VENCE\033[0::36m')
        elif jogador == 1:
            print('\033[0::31mjogador PERDEU\033[0::31m')
        elif jogador == 2:
            print('Empate')
        else:
            print('Jogada Inválida')