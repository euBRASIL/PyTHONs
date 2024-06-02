import hashlib
import ecdsa

# Função para realizar o espelhamento (complemento de dois)
def complemento_dois(hex_str):
    return ''.join('0' if c == '1' else '1' for c in hex_str)

# Função para calcular o ponto público a partir da chave privada
def calcular_ponto_publico(chave_privada_hex):
    # Converte a chave privada hexadecimal em um número inteiro
    chave_privada = int(chave_privada_hex, 16)
    
    # Gera a chave pública usando a curva elíptica secp256k1 (usada pelo Bitcoin)
    sk = ecdsa.SigningKey.from_string(chave_privada.to_bytes(32, 'big'), curve=ecdsa.SECP256k1)
    chave_publica = sk.verifying_key.to_string('compressed')
    
    # Retorna a chave pública comprimida como uma string hexadecimal
    return chave_publica.hex()

# Função para espelhar a chave pública
def espelhar_chave_publica(chave_publica_hex):
    # Converte a chave pública hexadecimal em uma string binária
    chave_publica_bin = bin(int(chave_publica_hex, 16))[2:].zfill(256)
    
    # Calcula o complemento de dois da chave pública binária
    chave_publica_espelhada_bin = complemento_dois(chave_publica_bin)
    
    # Retorna a chave pública espelhada como uma string hexadecimal
    return hex(int(chave_publica_espelhada_bin, 2))[2:]

# Chave privada de exemplo (em hexadecimal)
chave_privada_hex = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140'

# Calcula a chave pública correspondente
chave_publica_hex = calcular_ponto_publico(chave_privada_hex)

# Espelha a chave pública
chave_publica_espelhada_hex = espelhar_chave_publica(chave_publica_hex)

# Exibe os resultados
print("Chave privada:", chave_privada_hex)
print("Chave pública:", chave_publica_hex)
print("Chave pública espelhada:", chave_publica_espelhada_hex)
