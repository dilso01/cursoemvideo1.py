'''Crie um programa que leia varios numero inteiros pelo teclado. no final da
execução, mostre a media entre os valores e qual foi o maior e o menor número
digitado, o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores'''
media = 0
maior = 0
menor = 0
soma = 0
cont = 0
laco = 'S'
while laco in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    laco = input('Quer continuar? [S/N]').upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')