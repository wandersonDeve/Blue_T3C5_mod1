vingadores = {'Chris Evans':'Capitão América','Mark Ruffalo':'Hulk','Tom Hiddleston':'Loki','Chris Hemworth':'Thor','Robert Downey Jr':'Homem de Ferro','Scarlett Johansson':'Viúva Negra'}

vingadores['Tom Holland'] = 'Homem-Aranha'

print('=-'*30)
print('Em vingadores Temos:\n')
for k,v in vingadores.items():
    print(f'\033[1;32m{k:<20}\033[m no papel de \033[1;33m{v:<30}\033[m')
print('=-'*30)