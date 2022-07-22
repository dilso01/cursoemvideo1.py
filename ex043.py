'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status de acordo com a tabela abaixo
>abaixo de 18.5: abaixo do peso
>entre 18.5 e 25 peso ideal
>de 25 até 30: sobrepeso
>de 30 até 40 obesidade
>acima de 40: obesidade morbida'''
print(50*'-')
print('Descubra seu peso ideial'.center(50))
print(50*'-')
#peso = (float(input('Digite seu peso: ')))
altura = (float(input('Digite sua altura: ')))
print('1 - digite 1 para o sexo masculino')
print('2 - digite 2 para o sexo femino')
opcao = int(input('Digite a opção desejada'))
if opcao == 1:
  imc = 22
elif opcao == 2:
  imc = 21
else:
  imc = 0
peso = imc * (altura * altura)
print(50*'-')
print(f'***Seu peso ideal é: {peso:.2f}, kilos***'.center(50))
print(50*'-')