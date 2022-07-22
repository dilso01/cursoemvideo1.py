print(50 * "\33[93:2:1m-\33[m")
print("\33[93:2:1mTITULO DE ELEITOR\33[m".center(50))
print(50 * "\33[93:2:1m-\33[m")
print("\33[93:2:1mESCOLHA UMA OPÇÃO\33[m".center(50))
print(50 * "\33[93:2:1m-\33[m")
print("1 - Para verificar se seu Titulo de Eleitor e válido")
print("2 - Para gerar um Titulo de Eleitor")
print("3 - Para consultar o Estado emissor do seu Titulo de Eleitor")
opcao = input("Escolah uma Opção: [1/2/3] ").strip()
while opcao not in "123":
    opcao = str(input("Dados inválidos. Por favor escolah uma opção válida: "))
laco = "S"

if opcao == "1":
    while laco == "S":
        titulo = input("\33[93mInforme o numero do seu TITULO:\33[m").replace(".", "").replace("-", "").replace(",", "")
        titulo = list(titulo)

        contador = 0
        cont2 = 2
        tt = 0

        while contador <= 7:
            tt += int(titulo[contador]) * cont2
            contador += 1
            cont2 += 1
        titulo_digito = tt % 11

        tt = 0
        contador = 8
        cont2 = 7

        while contador < 11:
            tt += int(titulo[contador]) * cont2
            contador += 1
            cont2 += 1
        titulo_digito2 = tt % 11

        if titulo_digito == 10:
            titulo_digito = 0
        if titulo_digito2 == 10:
            titulo_digito2 = 0
        print(titulo_digito, titulo_digito2)

        if (titulo[0]) == (titulo[1]) and (titulo[0]) == (titulo[2]) and (titulo[0]) == (titulo[3]) and (titulo[0]) == (
        titulo[4]) and (titulo[0]) == (
                titulo[5]) and (titulo[0]) == (titulo[6]) and (titulo[0]) == (titulo[7]) and (titulo[0]) == (
        titulo[8]) and (titulo[0]) == (titulo[9]):
            print(30 * "-")
            print("SEU TITULO DE ELEITOR NÃO É VALIDO!")
            print(30 * "-")

        elif titulo[10] == str(titulo_digito) and titulo[11] == str(titulo_digito2):
            print(30 * "-")
            print(f"SEU TITULO DE ELEITOR É VALIDO!")
            print(30 * "-")
        else:
            print(30 * "-")
            print("SEU TITULO DE ELEITOR NÃO É VALIDO!")
            print(30 * "-")

        if titulo[8] == "0" and titulo[9] == "1":
            print("São Paulo")
        elif titulo[8] == "0" and titulo[9] == "2":
            print("Minas Gerais")
        elif titulo[8] == "0" and titulo[9] == "3":
            print("Rio de Janeiro")
        elif titulo[8] == "0" and titulo[9] == "4":
            print("Rio Grande do Sul")
        elif titulo[8] == "0" and titulo[9] == "5":
            print("Bahia")
        elif titulo[8] == "0" and titulo[9] == "6":
            print("Paraná")
        elif titulo[8] == "0" and titulo[9] == "7":
            print("Ceará")
        elif titulo[8] == "0" and titulo[9] == "8":
            print("Pernambuco")
        elif titulo[8] == "0" and titulo[9] == "9":
            print("Santa Catarina")
        elif titulo[8] == "1" and titulo[9] == "0":
            print("Goiás")
        elif titulo[8] == "1" and titulo[9] == "1":
            print("Maranhão")
        elif titulo[8] == "1" and titulo[9] == "2":
            print("Paraíba")
        elif titulo[8] == "1" and titulo[9] == "3":
            print("Pará")
        elif titulo[8] == "1" and titulo[9] == "4":
            print("Espirito Santo")
        elif titulo[8] == "1" and titulo[9] == "5":
            print("Piauí")
        elif titulo[8] == "1" and titulo[9] == "6":
            print("Rio Grande do Norte")
        elif titulo[8] == "1" and titulo[9] == "7":
            print("Alagoas")
        elif titulo[8] == "1" and titulo[9] == "8":
            print("Mato Grosso")
        elif titulo[8] == "1" and titulo[9] == "9":
            print("Mato Grosso do Sul")
        elif titulo[8] == "2" and titulo[9] == "0":
            print("Distrito Federal")
        elif titulo[8] == "2" and titulo[9] == "1":
            print("Sergipe")
        elif titulo[8] == "2" and titulo[9] == "2":
            print("Amazonas")
        elif titulo[8] == "2" and titulo[9] == "3":
            print("Rondônia")
        elif titulo[8] == "2" and titulo[9] == "4":
            print("Acre")
        elif titulo[8] == "2" and titulo[9] == "5":
            print("Amapá")
        elif titulo[8] == "2" and titulo[9] == "6":
            print("Roraima")
        elif titulo[8] == "2" and titulo[9] == "7":
            print("Tocantins")
        elif titulo[8] == "2" and titulo[9] == "8":
            print("Exterior")

        laco = input("Há mais um titulo de eleitor para verificar?: Responda com: S ou N: ").upper()
        if laco == "N":
            print(30 * "-")
            print("Função Terminada.")
            print(30 * "-")
            break
