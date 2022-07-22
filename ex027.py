# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o ultimo nome separadamente.
#
# ex: Ana Maria de Souza
# primeiro=Ana
# último=Souza

nome = str(input('Digite seu nome: ')).upper().strip()
n = nome.split()
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n)-1]}')