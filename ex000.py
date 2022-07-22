print(50 * "-")
print("\033[40mValidador de CPF\033[m".center(50))
print(50 * "-")
cpf = input("Informe o cpf: ]").replace('.','').replace('-','').replace(',','')

while cpf == "00000000000" or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or cpf == '888888888' or cpf == '99999999999':
    print(30 * "-")
    print('CPF INVALIDO')
    print(30 * "-")
    cpf = input('Digite um cpf válido: ').replace('.','').replace('-','').replace(',','')
else:
    cpf = list(cpf)
    cont = 0
    contador = 10
    b = 0
    while contador >= 2:
        a = int(cpf[cont])
        b += a * contador
        contador = contador - 1
        cont = cont + 1

b = b % 11
b = 11 - b
pv1 = b

if b >= 10:
    b = 0
    pv1 = b
else:
    print()

cont = 0
contador = 11
b = 0

while contador >= 2:
    a = int(cpf[cont])
    b += a * contador
    contador = contador - 1
    cont = cont + 1

b = b % 11
b = 11 - b
pv2 = b

if b >= 10:
    b = 0
    pv2 = b
else:
    print()

while cpf:
    if int(cpf[9]) == pv1 and int(cpf[10]) == pv2:
cpf = valido
        print(30*"-")
        print('cpf valido')
        print(30 * "-")
    else:
        cpf = input("Informe o cpf: ]").replace('.','').replace('-','').replace(',','')
cpf = invalido
        print(30 * "-")
        print("CPF Inválido")
        print(30 * "-")
