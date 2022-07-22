'''Faça um programa que leia o peso de 5 pessoas e no
final diga qual o maior e o menor peso'''
peso_menor = 0
peso_maior = 0
for i in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if i == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print(f'O peso maior é {peso_maior}')
print(f'O peso Menor é {peso_menor}')

