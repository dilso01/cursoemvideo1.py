'''Crie um programa que leia vários números inteiros pelo teclado. o
programa só vai parar quando o usuário digitar o valor 999, que
é a condição de parada. no final mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)'''
cont = 0
num = int(input('Digite um número: '))
total = 0
while num != 999:
    if num != 999:
        total += num
        cont += 1
        num = int(input('Digite um número: '))
    elif num == 999:
        break
print(f'Você digitou {cont} números e a soma entre eles é {total}.')