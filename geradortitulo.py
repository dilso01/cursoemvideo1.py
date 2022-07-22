import random
estado = input("Digite o estado:\n 1-São Paulo\n 2-Minas Gerais\n 3-Rio de Janeiro\n 4-Rio Grande do Sul\n 5-Bahia\n"
                   " 6-Paraná\n 7-Ceará\n 8-Pernambuco \n 9-Santa Catarina\n 10-Goiás \n 11-Maranhão\n 12-Paraíba\n 13-Pará"
                   "14-Espirito Santo\n 15-Piauí\n 16-Rio Grande do Norte\n 17-Alagoas\n 18-Mato Grosso\n"
                   " 19-Mato Grosso do Sul \n 20-Distrito Federal \n 21-Sergipe \n 22-Amazonas\n 23-Rondônia \n 24-Acre\n 25-Amapá"
                   "\n 26-Roraima\n 27-Tocantins\n 28-Exterior\n:")

x1 = random.randint(1,9)
x2 = random.randrange(1,9)
x3 = random.randint(1,9)
x4 = random.randrange(1,9)
x5 = random.randint(1,9)
x6 = random.randrange(1,9)
x7 = random.randint(1,9)
x8 = random.randrange(1,9)

if estado == "1":
    num = "01"
elif estado == "2":
    num = "02"
elif estado == "3":
    num = "03"
elif estado == "4":
    num = "04"
elif estado == "5":
    num = "05"
elif estado == '6':
    num = "06"
elif estado == '7':
    num = "07"
elif estado == '8':
    num = "08"
elif estado == '9':
    num = "09"
elif estado == '10':
    num = "10"
elif estado == '11':
    num = "11"
elif estado == '12':
    num = "12"
elif estado == '13':
    num = "13"
elif estado == '14':
    num = "14"
elif estado == '15':
    num = "15"
elif estado == '16':
    num = "16"
elif estado == '17':
    num = "17"
elif estado == '18':
    num = "18"
elif estado == '19':
    num = "19"
elif estado == '20':
    num = "20"
elif estado == '21':
    num = "21"
elif estado == '22':
    num = "22"
elif estado == '23':
    num = "23"
elif estado == '24':
    num = "24"
elif estado == '25':
    num = "25"
elif estado == '26':
    num = "26"
elif estado == '27':
    num = "27"
elif estado == '28':
    num = "28"












# calculo = ((x1*2)+(x2*3)+(x3*4)+(x4*5)+(x5*6)+(x6*7)+(x7*8)+(x8*9))
# teste = calculo % 11
#
# calculo2 = (int(estado[:1])*7)+(int(estado[2:])*8)+(teste*9)
# teste2 = calculo2 % 11

#print(f"{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}{num}{teste}{teste2}")
print(estado)