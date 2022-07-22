'''escreva um programa para aprovar o emprestimo bancario para a compra de
uma casa. O programa vai perguntar o valor da casa, o salario do comprador e
em quantos anos ele vai pagar.
calcule o valor da prestação mensal, sabendo que ele não pode exceder
30% do salario ou entao o emprestimo será negado'''

linha = print('~='*10)
print(linha)
print('EMPRÉSTIMO')
print(linha)
casa = float(input('qual o valor da casa? R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Em quantos anos quer pagar? : '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} ')
print(f'A prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser Concedido')
else:
    print('Empréstimo Negado')
##