elif opcao == "2":
               # escolher o estado
    estado = input("Digite o estado:\n 1-São Paulo\n 2-Minas Gerais\n 3-Rio de Janeiro\n 4-Rio Grande do Sul\n 5-Bahia\n"
            " 6-Paraná\n 7-Ceará\n 8-Pernambuco \n 9-Santa Catarina\n 10-Goiás \n 11-Maranhão\n 12-Paraíba\n 13-Pará"
            "14-Espirito Santo\n 15-Piauí\n 16-Rio Grande do Norte\n 17-Alagoas\n 18-Mato Grosso\n"
            " 19-Mato Grosso do Sul \n 20-Distrito Federal \n 21-Sergipe \n 22-Amazonas\n 23-Rondônia \n 24-Acre\n 25-Amapá"
            "\n 26-Roraima\n 27-Tocantins\n 28-Exterior\n:")
    import random
    numero = [random.randint(0, 9) for p in range(0, 8)]

               # separar o numero do estado
    if estado == "1":
        numero.append(0)
        numero.append(1)
    elif estado == "2":
        numero.append(0)
        numero.append(2)
    elif estado == "3":
        numero.append(0)
        numero.append(3)
    elif estado == "4":
        numero.append(0)
        numero.append(4)
    elif estado == "5":
        numero.append(0)
        numero.append(5)
    elif estado == '6':
        numero.append(0)
        numero.append(6)
    elif estado == '7':
        numero.append(0)
        numero.append(7)
    elif estado == '8':
        numero.append(0)
        numero.append(8)
    elif estado == '9':
        numero.append(0)
        numero.append(9)
    elif estado == '10':
        numero.append(1)
        numero.append(0)
    elif estado == '11':
        numero.append(1)
        numero.append(1)
    elif estado == '12':
        numero.append(1)
        numero.append(2)
    elif estado == '13':
        numero.append(1)
        numero.append(3)
    elif estado == '14':
        numero.append(1)
        numero.append(4)
    elif estado == '15':
        numero.append(1)
        numero.append(5)
    elif estado == '16':
        numero.append(1)
        numero.append(6)
    elif estado == '17':
        numero.append(1)
        numero.append(7)
    elif estado == '18':
        numero.append(1)
        numero.append(8)
    elif estado == '19':
        numero.append(1)
        numero.append(9)
    elif estado == '20':
        numero.append(2)
        numero.append(0)
    elif estado == '21':
        numero.append(2)
        numero.append(1)
    elif estado == '22':
        numero.append(2)
        numero.append(2)
    elif estado == '23':
        numero.append(2)
        numero.append(3)
    elif estado == '24':
        numero.append(2)
        numero.append(4)
    elif estado == '25':
        numero.append(2)
        numero.append(5)
    elif estado == '26':
        numero.append(2)
        numero.append(6)
    elif estado == '27':
        numero.append(2)
        numero.append(7)
    elif estado == '28':
        numero.append(2)
        numero.append(8)
    #print(numero)
    contador = 0
    cont2 = 2
    tt = 0
    while contador <= 7:
        tt += int(numero[contador]) * cont2
        contador += 1
        cont2 += 1
    numero_digito = tt % 11
    numero.append(numero_digito)

    tt = 0
    contador = 8
    cont2 = 7

    while contador < 11:
        tt += int(numero[contador]) * cont2
        contador += 1
        cont2 += 1
    numero_digito2 = tt % 11

    if numero_digito == 10:
        numero_digito = 0
    if numero_digito2 == 10:
        numero_digito2 = 0
    numero.append(numero_digito2)
    print(50 * "\33[93:2:1m-\33[m")
    print("\33[93:2:1mSEU TÍTULO DE ELEITOR É\33[m".center(50))
    print(str(f"\33[93:2:1m{numero}\33[m").strip().replace(',', '').replace(' ',''))
    print(50 * "\33[93:2:1m-\33[m")

