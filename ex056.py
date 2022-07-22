'''Desenvolva um programa que leia nome idade e sexo de 4 pessoas e no final
mostre
> a média de idade do grupo
>qual o nome do homem mais velho
>quantas mulheres tem menos de 20 anos'''
soma_idade = 0
media_idade = 0
maioridade_homem = 0
nome_velho = 0
total_mulher20 = 0
for i in range(1, 5):
    nome = input(f'-----{i}ª PESSOA------').upper()
    idade = int(input('Idade'))
    sexo = input(' Sexo: [M/F]').strip().upper()
    soma_idade += idade
    if i == 1 and sexo in 'M':
        maioridade_homem = idade
        nome_velho = nome
    if sexo in 'F' and idade < 20:
        total_mulher20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maioridade_homem} anos e se chama {nome_velho}')
print(f'Ao todo são {total_mulher20} com menos de 20 anos')