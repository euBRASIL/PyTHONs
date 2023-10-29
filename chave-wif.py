import hashlib
import base58

# Valor hexadecimal fornecido
hex_private_key = "0000000000000000000000000000000000000000000000030000000008641288"

# Adicionar o prefixo da versão (0x80)
wif_key_hex = "80" + hex_private_key

# Calcular o checksum (SHA-256 duas vezes e pegar os 4 bytes à esquerda)
checksum = hashlib.sha256(hashlib.sha256(bytes.fromhex(wif_key_hex)).digest()).digest()[:4]

# Adicionar o checksum à chave WIF
wif_key_hex += checksum.hex()

# Codificar em Base58
wif_key = base58.b58encode(bytes.fromhex(wif_key_hex)).decode()

print("Chave WIF:", wif_key)
