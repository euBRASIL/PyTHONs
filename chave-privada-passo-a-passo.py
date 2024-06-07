import ecdsa
import binascii
from ecdsa.util import string_to_number

# 1. Definir os parâmetros da curva (secp256k1)
curve = ecdsa.SECP256k1

# 2. Chave privada fornecida (hexadecimal)
private_key_hex = "000000000000000000000000000000000000000000000003bbbbbbbc810d8540"
private_key = int(private_key_hex, 16)
print(f"Chave Privada: {hex(private_key)}")

# 3. Calcular a chave pública pela multiplicação do ponto gerador
point = private_key * curve.generator

# A chave pública é um ponto na curva, representado por suas coordenadas x e y
public_key_x = point.x()
public_key_y = point.y()
print(f"Chave Pública (x): {hex(public_key_x)}")
print(f"Chave Pública (y): {hex(public_key_y)}")

# 4. Mostrar as etapas intermediárias
print("\nEtapas Intermediárias:")

# Representação binária da chave privada
private_key_bin = bin(private_key)[2:].zfill(curve.order.bit_length())
print(f"Chave Privada em Binário: {private_key_bin}")

# Função de duplicação de ponto
def point_double(x1, y1, p, a):
    s = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    x3 = (s * s - 2 * x1) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3

# Função de adição de pontos
def point_add(x1, y1, x2, y2, p):
    s = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3

# Multiplicação escalar
Gx, Gy = curve.generator.x(), curve.generator.y()
a, p = curve.curve.a(), curve.curve.p()

Rx, Ry = 0, 0  # ponto no infinito (identidade aditiva)
addend_x, addend_y = Gx, Gy

for bit in private_key_bin:
    if Rx == 0 and Ry == 0:
        Rx, Ry = addend_x, addend_y
    else:
        Rx, Ry = point_double(Rx, Ry, p, a)
    
    if bit == '1':
        Rx, Ry = point_add(Rx, Ry, addend_x, addend_y, p)
    
    print(f"Rx: {hex(Rx)}")
    print(f"Ry: {hex(Ry)}")

# Verificação final
assert (Rx, Ry) == (public_key_x, public_key_y)
print("\nVerificação: A chave pública derivada está correta.")
