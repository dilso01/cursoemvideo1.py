'''Crie um programa que leia dois valores e
mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''
laco = '5'
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while True:
    operacao = input('''Escolha uma das opções de operadorades
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    : ''')
    if operacao == '5':
        break
    if operacao == '1':
        total = num1 + num2
        print(total)
    elif operacao == '2':
        total = num1 * num2
        print(total)
    elif operacao == '3':
        if num1 > num2:
            print(f'O número {num1} é maior que o {num2}')
        elif num2 > num1:
            print(f'O número {num2} é maior que o {num1}')
        else:
            print(f'Os números {num1} e {num2} são iguais')
    if operacao == '4':
        num1 = int(input('digite novos números: '))
        num2 = int(input('digite novos números: '))
    if operacao == '5':
        print('Operação finalizada')

print('~='*10)