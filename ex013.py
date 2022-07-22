# Faça um algoritmo que leia o salario de u funcionario e mostre seu novo salario, com 15% de aumento
sal = float(input('Digite o seu salario: '))
saln = sal * 1.15
print('seu salario de R${:.2f}, recebeu um reajuste e agora seráR${:.2f}.'.format(sal, saln))