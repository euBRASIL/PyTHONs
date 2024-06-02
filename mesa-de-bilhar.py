import numpy as np
import matplotlib.pyplot as plt

def plot_billiard_table(ball_white, ball_black):
    # Definir o centro da mesa
    center = (0, 0)
    radius = 1

    # Criar a figura e os eixos
    fig, ax = plt.subplots()

    # Desenhar a mesa de bilhar
    table = plt.Circle(center, radius, color='green', fill=False)
    ax.add_artist(table)

    # Desenhar a bola branca
    ax.plot(ball_white[0], ball_white[1], 'wo', markersize=10)

    # Desenhar a bola preta
    ax.plot(ball_black[0], ball_black[1], 'ko', markersize=10)

    # Definir limites dos eixos
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    # Adicionar título e rótulos dos eixos
    ax.set_title('Mesa de Bilhar Circular')
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')

    # Mostrar a mesa de bilhar
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

def main():
    # Posicionar a bola branca em qualquer posição (x, y) na mesa de bilhar
    ball_white = np.random.uniform(-1, 1, size=(2,))

    # Posicionar a bola preta em qualquer posição (x, y) na mesa de bilhar
    ball_black = np.random.uniform(-1, 1, size=(2,))

    # Visualizar a mesa de bilhar com as bolas branca e preta
    plot_billiard_table(ball_white, ball_black)

if __name__ == "__main__":
    main()
