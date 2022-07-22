'''faça um program que leia o ano de nascimento de um jovem e
informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-:raise é a hora de se alistar.
-:raise ja passou do tempo do alistamento
seu program também deverá mostrar o tempo que falta ou que passou do prazo.'''

# recruta = input('Digite seu nome: ').upper()
# idade = int(input('Digite sua ideda: '))
#
# if idade > 18:
#     print('-=-' * 30)
#     print(recruta.center(30))
#     print(f'Você ja passou da idade pra se alistar, seu prazo passou em {idade - 18} anos')
#     print('-=-' * 30)
# elif idade == 18:
#     print('-=-' * 30)
#     print(recruta.center(30))
#     print('Está na hora de servir o país')
#     print('-=-' * 30)
# else:
#     print('-=-'*30)
#     print(recruta.center(30))
#     print(f'Ainda não chegou sua hora de servir o país, faltam {18 - idade} anos')
#     print('-=-' * 30)
from datetime import date
atual = date.today().year
ano = int(input('Informe o seu ano de nascimento: '))
idade = atual - ano
print(f'quem nasceu em {ano}, tem {idade} anos, em {atual}')
if idade == 18:
    print('Você precisa se alistar imediatamente')
elif idade < 18:
    print(f'Você ainda não tem 18 anos, faltam {18 - idade} para o alistamento')
else:
    print(f'Você ja passou da idade de se alistar há {idade - 18} anos')