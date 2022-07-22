# Crie um código solicite login e senha para dar acesso ao sistema.
# Já deverá estar previamente cadastrado no código as 3 primeiras letras
# do seu nome como usuário e sua data de nascimento sem separadores como senha.

log = str('adi')
sen = ('26091983')
login = print(input('Digite seu login: ')).strip()
senha = print(input('Digite sua senha: ')).strip()

if login == log or senha == sen:
    print('Sua entrada foi liberada')

else:
   print('Login e senha não confere, tente novamente')