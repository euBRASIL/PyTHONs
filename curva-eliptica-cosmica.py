import matplotlib.pyplot as plt
import numpy as np
from ecdsa.ellipticcurve import Point, CurveFp
from ecdsa.curves import SECP256k1

# Número cósmico com 78 casas decimais
numero_cozmico = 123456789012345678901234567890123456789 * 987654321098765432109876543210987654321

# Converter para anos-luz
# 1 segundo ≈ 3.16887e-8 anos-luz
distancia_cozmica_al = numero_cozmico * 3.16887e-8

# Chave privada baseada no número cósmico
private_key_int = numero_cozmico

# Curva elíptica SECP256k1
curve = SECP256k1

# Ponto base na curva
G = curve.generator

# Multiplicação escalar para obter o ponto público
public_point = G * private_key_int

# Extrair coordenadas x e y do ponto público
x_point = public_point.x()
y_point = public_point.y()

# Plotar o ponto na curva elíptica em anos-luz
plt.figure(figsize=(8, 6))
plt.plot(x_point, y_point, marker='o', color='b')
plt.title("Curva Elíptica SECP256k1 em Anos-Luz")
plt.xlabel("Anos-Luz")
plt.ylabel("Anos-Luz")
plt.grid(True)
plt.tight_layout()
plt.show()
