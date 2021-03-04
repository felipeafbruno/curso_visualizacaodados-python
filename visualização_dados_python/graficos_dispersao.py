import matplotlib.pyplot as plt


x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 440, 3330, 100]

titulo = 'Scatterplot: gráfico de dispersão'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# em color é possível passar cores em hexadecimal
# 's' é o tamanho dos ponto no gráfico de dispersão e é possivel passar varios tamanhos
# utilizando a estrutura de  lista
plt.scatter(x, y, label='Meus pontos', color='k', marker='.', s=z) # são os pontos 
plt.plot(x, y, color='#000099', linestyle='--') # plot é a linha
# legend() - faz com que a legenda aparece no gráfico
plt.legend()
# plt.show()

# salvar a figura 
# dpi altera a resolução da imagem
plt.savefig('figura1.png', dpi=300)
