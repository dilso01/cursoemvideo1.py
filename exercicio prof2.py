print(50*'-')
print('BEM VINDO'.center(50))
print(50*'-')
print('Escolha uma forma de pagamento'.center(50))
print('1 - À vista em dinheiro ou Cheque, recebe 10% de desconto')
print('2 - À vista no Cartão de crédito, recebe 15% de desconto')
print('3 - Em duas vezes, preço normal da etiqueta')
print('4 - Em duas vezes, preço normal da etiqueta mais juros de 10%')
opcao = input('Qual a opção desejada?')
etiqueta = float(input('Digite o valor do produto:R$: '))
if opcao == '1':
    valor = etiqueta * 0.90
elif opcao == '2':
    valor = etiqueta * 0.85
elif opcao == '3':
    valor = etiqueta
elif opcao == '4':
    valor = etiqueta * 1.10
else:
    print(f'Condição não cadastrada')
print(f'Valor da etiqueta {valor:.2f}')