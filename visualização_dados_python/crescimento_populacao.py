# Crescimento da População Brasileira de 1980 á 2015
# dados do DataSUS
import matplotlib.pyplot as plt


dados = open('visualização_dados_python/populacao_brasileira.csv').readlines()

# Eixos
x = [] # x para os anos
y = [] # y para o tamanho da população

# abaixo 'dados' é iterados para buscar as linhas
# pulando a linha '0' e partindo da linha 1 em diante
# é da um splite em ';' para separar em dados de ano e tamanho da população
# desse modo é possível popular os eixos X e Y com ano e população 
for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

titulo_grafico = 'Crescimento da População Brasileira de 1980-2015'
label_x = 'ano'
label_y = 'população x100.000.000'
legenda_x = 'ano'
legenda_y = 'população'

plt.title(titulo_grafico)
plt.xlabel(label_x)
plt.ylabel(label_y)

plt.bar(x, y, color='#0A75AD', label=legenda_x)
plt.plot(x, y, color='k', linestyle="--", label=legenda_y)
plt.legend()
plt.show()

# plt.savefig('população_brasileira.png', dpi=300)
