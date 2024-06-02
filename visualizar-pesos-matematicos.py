import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Função para simular a atualização de pesos (simplificada)
def update_weights(weights, gradients, learning_rate):
    for i in range(len(weights)):
        weights[i] -= learning_rate * gradients[i]
    return weights

# Exemplo de uso:
weights = np.random.rand(256)
gradients = np.random.rand(256)  # Gradientes simulados
learning_rate = 0.01
new_weights = update_weights(weights, gradients, learning_rate)
print("Pesos atualizados:", new_weights[:5])
