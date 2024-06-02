import hashlib
import base58

# Chave privada em hexadecimal
chavePrivadaHEX = "000000000000000000000000000000000000000000000003888888b0a23fc0fe"

# Prefixo para chave privada WIF (mainnet)
prefixoWIF = "80" # Número (decimal) 128 convertido para HEX é 80

# Concatenar o prefixo da chave privada com a chave privada em hexadecimal
chavePrefixo = prefixoWIF + chavePrivadaHEX

# Calcular o checksum da chave privada estendida
checksum = hashlib.sha256(hashlib.sha256(bytes.fromhex(chavePrefixo)).digest()).digest()[:4] # 2xSHA256 + CheckSum

# Adicionar o checksum à chave privada estendida
chaveWIF = chavePrefixo + checksum.hex()

# Codificar a chave privada WIF
formatoWIF = base58.b58encode(bytes.fromhex(chaveWIF)).decode() #

print(f"Chave Privada WIF: {formatoWIF}")
