import ecdsa
from ecdsa.util import string_to_number

# 1. Definir os parâmetros da curva (secp256k1)
curve = ecdsa.SECP256k1
G = curve.generator
p = curve.curve.p()
a = curve.curve.a()

# 2. Chave privada fornecida (hexadecimal)
private_key_hex = "000000000000000000000000000000000000000000000003bbbbbbbc810d8540"
private_key = int(private_key_hex, 16)
print(f"Chave Privada: {hex(private_key)}")

# 3. Função de duplicação de ponto
def point_double(x1, y1):
    if y1 == 0:
        return (0, 0)
    s = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    x3 = (s * s - 2 * x1) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3

# 4. Função de adição de pontos
def point_add(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return point_double(x1, y1)
    if x1 == x2:
        return (0, 0)
    s = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3

# 5. Multiplicação escalar
def scalar_mult(k, G):
    x, y = G.x(), G.y()
    R_x, R_y = 0, 0  # Inicialmente o ponto no infinito
    Gx, Gy = x, y

    k_bin = bin(k)[2:]
    for bit in k_bin:
        R_x, R_y = point_double(R_x, R_y)
        if bit == '1':
            R_x, R_y = point_add(R_x, R_y, Gx, Gy)
        print(f"Rx: {hex(R_x)}")
        print(f"Ry: {hex(R_y)}")
    
    return R_x, R_y

# Ponto gerador G
Gx, Gy = G.x(), G.y()

# Realizando a multiplicação escalar
public_key_x, public_key_y = scalar_mult(private_key, G)
print(f"\nChave Pública (x): {hex(public_key_x)}")
print(f"Chave Pública (y): {hex(public_key_y)}")
