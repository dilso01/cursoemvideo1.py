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
  imc = ('Não existe')

peso = imc * (altura * altura)

print(f'Seu peso ideal é: {peso:.2f}, kilos')


