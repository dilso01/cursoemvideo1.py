import requests
# entendo o request.
# no site https://docs.awesomeapi.com.br/api-de-moedas voce pega o
# link abaixo que vai te direcionar para a API de cotação de moedas

# requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
# print(requisicao)
# print(requisicao.json())

# criação da IPA, site da google https://console.firebase.google.com, criar novo projeto, Realtime database (criar em modo teste)
#dar um nome ao projeto, vai criar um link copia esse link que vamos usar pra ecessar ele pelo pycharm, um lembrete nos termos de
#uso do firebase ele pede que você coloque no final desse link .json


requisicao = requests.get('https://aula--requests-default-rtdb.firebaseio.com.json')
print(requisicao)
print(requisicao.json())