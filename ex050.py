'''desenvolva um programa que leia 6 números inteiros
e mostre a soma apenas dos números pares, se o valor for impar, desconsiderar'''
soma = 0
cont = 0
for i in range(0, 6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f' Você digitou {cont} números pares e a soma foi {soma}')
