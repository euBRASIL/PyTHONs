def decompress_public_key(compressed_key):
    # Removendo o prefixo '04'
    compressed_key = compressed_key[2:]
    # Obtendo a coordenada x e os bytes indicando a paridade de y
    x_bytes = compressed_key[:64]
    y_parity = int(compressed_key[64:], 16)
    
    # Convertendo as coordenadas x e y para inteiros
    x = int(x_bytes, 16)
    
    # Recuperando a coordenada y a partir da coordenada x e sua paridade
    p = 2**256 - 2**32 - 977
    y_square = (pow(x, 3, p) + 7) % p
    y = modular_sqrt(y_square, p)
    
    # Verificando a paridade de y
    if (y & 1) != y_parity:
        y = p - y
    
    return x, y

# Função para verificar se um número é um quadrado perfeito em um corpo finito
def is_quadratic_residue(n, p):
    return pow(n, (p - 1) // 2, p) == 1

# Função para calcular a raiz quadrada modular
def modular_sqrt(a, p):
    if is_quadratic_residue(a, p):
        return pow(a, (p + 1) // 4, p)
    else:
        raise ValueError("Não há raiz quadrada modular para este número.")

# Chave pública comprimida
compressed_public_key = "04104b35d403d49711c31d0a8b73dc3728a13c7aa1512b7b0993e950ea58a59584bb634a302284dc6b680f9b747824240eae1999ba8a4a68e366afc47387b0273964"

# Convertendo a chave pública comprimida em coordenadas x e y
x, y = decompress_public_key(compressed_public_key)
print("Coordenadas x e y:")
print("x:", x)
print("y:", y)
