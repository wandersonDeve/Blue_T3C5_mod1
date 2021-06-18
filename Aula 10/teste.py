### LIST CONPREHENSION ###

# CASO 01
lista = [10,20,30,40,50,60,70,80,90,100]

nova_lista = [valor*2 for valor in lista]

print(nova_lista)

# CASO 02

lista1 = [500,1500,2000,100,25]

nova_lista1 = [valor*0.5 for valor in lista1 if valor >= 1000]

print(nova_lista1)

