# import matplotlib.pyplot as plt 
# from random import sample

# x = sample(range(1, 1000), 100)
# y = sample(range(1, 1000), 100)

# plt.scatter(x, y)
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# plt.title('Gráfico de Dispersão, experimental')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# data = np.random.randn(1000)

# plt.hist(data, bins=30, alpha=0.75, color='blue')
# plt.xlabel('Valor')
# plt.ylabel('Frequência')
# plt.title('Histograma')
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# plt.boxplot(data, vert=True, patch_artist=True)
# plt.xlabel('Grupo')
# plt.ylabel('Valor')
# plt.title('Box Plot')
# plt.show()


# import plotly.graph_objects as go
# import numpy as np

# t = np.linspace(0, 10, 100)
# y = np.sin(t)

# fig = go.Figure(data=go.Scatter(x=t, y=y, mode='lines', name='Seno'))
# fig.update_layout(title='Gráfico de Linhas', xaxis_title='Tempo', yaxis_title='Amplitude')
# fig.show()

# import plotly.graph_objects as go

# labels = ['Oxigênio', 'Hidrogênio', 'Gás Carbônico', 'Nitrogênio']
# values = [4500, 2500, 1053, 500]

# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
# fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
#                   marker=dict(line=dict(color='#000000', width=2)))
# fig.update_layout(title='Gráfico de Pizza')
# fig.show()



