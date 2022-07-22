''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA,
No final, mostre os 10 primeiros termos dessa progressão.'''

i = int(input('Inicio: '))

p = int(input('Passo: '))
f = i + (11 - 1) * p
for j in range(i, f, p):
    print(j, end=' -> ')
print('Acabou')