frase = 'Curso em video Python'
print(frase[:13])
print(frase.count('o'))   #verificar quantas letras ou numeros tem numa frase
print(frase.strip()) # retira espaços indesejados
print(len(frase)) # conta quantos caractesres tem
print(frase.replace('Python', 'android')) # substitui um nome de uma str, mas nao salva a troca, so faz a troca no momento
print(frase.lower().find('video')) # o .lower transforma a frase toda em letras minusculas, .find procura se tem a palavradentro da frase
print(frase.split()) # ele divide a frase
print(frase.split()) # ele divide a frase e printa somente a posição que voce escolher
dividido = frase.split()
print(dividido[2][3]) # ele esta pedindo pra mostar, a palavra que esta na posição 2 e verificar a letra que esta na posição 3
