# escreve um programa que leia a velocidade de um carra.
# se ele ultrapassar o 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# >a multa vai custar R$7,00 por cada km acima do limite
vel = int(input('Qual a velocidade? '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado por andar acima da velociade permitida {vel}km/h')
    print(f'Valor da sua multa é R${multa:.2f}')
else:
    print(f'Você está dentra da velocidade da via {vel}km/h')