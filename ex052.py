''' Faça um programa que leia um número inteiro e diga se ele
é ou nao um número primo'''
primo = int(input('Digite um número: '))
total = 0
for i in range(1, primo + 1):
    if primo % i == 0:
        print('\33[33m', end='')
        total += 1
    else:
        print('\33[31m', end='')
    print(f'{i}', end='')
print(f'\n\033[m0 número {primo}, foi divisível {total}, vezes.')
if total == 2:
    print('É um número Primo')
else:
    print('Não é Primo')
