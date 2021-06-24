def area(largura,comprimento):
    area = largura * comprimento
    print(f'O terreno com Largura {largura} m e comprimento {comprimento} m tem de area {area} m².')


lado1 = float(input('Digite em metros o valor da largura do terreno : '))
lado2 = float(input('Digite em metros o valor da comprimento do terreno : '))
area(lado1, lado2)