'''escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão:
-1 para binario
-2 para octal
-3 para hexadecimal'''
num = int(input('Digite um número: '))
print('''Escolha uma das base para conversão:
[ 1 ] para binario
[ 2 ] para octal
[ 3 ] para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para Octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} Convertido para Hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção inválida, Tente novamente')