# #02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

maior_18 = homens = mulheres_20_menos = 0

while True:
    print('-'*20)
    age = int(input('Qual sua Idade: '))
    sexo = str(input('Qual seu sexo:\n[M,F]: ')).upper().strip()
    if age > 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and age < 20:
        mulheres_20_menos += 1
    cond = str(input('Deseja continuar ? [S/N] ')).upper().strip()
    if cond == 'N':
        break
print('-'*20)
print(f'Existe nesse cadastro {maior_18} pessoas com mais de 18 anos de idade.\n'
      f'Foram cadastrados {homens} homens. \n'
      f'E temos {mulheres_20_menos} mulheres com menos de 20 anos de idade')