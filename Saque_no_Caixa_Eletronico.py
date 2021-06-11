valor = int(input('Qual valor você deseja sacar? R$ '))

lobo = valor // 200
peixe = (valor % 200)//100
onca = ((valor%200)%100)//50
mico = (((valor%200)%100)%50)//20
arara = ((((valor%200)%100)%50)%20)//10
garça = (((((valor%200)%100)%50)%20)%10)//5
tartaruga = ((((((valor%200)%100)%50)%20)%10)%5)//2
beija_flor = (((((((valor%200)%100)%50)%20)%10)%5)%2)//1

if lobo != 0:
    print(f'Total de {lobo} cedulas de R$ 200,00')
if peixe != 0:
    print(f'Total de {peixe} cedulas de R$ 100,00')
if onca != 0:
    print(f'Total de {onca} cedulas de R$ 50,00')
if mico != 0:
    print(f'Total de {mico} cedulas de R$ 20,00')
if arara != 0:
    print(f'Total de {arara} cedulas de R$ 10,00')
if garça != 0:
    print(f'Total de {garça} cedulas de R$ 5,00')
if tartaruga != 0:
    print(f'Total de {tartaruga} cedulas de R$ 2,00')
if beija_flor != 0:
    print(f'Total de {beija_flor} cedulas de R$ 1,00')
