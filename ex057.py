sexo = str(input('Informe seu sexo: [M/F] ')).upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

