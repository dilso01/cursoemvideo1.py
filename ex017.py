#faça um programa que leia o comprimento do cateto oposto e do cateto adjancente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa.
#
import math
oposto = float(input('digite o valor do cateto oposto: '))
adjacente = float(input('digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('com o calculo entre catedo oposto {} e do cateto adjacente {} a sua hipotenusa é {:.2f}'.format(oposto, adjacente, hipotenusa ))