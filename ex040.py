''' crie um programa que leia duas notas de um aluno e calcule sua
media, mostrando uma mensagem no final dde acordo com a média atingida
> Média abaixo de 5.0: reprovado
> Média entre 5.0 e 6.9: recuperção
> Média 7.0 ou superior: aprovado'''

nome = input('Digite o nome do aluno: ')
nota = int(input('Digite a primeira nota: '))
nota2 = int(input('Digete a segunda nota: '))
soma = nota + nota2
media = soma / 2
print('-=-'*30)
print(nome)

print(f'Primeira nota {nota} segunda nota {nota2}')
print(f'a soma das notas é {soma} e a média do aluno é {media}')
if media < 5:
    print('Reprovado')
elif media < 6.9:
    print('Em recuperção, precisa estudar um pouco mais')
else:
    print('APROVADO')
print('-=-'*30)
