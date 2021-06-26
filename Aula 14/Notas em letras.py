#05.Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

def nota_aluno(nt):
    if nt >= 9.0:
        print('A')
    elif nt >=8.0:
        print('B')
    elif nt >=7.0:
        print('C')
    elif nt >=6.0:
        print('D')
    elif nt <=4.0:
        print('F')

nota = float(input('Digite a nota do aluno: '))

nota_aluno(nota)
