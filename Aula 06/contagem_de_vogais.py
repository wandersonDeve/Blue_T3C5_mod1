### 01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece as vogais a,e,i,o,u

frase = str(input('Digite uma frase: ').lower())

vogal = 0

for i in frase:
    if i in 'aeiou':
        vogal += 1

print(f'Aparece {vogal} as vogais a, e, i, o, u')