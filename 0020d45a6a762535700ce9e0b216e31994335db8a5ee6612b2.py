import hashlib

# Passo 3: Calcular o hash RIPED-160
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(address_no_checksum)
hashed_address = ripemd160.digest()

print("Endereço com hash RIPED-160:", hashed_address.hex())
