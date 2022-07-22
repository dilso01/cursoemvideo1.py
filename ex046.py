'''Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogas de artifio, indo de 10 até 0, com um pausa de 1 segundo entre eles'''

from time import sleep

for i in range(10, -1, -1):
    sleep(1)
    print(i)
print('Feliz ano NOVO')