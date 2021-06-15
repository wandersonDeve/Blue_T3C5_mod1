### 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a soma deles (o usuário vai dizer quantos números serão informados antes de começar)

soma = 0

qtn_numeros = int(input('Quantos numeros deseja somar? '))

for i in range(0,qtn_numeros):
    num = float(input(f'Digite o {i+1}º numero: ').replace(',','.'))
    soma += num
print(f'Você digitou {qtn_numeros} numeros e sua soma deu {soma:.2f}')