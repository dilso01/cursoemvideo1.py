def triangulo(l1, l2, l3):
    if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
        return('Não é um triangulo')
    elif l1 == l2 == l3:
        return('Sim é um Triangulo Equilatero')
    elif l1 != l2 != l3:
        return ('Sim é um Triangulo Escaleno')
    else:
        return('Sim é um Triangulo Isóceles')


def contador(a,b):
    cont = 0
    for i in a:
        if i == b:
            cont += 1
    return cont


def inverso(a):
    a = a.reverse(a)
    return a

def dedos(a):
    cont = 0
    for i in a:
        cont += 1
    return cont
