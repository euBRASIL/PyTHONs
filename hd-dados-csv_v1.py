import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import pandas as pd

# Carregar dados do arquivo CSV
df = pd.read_csv('dados.csv')
pontos = df['valor'].values

# Número de setores
num_setores = len(pontos)

# Ângulo entre os setores
angulo_setor = 360 / num_setores

# Configurações do gráfico
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_theta_zero_location('N')  # Define o ponto zero do ângulo no topo
ax.set_theta_direction(-1)  # Define a direção anti-horária

# Lista para armazenar todos os pontos
todos_pontos = []

# Desenhando os setores e os pontos
for i, ponto in enumerate(pontos):
    angulo = np.deg2rad(i * angulo_setor)
    ax.plot([angulo, angulo], [0, ponto], color='gray', linestyle='--')  # Desenha a linha do setor
    sc = ax.scatter(angulo, ponto, color='blue')  # Desenha o ponto
    todos_pontos.append(sc)

# Ajustando os eixos
ax.set_xticks([])  # Remove os rótulos dos setores
ax.set_xticklabels([])

# Adicionando tooltips
crs = mplcursors.cursor(todos_pontos, hover=True)

@crs.connect("add")
def on_add(sel):
    ponto_idx = todos_pontos.index(sel.artist)
    sel.annotation.set_text(f'Ponto {ponto_idx + 1}\nValor: {pontos[ponto_idx]:.2f}')
    sel.annotation.get_bbox_patch().set(fc="white", alpha=0.8)  # Define a cor de fundo do balão de informação
    sel.annotation.get_bbox_patch().set_edgecolor('black')  # Define a cor da borda do balão de informação
    sel.annotation.set_fontsize(12)  # Aumenta o tamanho do texto

# Exibindo o gráfico
plt.show()
