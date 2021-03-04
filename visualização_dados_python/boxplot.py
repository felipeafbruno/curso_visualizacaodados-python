# Boxplot - diagrama de caixa
import matplotlib.pyplot as plt
import random


vetor = [13, 25, 53, 94, 65, 41, 56]

for i in range(100):
    numero_aleatorio = random.randint(0,50)
    vetor.append(numero_aleatorio)


plt.boxplot(vetor)
plt.title('Gráfico de Boxplot')
plt.show()
