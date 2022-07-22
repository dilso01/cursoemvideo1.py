print(50*"-")
print('\33[93:40:2:1mVALIDADOR DE TITULO DE ELEITOR\33[m'.center(60))
print(50*"-")

titulo = input('\33[93mInforme o numero do seu TITULO:\33[m').replace('.','').replace('-','').replace(',','')

while titulo == "00000000000" or titulo == '11111111111' or titulo == '22222222222' or titulo == '33333333333' or titulo == '44444444444' or titulo == '55555555555' or titulo == '66666666666' or titulo == '77777777777' or titulo == '888888888' or titulo == '99999999999':
    print(30 * "-")
    print('TITULO DE ELEITOR INVALIDO')
    print(30 * "-")
    cpf = input('Digite um cpf válido: ').replace('.','').replace('-','').replace(',','')
else:
    titulo = list(titulo)
    cont = 0
    contador = 2
    b = 0
    while contador <= 9:
        a = int(titulo[cont])
        b += a * contador
        contador = contador + 1
        cont = cont + 1

b = b % 11
pv1 = b

if b >= 10:
    b = 0
    pv1 = b

print(f(titulo,[9],[10]))

cont = 8
contador = 7
b = 0
#print(pv1)
while contador <= 9:
     a = int(titulo[cont])
     b = b + a * contador
     contador = contador + 1
     cont = cont + 1

b = b % 11

pv2 = b

if b >= 10:
    b = 0

print(pv2)

