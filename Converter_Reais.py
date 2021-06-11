# Script para converter Reais em uma das 5 moedas listadas
# Dólar(USD), Libra Esterlina(GBP), Dólar Canadense(CAD), Peso Argentino(ARS) e Peso Chileno(CLP)

# Cotações para Dólar(USD), Libra Esterlina(GBP), Dólar Canadense(CAD), Peso Argentino(ARS) e Peso Chileno(CLP)
# Viriam de uma fonte externa
cotacao_USD = 5.04
cotacao_GBP = 7.13
cotacao_CAD = 4.16
cotacao_ARS = 0.053
cotacao_CLP = 0.007

# Função Menu
# Coloquei apenas para facilitar uma futura chamada de repetição
def menu_moedas():
    print("[1] Dólar (USD) \n" + 
        "[2] Libra Esterlina (GBP) \n" +
        "[3] Dólar Canadense (CAD) \n" +
        "[4] Peso Argentino (ARS) \n" +
        "[5] Peso Chileno (CLP) \n")
    moeda = (int(input("Escolha a moeda de destino dentre as opções acima: ").replace(",",".")))
    return moeda

#  Lê o valor em R$ que o usuário irá digitar
BRL = float(input("Digite o valor em Reais(BRL) que deseja converter: ").replace(",", ".")) 
moeda = menu_moedas()

# Organizando em uma Lista {MOEDA} para indexar e usar a entrada do usuário
index_moeda = moeda - 1
dic_moeda = {"USD": cotacao_USD, "GPB": cotacao_GBP, "CAD": cotacao_CAD, "ARS": cotacao_ARS, "CLP": cotacao_CAD}
lista_cotacao = list(dic_moeda.values())
lista_moeda = list(dic_moeda.keys())

# Função que imprime a cotação
# É inútil neste script, mas se formos cotar mais de uma moeda, seria só implementar um laço de repetição aqui dentro
def cotar(valor):
    print(f"BRL {valor:.<15} {lista_moeda[index_moeda]} {valor/lista_cotacao[index_moeda]:.2f}")

# chama a função cotar()
cotar(BRL)
