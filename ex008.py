#Escreva um programa que de o valor em metros e o exiba convertido em centimetros e milimitros
m = float(input('digite a medida: '))
cm = m * 100
mm = m * 1000
print('medida {}metros é igual {} centimetros e igual {} milimitros.'.format(m, cm, mm))
