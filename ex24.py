# crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'SANTO'

cid = str(input('Em que Cidade Você Nasceu? ')).strip()
# cid = cid.upper()
print(cid[:5].upper() == 'SANTO')

