# pip install pillow matplotlib
import random
from PIL import Image, ImageDraw

# Configurações do calendário
days = 365  # Total de dias (um ano)
width, height = 7, 52  # 7 dias por semana, 52 semanas
cell_size = 20  # Tamanho de cada célula
margin = 2  # Espaço entre células

# Gera contribuições aleatórias (1-5 commits por dia)
contributions = [random.randint(0, 5) for _ in range(days)]

# Cores para o efeito "chama"
colors = [(0, 0, 0), (255, 50, 0), (255, 100, 0), (255, 150, 0), (255, 200, 0)]

# Cria a imagem
image = Image.new("RGB", (width * cell_size, height * cell_size), (0, 0, 0))
draw = ImageDraw.Draw(image)

# Preenche o calendário com pixels representando as contribuições
for i, count in enumerate(contributions):
    x = (i % width) * cell_size
    y = (i // width) * cell_size
    if count > 0:
        draw.rectangle(
            [x + margin, y + margin, x + cell_size - margin, y + cell_size - margin],
            fill=colors[min(count, len(colors) - 1)],
        )

# Salva o resultado
image.save("commits_fire.gif")
print("Imagem criada: commits_fire.gif")

# ---------------
images = []
for frame in range(10):  # 10 frames para a animação
    for i in range(len(contributions)):
        contributions[i] = max(0, contributions[i] - random.randint(0, 1))  # Reduz a intensidade
    # Atualiza a imagem
    for i, count in enumerate(contributions):
        x = (i % width) * cell_size
        y = (i // width) * cell_size
        if count > 0:
            draw.rectangle(
                [x + margin, y + margin, x + cell_size - margin, y + cell_size - margin],
                fill=colors[min(count, len(colors) - 1)],
            )
    images.append(image.copy())

# Salva como GIF animado
images[0].save("commits_fire.gif", save_all=True, append_images=images[1:], loop=0, duration=100)
print("GIF animado criado: commits_fire.gif")
