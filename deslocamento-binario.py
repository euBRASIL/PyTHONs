import matplotlib.pyplot as plt

# Função para mostrar o deslocamento binário
def plot_binary_shift():
    nums = [0.5**i for i in range(10)]  # Lista de números decrescentes

    plt.figure(figsize=(8, 5))
    plt.plot(nums, marker='o', linestyle='-', color='r')
    plt.title('Deslocamento Binário')
    plt.xlabel('Iterações')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.show()

plot_binary_shift()  # Mostrar o gráfico de deslocamento binário
