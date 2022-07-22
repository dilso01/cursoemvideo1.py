'''Refaça o desafio 035 dos triangulos, acressentando o recurso
de mostrar que tipo de triangulo será formado
>equilátero: todos os lados iguai
>isóceles: dois lados iguais
>escaleno: todos os lados diferentes'''

l1 = int(input('Solicite a primeura medida: '))
l2 = int(input('solicite a segunda medida: '))
l3 = int(input('solicite a terceira medida: '))

if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
    print('Não é um triangulo')
elif l1 == l2 == l3:
    print('Sim é um Triangulo Equilatero')
elif l1 != l2 != l3:
    print('Sim é um Triangulo Escaleno')
else:
    print('Sim é um Triangulo Isóceles')