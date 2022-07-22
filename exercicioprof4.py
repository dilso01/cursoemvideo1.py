print(50 * '-')
print('BEM VINDO AO HEMOSC'.center(50))
print(50 * '-')
idade = input('digite sua idade: ')

if idade > '65' or idade <= '15':
    print('*** Obrigado, mas Você não pode doar sangue! ***')
else:
    print('*** Vamos verificar nosso estoque ***')
print('1 - para tipo sanguíneo tipo O+')
print('2 - para tipo sanguíneo tipo O-')
print('3 - para tipo sanguíneo tipo B+')
print('4 - para tipo sanguíneo tipo B-')
print('5 - para tipo sanguíneo tipo AB+')
print('6 - para tipo sanguíneo tipo AB-')
print('7 - para tipo sanguíneo tipo A+')
print('8 - para tipo sanguíneo tipo A-')
sangue = int(input('Digite a opção do seu tipo sanguíneo: '))
op = 'O+'
on = 'O-'
bp = 'B+'
bn = 'B-'
abp = 'AB+'
abn = 'AB-'
ap = 'A+'
an = 'A-'
if sangue == 1:
    sangue = op
if sangue == 2:
    sangue = on
if sangue == 3:
    sangue = bp
if sangue == 4:
    sangue = bn
if sangue == 5:
    sangue = abp
if sangue == 6:
    sangue = abn
if sangue == 7:
    sangue = ap
if sangue == 8:
    sangue = an

print('Seu tipo sanguíneo é', sangue)

print(50 * '-')
print('Voce quer doar ou retirar sngue?')
print(50 * '-')
print('1 - Para doar sangue: ')
print('2 - para retirar: ')
opcao = int(input('Escolha uma das opções: '))

if opcao == 1:
    opcao = 'doar'
elif opcao == 2:
    opcao = 'retirar'
print(opcao)

