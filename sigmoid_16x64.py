import numpy as np

# Definindo a função sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Criando matrizes de exemplo A e B
A = np.random.rand(16, 64)
B = np.random.rand(16, 64)

# Multiplicação de matriz elemento a elemento
C = A * B

# Divisão de matriz elemento a elemento
D = A / B

# Aplicando a função sigmoid a cada elemento de C e D
C_sigmoid = sigmoid(C)
D_sigmoid = sigmoid(D)

# Exibindo cada etapa
for i in range(16):
    for j in range(64):
        print(f"Elemento ({i},{j}):")
        print(f"Multiplicação: {A[i,j]} * {B[i,j]} = {C[i,j]}")
        print(f"Divisão: {A[i,j]} / {B[i,j]} = {D[i,j]}")
        print(f"Sigmoid da Multiplicação: {C_sigmoid[i,j]}")
        print(f"Sigmoid da Divisão: {D_sigmoid[i,j]}")
        print("="*30)
