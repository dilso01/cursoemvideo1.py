# faça um programa que leia um numeor do 0 a 9999, mostre na tela
# cada um dos digitos separados
#
# ex digite um numero:1834
# unidade 4
# dezenas 3
# centena 8
# milhar 1
num = int(input('Digite um numero de 0 ate 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
