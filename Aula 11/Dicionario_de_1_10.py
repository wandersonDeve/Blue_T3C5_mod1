# b – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.​

quadrado = {}
lista = list(range(1,11))

for i in lista:
    quadrado[i] = i**2

print(quadrado)