import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Gerar dados de exemplo (1000 chaves privadas de 256 bits)
num_chaves = 1000
chaves_privadas = np.random.randint(2, size=(num_chaves, 256))
rotulos = np.random.randint(2, size=(num_chaves, 1))

# Definindo o modelo
modelo = Sequential()
modelo.add(Dense(256, input_dim=256, activation='relu'))
modelo.add(Dense(128, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))

# Compilando o modelo com entropia cruzada como função de perda
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinando o modelo
modelo.fit(chaves_privadas, rotulos, epochs=10, batch_size=32, validation_split=0.2)
