# 2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.

quadrado = {}
lista = [1, 4, 5, 6, 7, 9]

for i in lista:
    quadrado[i] = i**2

print(quadrado)

