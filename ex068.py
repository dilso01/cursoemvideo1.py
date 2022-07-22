'''Faça um programa que jogue par ou impar com o computador.
O jogo so será interrompido quando o jogador perder,
mostrando o total de vitória consecutivas que ele conquistou no final do jogo'''
from random import randint


def par_impar(a):
    if a % 2 != 0:
        return 1
    else:
        return 2


jPoui = input('Par ou Impar P/I').upper()
while True:
    if jPoui == 'P':
        print('Joagador escolheu PAR')
        jPoui = 2
        break
    elif jPoui == 'I':
        print('Jogador escolheu IMPAR')
        jPoui = 1
        break
    else:
        jPoui = input('Par ou Impar P/I').upper()

escolha_pc = randint(1, 2)
print(escolha_pc)
if escolha_pc == 1:
    escolha_pc = 1
    print('Computador escolheu IMPAR')
else:
    escolha_pc = 2
    print('Computador escolheu PAR')



#
# jogador = int(input('Digite um número: '))
# comp = randint(0, 11)
# cond_vitoria = jogador + comp
# par_impar(cond_vitoria)
# print(cond_vitoria)