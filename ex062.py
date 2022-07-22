'''Melhore o desafio 61, perguntando mais quantos termos ele quer mostrar,
o programa encerra quando ele disser que quer mostrar o termos '''

print('Gerador de PA')
print('~=' *10)
i = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão da PA: '))
termo = i
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += r
        cont +=1

    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão mostrada com {total} termos')
print('***FIM***')
