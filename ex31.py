# desenvolva um programa que pergunte a distância de uma viagem em km.
# >calcule o preço da passagem, cobramdo
# >R$0.50 por km para viagens até 200km
# >R$0.45 para viagens mais longas

valor = 0
dist = float(input('Digite a distancia de sua viagem: '))
if dist <= 200:
    valor = 0.50
    print(f'Valor da sua viagem é R$ {valor*dist:.2f}')
else:
    valor = 0.45
    print(f'Valor da sua viagem é R${valor*dist:.2f}')