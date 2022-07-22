print(50*'-')
print('CONVERTENDO MOEDAS'.center(50))
print(50*'-')
print('Comece escolhendo a moeda quer comprar'.center(50))
#dolar = 1 == libra = 1.23, Real = 0.20, Euro = 1.05
#Reais = 1 == dolar = 5.08, Euro = 5.35, Libra = 6.26
#Euro = 1 == Reais = 0.19, dolar = 0.95, libra = 1.17
#Libra = 1 == Reais 0.16,  Euro = 0.85, Dolar = 0.81
#dolar = 1 #Moeda principal***
#libra = 1.23
#reais = 0.2
#euro = 1.05

print('1 - Digite para comprar Dólar com Real')
print('2 - Digite para comprar Dólar com Euro')
print('3 - Digite para comprar Dólar com Libra')
print('4 - Digite para comprar Real com Dólar')
print('5 - Digite para comprar Real com Euro')
print('6 - Digite para comprar Real com Libra')
print('7 - Digite para comprar Euro com Dólar')
print('8 - Digite para comprar Euro com Real')
print('9 - Digite para comprar Euro com libra')
print('10 - Digite para comprar Libra com Dólar')
print('11 - Digite para comprar Libra com Real')
print('12 - Digite para comprar Libra com Euro')
op = int(input('Digite a opção'))
if op == 1 or op == 2 or op == 3:
    libras = 1.23
    reais = 0.20
    euro = 1.05
elif op == 4 or op == 5 or op == 6:
    dolar = 5.08
    euro = 5.35
    libras = 6.26
elif op == 7 or op == 8 or op == 9:
    reais = 0.19
    dolar = 0.95
    libras = 1.17
elif op == 10 or op == 11 or op == 12:
    reais = 0.16
    euro = 0.85
    dolar = 0.81

if op == 1:
    op = 'Real'
    op2 = 'Dólar'
    total = float(input('Digite o valor desejado em Dólar'))
    total2 = total / reais
if op == 2:
    op = 'Euro'
    op2 = 'Dólar'
    total = float(input('Digite o valor desejado em Dólar'))
    total2 = total / euro
if op == 3:
    op = 'Libra'
    op = 'Dólar'
    total = float(input('Digite o valor desejado em Dólar'))
    total2 = total / libras
if op == 4:
    op = 'Dólar'
    op2 = 'Real'
    total = float(input('Digite o valor desejado em Reais'))
    total2 = total / dolar
if op == 5:
    op = 'Euro'
    op2 = 'Real'
    total = float(input('Digite o valor em Reais'))
    total2 = total / euro
if op == 6:
    op = 'Libra'
    op2 = 'Real'
    total = float(input('Digite o valor em Reais'))
    total2 = total / libras
if op == 7:
    op = 'Dólar'
    op2 = 'Euro'
    total = float(input('Digite o valor em Euro'))
    total2 = total / dolar
if op == 8:
    op = 'Real'
    op2 = 'Euro'
    total = float(input('Digite o valor em Euro'))
    total2 = total / reais
if op == 9:
    op = 'Libras'
    op2 = 'Euro'
    total = float(input('Digite o valor em Euro'))
    total2 = total / libras
if op == 10:
    op = 'Dólar'
    op2 = 'Libras´'
    total = float(input('Digite o valor em Libra'))
    total2 = total / dolar
if op == 11:
    op = 'Real'
    op2 = 'Libras'
    total = float(input('Digite o valor em Libra'))
    total2 = total / reais
if op == 12:
    op = 'Euros'
    op2 = 'Libras'
    total = float(input('Digite o valor em Libra'))
    total2 = total / euro

print(f'Valor desejado {total:.2f}',op2)
print(f'valor nessario em {total2:.2f}',op)
