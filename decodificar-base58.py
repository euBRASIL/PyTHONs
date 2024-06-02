import base58

# Passo 1: Decodificar o endereço Base58
btc_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
decoded_address = base58.b58decode(btc_address)

print("Endereço decodificado:", decoded_address.hex())
