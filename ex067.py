'''Faça um programa que mostre a tabuada de vários números, um
de cada vez, para cada valor digitado pelo usuário. O programa será
interronpido quando o número solicitado for negativo'''
linha = ('-='*12)
print(linha)
print('Vamos Aprender a Tabuada')
print(linha)
num = int(input('Digite um número: '))
while num > 0:

    if num < 0:
        break

    else:
        print(f'Tabuada de {num}')
        for i in range(0, 11):
            total = num * i
            print(f'{num}  X  {i}   =  {total}')
        print(linha)
        num = int(input('Qual tabuada você quer? '))
        print(linha)
print('Fim da execução')
print('X'*20)