''' Crie um programa que leia uma frase qualquer e diga se ela e um palindromo,
desconsiderando os espaços
ex= apos a sopa
ex= a sacada da casa
ex= a torre da derrota
ex o lobo ama o bolo
ex= anotaram a data da maratona'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('Não temos um Palíndromo')