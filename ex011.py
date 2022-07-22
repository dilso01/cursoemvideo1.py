# Faça um program que leia a largura e a altura de uma parede em metros, calcula a sua área e
# a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2mt².

l1 = float(input('digite a primeira medida: '))
l2 = float(input('digite a segunda medida: '))
área = l1 * l2
print("Sua parede tem a medida de {}X{} e sua área é de {}m²".format(l1, l2, área))
tinta = área / 2
print('Você precisará de {}L de tinta para pintar a parede.'.format(tinta))