''' crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles, desconsiderando o flag'''

num = 0
cont = 0
total = 0
while num !=999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    else:
        total += num
        cont += 1

print(f'O total de números digitados foi {cont}, e a soma entre eles é {total}')