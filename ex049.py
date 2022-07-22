''' Refaça o desafio 09, mostrando a tabuada de um número
que o usuario escolher, só que agora utilizando um laço for'''

linha = ('-='*12)
print(linha)
print('Vamos Aprender a Tabuada')
print(linha)
tabu = int(input('Digite o número: '))
for i in range(0, 11):
    print(f'{tabu} X {i} = {tabu*i}')
print(linha)