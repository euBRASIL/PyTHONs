import hashlib
import base58

def private_key_to_wif(private_key_hex):
    version = b'\x80'  # Byte de versão para chave privada principal
    extended_key_hex = version + bytes.fromhex(private_key_hex)
    checksum = hashlib.sha256(hashlib.sha256(extended_key_hex).digest()).digest()[:4]
    wif = base58.b58encode(extended_key_hex + checksum).decode()
    return wif

private_key_hex = "0000000000000000000000000000000000000000000000030000000008641288"
wif = private_key_to_wif(private_key_hex)
print("Chave Privada WIF:", wif)
