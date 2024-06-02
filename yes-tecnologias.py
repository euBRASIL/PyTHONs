import ecdsa
import hashlib
import base58
import json
import sys

# Passo 1: Decodificar o endereço Base58
btc_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
decoded_address = base58.b58decode(btc_address)

print("Endereço  decodificado :", decoded_address.hex())

# Passo 2: Remover o checksum
address_no_checksum = decoded_address[:-4]

print("Endereço  sem  checksum:", address_no_checksum.hex())

# Passo 3: Calcular o hash RIPED-160
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(address_no_checksum)
hashed_address = ripemd160.digest()

print("Endereço hash RIPED-160:", hashed_address.hex())

# Passo 4: Adicionar a versão de rede
version_byte = b'\x00' # Versão de rede para Bitcoin Mainnet
hashed_address_with_version = version_byte + hashed_address

print("Endereço versão de rede:", hashed_address_with_version.hex())

# Passo 5: Calcular o checksum
checksum = hashlib.sha256(hashlib.sha256(hashed_address_with_version).digest()).digest()[:4]

# Passo 6: Adicionar o checksum ao final do hash
binary_address = hashed_address_with_version + checksum

print("Endereço  ( CheckSum ) :", binary_address.hex())

# Passo 7: Conversão para Base58
btc_public_key = base58.b58encode(binary_address)

print("Chave Pública Bitcoin  :", btc_public_key.decode())


publicabyt = bytes.fromhex("04") + btc_public_key
algoritmo = hashlib.sha256(publicabyt).digest()
ripemd160 = hashlib.new('ripemd160', algoritmo).digest()
extendida = b'\x00' + ripemd160
checksum  = hashlib.sha256(hashlib.sha256(extendida).digest()).digest()[:4]
address   = extendida + checksum
bitcoin   = base58.b58encode(address).decode()



print(f"Address (validar) BTC  : {bitcoin}")


