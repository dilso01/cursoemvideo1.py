'''A confederção nacional de natação pracisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
> até 9 anos: mirim
>ate 14 anos: infantil
>até 19 anos: junior
>até 20 anos: senior
> acima: master'''

print('-=-'*20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO'.center(20))
print('-=-'*20)
atleta = input('Ddigite o nome do atleta: ').upper()
idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade == 20:
    categoria = 'Senior'
else:
    categoria = 'Master'

print('-=-'*20)
print(atleta.center(20))
print('-=-'*20)
print(categoria.center(20))
print('-=-'*20)