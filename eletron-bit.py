import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Função para inicializar o gráfico
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

# Função de animação
def animate(i):
    # Decaimento eletrônico
    time = [t for t in range(i)]
    electrons = [10 * 0.5**t for t in time]
    line1.set_data(time, electrons)

    # Deslocamento binário
    nums = [0.5**t for t in range(i)]
    line2.set_data(range(i), nums)

    # Transformação de números negativos em positivos
    negative_nums = [-0.5**t for t in range(i)]
    positive_nums = [-num for num in negative_nums]
    line3.set_data(range(i), negative_nums)
    
    return line1, line2, line3

# Criando a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Definindo os limites dos eixos
ax.set_xlim(0, 20)
ax.set_ylim(-2, 12)

# Criando as linhas para cada gráfico
line1, = ax.plot([], [], 'r-', label='Decaimento Eletrônico')
line2, = ax.plot([], [], 'g-', label='Deslocamento Binário')
line3, = ax.plot([], [], 'b-', label='Números Negativos > Positivos')

# Adicionando legenda
ax.legend()

# Criando a animação
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=20, interval=500, blit=True)

plt.title('Animação das Condições de Analogia')
plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.grid(True)
plt.show()
