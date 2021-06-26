#07 - Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def salario(horas,salario):
    horas_extras = horas - 220
    valor_hora = salario/220
    horasExtrasGanha = (horas_extras * 1.5) * valor_hora
    total = salario + horasExtrasGanha
    print(f'O salario de quem trabalhou {horas_extras} horas extras \nganhando R${salario:.2f} por mes é de R${horasExtrasGanha:.2f} ganhos em horas extras no total da R${total:.2f}')


ordenado = float(input('Digite seu Salario: '))
hora = float(input('Digite quantas horas trabalhadas: '))

salario(hora,ordenado)
