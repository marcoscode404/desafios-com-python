import matplotlib.pyplot as plt 
from random import sample

x = sample(range(1, 1000), 100)
y = sample(range(1, 1000), 100)

plt.scatter(x, y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão, experimental')
plt.show()