''' Faça um programa que calcule os números ímpares qua são multiplos de 3 e
que se encontram no intervalo de 1 a 500'''

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print(soma)
print(cont)
