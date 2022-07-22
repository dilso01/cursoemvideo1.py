# desnvolva um programa que leia o comprimento de três retas e dia ao usuário
# se elas podem ou não formar um triângulo.
r1 = float(input('Digite o primeiro parâmetro: '))
r2 = float(input('Digite o segundo parâmetro: '))
r3 = float(input('Digite o terceiro parâmetro: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os parâmetros digitados formam um triângulo!')
else:
    print('Os parâmetros digitados não formam um triângulo')