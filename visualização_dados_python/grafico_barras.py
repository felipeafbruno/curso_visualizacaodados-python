import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = 'Gráfico de barras'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.bar(x, y)
plt.show()
