# crie um programa que leia o nome completo de uma pessoa e mostre
# > o nome com todas as letras maisculas
# > o nome com todas as letras minusculas
# > quantas letras ao todo (sem considerar espaços)
# > quantas letras tem o primeiro nome
nome = str(input('Digite seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
separa = nome.split()
print(separa[0], len(separa[0]))
#print(nome.find(' '))

