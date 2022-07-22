#crie um programa que pergunte um nome completo e diga se tem 'SILVA' no nome, em qualquer lugar do nome
nome = str(input('Digite seu Nome: ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
