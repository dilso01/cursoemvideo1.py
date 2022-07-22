# Crie um programa que leia quanto uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
# considere US$1.00=R$3.27

real = float(input('Quantos Reais você tem na carteira: '))
dolar = real / 3.27
print('Vpcê tem R${:.2f} e pode comprar US${:.2f}'.format(real, dolar))