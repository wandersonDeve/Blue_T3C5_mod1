def verificaNumero(pergunta):
    tam = len(pergunta)//2
    resultado = 0
    while True:
        print('=-'*20)
        n = str(input(pergunta).strip().replace(',','.'))
        if n.replace('.','').isnumeric():
            if '.' in n:
                resultado = float(n)
                break
            else:
                resultado = int(n)
                break
        else:
            print('\033[1;31mEntrada invalida\033[m')
    return resultado