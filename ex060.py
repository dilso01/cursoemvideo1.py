'''Faça um programa que leia um número qualquer e mostre o seu fatorial
ex= 5! = 5x4x3x2x1 = 120'''

linha = ('~='*20)

print(linha)
numero = int(input("Fatorial de: ") )
print(linha)

resultado=1
for i in range(1,numero+1):
    resultado *= i

print(resultado)
print(linha)