'''Escreva um programa que lê um número inteiro qualquer e mostre na tela os
primeiros elementos de uma sequência de fibonacci. '''

linha = '-'*22
print(linha)
print('Sequência de Fibonicci')
print(linha)
n = int(input('Quantos termos você que mostrar? '))
t1 = 0
t2 = 1
print('~'*22)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    cont += 1
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3


print(' -> FIM')
print(linha)
