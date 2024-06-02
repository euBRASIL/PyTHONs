import matplotlib.pyplot as plt
import numpy as np

# Definindo os dados
pontos = [4.4, 3.6, 4.5, 2.9, 4.7, 3.5, 3.6, 2.5, 3.4, 4.5]

# Número de setores (quantidade de pontos)
num_setores = len(pontos)

# Ângulo entre os setores
angulo_setor = 360 / num_setores

# Configurações do gráfico
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_theta_zero_location('N')  # Define o ponto zero do ângulo no topo
ax.set_theta_direction(-1)  # Define a direção anti-horária

# Desenhando os setores e os pontos
for i, ponto in enumerate(pontos):
    angulo = np.deg2rad(i * angulo_setor)
    ax.plot([angulo, angulo], [0, ponto], color='gray', linestyle='--')  # Desenha a linha do setor
    ax.scatter(angulo, ponto, color='blue')  # Desenha o ponto

# Ajustando os eixos
ax.set_xticks(np.deg2rad(np.arange(0, 360, angulo_setor)))  # Define os ângulos dos setores
ax.set_xticklabels([f'{i+1}' for i in range(num_setores)])  # Define os rótulos dos setores

# Exibindo o gráfico
plt.show()
