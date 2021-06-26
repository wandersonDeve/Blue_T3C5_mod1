def validaNumero(Pergunta):
    '''
    parametro num : Recebe uma pergunta onde o usuaria tera que digitar um numero.
    '''
    tam = len(Pergunta)/2
    resultado = 0
    while True:
        print('=-'*tam)
        n = str(input(Pergunta)).replace(',','.').strip()
        if n.isnumeric:
            resultado = n
            break
        else:
            print('\033[1;31mFavor digite u numero\033[m')
    return resultado