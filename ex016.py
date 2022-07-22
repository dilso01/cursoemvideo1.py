#crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
#ex: digite um 6.127
#o numro 6.127 tem tem a parte inteira 6
import math
# num = float(input("digite um numero: "))
# print(math.floor(num))
#
num = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
