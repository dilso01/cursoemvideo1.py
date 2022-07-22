import requests
#API cotação de moedas
# no site https://docs.awesomeapi.com.br/api-de-moedas voce pega o
# link abaixo que vai te direcionar para a API de cotação de moedas

# requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
# print(requisicao)
# print(requisicao.json())

# criação da API, site da google https://console.firebase.google.com, criar novo projeto, Realtime database (criar em modo teste)
#dar um nome ao projeto, vai criar um link copia esse link que vamos usar pra ecessar ele pelo pycharm, um lembrete nos termos de
#uso do firebase ele pede que você coloque no final desse link .json

#pegar informação de uma API função GET
#codigo
# requisicao = requests.get('https://aula--requests-default-rtdb.firebaseio.com/.json')
# print(requisicao)
# print(requisicao.json())

#adicionar uma informação de um API função POST
# crie um dicionário e coloque ele entre aspas simples.
#coloque as informações que deseja adicionar no banco de dados, em uma variavel
# #adicione ao link o que você quer adicionar no banco de dados

#codigo
# informacoes = '{"nome": "Amanda"}'

# requisicao = requests.post('https://aula--requests-default-rtdb.firebaseio.com/.json', data=informacoes)
# print(requisicao)
# print(requisicao.json())


#corrigir um item no banco de dados função PATCH
#você pega o link que deseja fazer a correção, e adiciona ao link do seu banco de dados

#codigo
# informacoes = '{"nome": "Pedro", "sobrenome": "Silva", "idade": "28"}'
#
# requisicao = requests.patch('https://aula--requests-default-rtdb.firebaseio.com/-N3p_L9h7ExTbtcF-VY6.json', data=informacoes)
# print(requisicao)
# print(requisicao.json())

#deletar um item do banco de dados função DELETE
#vá ate o banco de dados pegue o link que quer deletar e copie
#como é uma função delete não tem complicações no codigo,
#codigo
#requisicao = requests.delete("https://aula--requests-default-rtdb.firebaseio.com/-N3p_L9h7ExTbtcF-VY6/-N3ped9fGAGFwVfEONZ9.json")


