### 06 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase = str(input('Digite uma frase: ').lower().strip())

for letra in frase:
    if letra not in 'aeiou':
        print(letra,end='')