else:
    print(50 * "\33[93:2:1m-\33[m")
    consulta = input("\33[93:2:1mDigite o Número do seu Titulo de Eleitor\33[m".center(50))
    print(50 * "\33[93:2:1m-\33[m")
    consulta = list(consulta)

    if consulta[8] == "0" and consulta[9] == "1":
        print("\33[93:2:1mSÃO PAULO\33[m".center(50))
    elif consulta[8] == "0" and consulta[9] == "2":
        print("\33[93:2:1mMINAS GERAIS\33[m".center(50))
    elif consulta[8] == "0" and consulta[9] == "3":
        print("\33[93:2:1mRIO DE JANEIRO\33[m".center(50))
    elif consulta[8] == "0" and consulta[9] == "4":
        print("\33[93:2:1mRIO GRANDE DO SUL\33[m".center(50))
    elif consulta[8] == "0" and consulta[9] == "5":
        print("\33[93:2:1mBAHIA\33[m".center(50))
    elif consulta[8] == "0" and consulta[9] == "6":
        print("\33[93:2:1mPARANÁ\33[m".center(50))
    elif consulta[8] == "0" and consulta[9] == "7":
        print("\33[93:2:1mCEARÁ\33[m".center(50))
    elif consulta[8] == "0" and consulta[9] == "8":
        print("\33[93:2:1mPERNAMBUCO\33[m".center(50))
    elif consulta[8] == "0" and consulta[9] == "9":
        print("\33[93:2:1mSANTA CATARINA\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "0":
        print("\33[93:2:1mGOIÁS\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "1":
        print("\33[93:2:1mMARANHÃO\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "2":
        print("\33[93:2:1mPARAÍBA\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "3":
        print("\33[93:2:1mPARÁ\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "4":
        print("\33[93:2:1mESPÍRITO SANTO\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "5":
        print("\33[93:2:1mPIAUÍ\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "6":
        print("\33[93:2:1mRIO GRANDE DO NORTE\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "7":
        print("\33[93:2:1mALAGOAS\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "8":
        print("\33[93:2:1mMATO GROSSO\33[m".center(50))
    elif consulta[8] == "1" and consulta[9] == "9":
        print("\33[93:2:1mMATO GROSSO DO SUL\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "0":
        print("\33[93:2:1mDISTRITO FEDERAL\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "1":
        print("\33[93:2:1mSERGIPE\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "2":
        print("\33[93:2:1mAMAZONAS\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "3":
        print("\33[93:2:1mRONDONIA\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "4":
        print("\33[93:2:1mACRE\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "5":
        print("\33[93:2:1mAMAPÁ\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "6":
        print("\33[93:2:1mRORAIMA\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "7":
        print("\33[93:2:1mTOCANTINS\33[m".center(50))
    elif consulta[8] == "2" and consulta[9] == "8":
        print("\33[93:2:1mEXTERIOR\33[m".center(50))
print(50 * "\33[93:2:1m-\33[m")