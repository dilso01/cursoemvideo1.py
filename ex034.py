# escreva um program que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# >para salarios superiores a 1.250,00, calcule um aumento de 10%
# >para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite o seu salario: '))
if sal >= 1250.00:
    print(f'Seu novo salario seré R${sal*1.15:.2f}')
else:
    print(f'Seu novo salario será R${sal*1.10:.2f}')