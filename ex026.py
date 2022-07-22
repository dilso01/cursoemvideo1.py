# faça um programa que leia uma frase pelo teclado e mostre
#
# > quantas vezes aparece a letra 'A'
# > em que posição ela aparece a primeira vez
# > em que posição ela aparece a última vez
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece na pasição {} pela primeira vez.'.format(frase.find('A')+1))
print('A letra A aparece na pasição {} pela primeira vez.'.format(frase.rfind('A')+1))
