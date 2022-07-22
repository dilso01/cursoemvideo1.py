'''escreva um programa que leia dois números inteiros e
compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais'''
num = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
if num > num2:
    print(f'O primeiro número {num} é maior que o segundo número {num2}')
elif num2 > num:
    print(f'O segundo número {num2} é maior que o primeiro número {num}')
else:
    print(f'Os dois números {num}, {num2} são iguais')