import os
import random

jogarnovamente = 's'
jogadas = 0
quemjoga = 2
maxjogadas = 9
vit = 'n'
velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    global jogadas
    os.system('cls')
    print('   0  1  2')
    print('0:  ' + velha[0][0] +"| "    + velha[0][1] +  '| '  + velha[0][2])
    print(14*'-')
    print('0:  ' + velha[1][0] + "| "    + velha[1][1] + '| '    + velha[1][2])
    print(14 * '-')
    print('0:  ' + velha[2][0] + "| "    + velha[2][1] + '| '    + velha[2][2])
    print('jogadas: ')

def jogadorjoga():
    global jogadas
    global quemjoga
    global vit
    global maxjogadas
    if quemjoga == 2 and jogadas < maxjogadas:
        l = int(input('linha..: '))
        c = int(input('coluna.: '))
        try:
            l = int(input('linha..: '))
            c = int(input('coluna.: '))
            while velha[l][c] != ' ':
                l = int(input('linha..: '))
                c = int(input('coluna.: '))
            velha[l][c] = 'X'
            quemjoga = 1
            jogadas += 1
        except:
            print('Linha e ou coluna inválida')
            #vit = 'n'
def cpujoga ():
    global jogadas
    global quemjoga
    global vit
    global maxjogadas
    if quemjoga == 1 and jogadas <maxjogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != ' ':
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
            velha[l][c] = 'O'
            quemjoga = 2
            jogadas += 1

while True:
    tela()
    jogadorjoga()
    cpujoga()
    #vv
