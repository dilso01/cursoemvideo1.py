'''crie um programa que leia o ano de nascimento de 7 pessoas,
no final ele diga quantas ainda não atingiram a maioridade e quantas ja são maiores'''

maior = 0
menor = 0
ano = 2022
for i in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    if ano - nasc < 21:
        menor += 1
    else:
        maior += 1
print(f'temos {maior} pessoas maiores de idade e {menor} pessoas menor de idade.')