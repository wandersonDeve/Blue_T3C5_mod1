###   2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem corretamente a senha. A senha é “Blue123” 2b - Exiba quantas vezes o usuário errou a digitação. ###

senha = 'Blue123'
tentativas = 0

while True:
    chance = str(input('Qual a senha da plataforma? '))
    if chance == senha:
        break
    else:
        tentativas += 1
print(f'Você errou {tentativas} vezes antes de acertar a senha \033[01;33m{senha}\033[m')