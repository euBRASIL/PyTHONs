import numpy as np
import matplotlib.pyplot as plt

# Definindo as matrizes
A = np.random.rand(8, 8)
B = np.random.rand(8, 8)

# Multiplicação de matrizes
C = np.dot(A, B)

# Normalizando os valores para o intervalo [0, 1]
C_normalized = C / np.max(C)

# Plotando o resultado em um formato de tabuleiro de xadrez
fig, ax = plt.subplots()
for i in range(8):
    for j in range(8):
        color = plt.cm.hot(C_normalized[i, j])
        ax.add_patch(plt.Rectangle((i, j), 1, 1, color=color))
        ax.text(i + 0.5, j + 0.5, f"{C_normalized[i, j]:.2f}", ha='center', va='center', color='black')

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.set_title('Tabuleiro de Xadrez com Valores Resultantes da Multiplicação de Matrizes')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
