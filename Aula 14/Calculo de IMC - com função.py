#04.Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg

def imc(peso,altura):
    imc_calc = peso/(altura**2)
    print(f'O IMC foi de {imc_calc:.2f}')

imc(75,1.68)