''' Elabore um programa que calcule o valor a ser pago por um
produto considerando o seu preço normal e condição de pagamento:
>à vista dinheiro ou cheque 10% de desconto
>à vista no cartão: 5% de desconto
>em atée 2x no cartão preço normal
3x ou mais no cartão 20% de juros'''

valor = float(input('Qual o valor do produto? R$'))
pag = int(input('''escolha sua forma de pagamento
[ 1 ] para pagamento à vista
[ 2 ] para pagamento à vista no cartão
[ 3 ] pagamento em até 2x no cartão
[ 4 ] para parcelar em 3x ou mais vezes'''))
if pag == 1:
    print(f'O valor a ser pago é de R${valor * 0.90}')
elif pag == 2:
    print(f'O valor a ser pago é de R${valor * 0.95}')
elif pag == 3:
    print(f'O valor a ser pago é de R${valor}')
elif pag == 4:
    prest = int(input('Quantas vezes você quer fazer? '))
    print(f'O valor a ser pago é de R${valor * 1.20} divido em {prest}X de R${valor * 1.20 / prest}')
else:
    print('Opção inválida, escolha uma opção válida')

