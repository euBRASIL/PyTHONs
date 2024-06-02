import base58
import hashlib

# Passo 1: Decodificar o endereço Base58
btc_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
decoded_address = base58.b58decode(btc_address)

print("Endereço decodificado:", decoded_address.hex())

# Passo 2: Remover o checksum
address_no_checksum = decoded_address[:-4]

print("Endereço sem checksum:", address_no_checksum.hex())

# Passo 3: Calcular o hash RIPED-160
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(address_no_checksum)
hashed_address = ripemd160.digest()

print("Endereço com hash RIPED-160:", hashed_address.hex())
