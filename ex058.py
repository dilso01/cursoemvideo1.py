''' Melhore o jogo do desafio 028 onde o computador vai pensar
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar ate acertar
mostrando no final quantos palpites foram necessários para vencer'''

# import random
# num = int(input('Digite um número entre 0 e 10: '))
# sorteado = [random.randint(0, 10)]
#
# while num != sorteado:
#     num = int(input('Digite um número entre 0 e 10: '))
#     if num == sorteado:
#         print('PARABENS VOCÊ GANHOU')
#         break
#     else:
#         print('TENTE NOVAMENTE')
#
#     print(sorteado)

from random import randint

computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um número entre 0 e 10')
print('Será que você consegue acertar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente ,mais uma vez.")
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentivas, Parabéns!!!')
