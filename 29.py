import ecdsa
import hashlib
import base58

def calculate_match_percentage(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    min_len = min(len_str1, len_str2)
    matching_chars = sum(1 for c1, c2 in zip(str1, str2) if c1 == c2)

    return (matching_chars / min_len) * 100

def generate_bitcoin_keypair_range(start_hex, end_hex, target_address):
    start_int = int(start_hex, 16)
    end_int = int(end_hex, 16)

    max_match_percentage = 0
    max_match_address = ""

    with open("29Porcento.txt", "w") as file:
        for private_key_int in range(start_int, end_int + 16):
            private_key_hex = format(private_key_int, 'x').zfill(64)
            private_key_bytes = bytes.fromhex(private_key_hex)
            sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
            vk = sk.get_verifying_key()

            public_key_bytes = vk.to_string()
            sha256_hash = hashlib.sha256(public_key_bytes).digest()
            ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
            extended_hash = b'\x00' + ripemd160_hash
            checksum = hashlib.sha256(hashlib.sha256(extended_hash).digest()).digest()[:4]
            address_bytes = extended_hash + checksum
            bitcoin_address = base58.b58encode(address_bytes).decode()

            match_percentage = calculate_match_percentage(target_address, bitcoin_address)
            if match_percentage > max_match_percentage:
                max_match_percentage = match_percentage
                max_match_address = bitcoin_address

            print(f"Chave Privada (hexadecimal): {private_key_hex}")
            print(f"Endereço Bitcoin: {bitcoin_address}")
            print(f"Percentual de Correspondência: {match_percentage:.2f}%\n")

            if match_percentage > 16 and bitcoin_address.startswith("13"):
                file.write(f"Chave Privada (hexadecimal): {private_key_hex}\n")
                file.write(f"Endereco Bitcoin: {bitcoin_address}\n")
                file.write(f"Percentual de Correspondencia: {match_percentage:.2f}%\n")
                file.write("\n")

    print(f"Endereço com maior correspondência: {max_match_address}")
    print(f"Maior percentual de correspondência: {max_match_percentage:.2f}%")

if __name__ == "__main__":
    initial_private_key_hex = "000000000000000000000000000000000000000000000002000000000e8268e2"
    final_private_key_hex =   "000000000000000000000000000000000000000000000003ffffffffffffffff"
    target_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
    generate_bitcoin_keypair_range(initial_private_key_hex, final_private_key_hex, target_address)
