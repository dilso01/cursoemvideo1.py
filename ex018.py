#faca um programa que leia um anguloe mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
an = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))