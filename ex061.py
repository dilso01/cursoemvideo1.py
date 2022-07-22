'''Refaca o desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while'''

print('Gerador de PA')
print('~=' *10)
i = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão da PA: '))
termo = i
cont = 1
while cont<= 10:
    print(f'{termo} -> ', end='')
    termo += r
    cont +=1

print('FIM')
