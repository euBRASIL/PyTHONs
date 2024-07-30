import hashlib
import ecdsa
import base58
import matplotlib.pyplot as plt

# Lista das chaves privadas em hexadecimal
chaves_privadas_hex = [
    '000000000000000000000000000000000000000000000003bbbbbbbc810d8540',
    '000000000000000000000000000000000000000000000003bbbbbbc0a43135a0',
    '000000000000000000000000000000000000000000000003bbbbbbc70d030883',
    '000000000000000000000000000000000000000000000003cccccccc846af87a',
    '000000000000000000000000000000000000000000000003cccccccc59a2bf0c',
    '000000000000000000000000000000000000000000000003eeeeeef13c301420',
    '000000000000000000000000000000000000000000000003eeef00005b3ea8f6',
    '000000000000000000000000000000000000000000000003eeef0000adc3d1eb',
    '000000000000000000000000000000000000000000000003eeef0000cd745eea',
    '000000000000000000000000000000000000000000000003aaa00000ff75eef7',
    '000000000000000000000000000000000000000000000003aaaa00015fe32a77',
    '000000000000000000000000000000000000000000000003aaaaa0000ee373be',
]

# Função para converter uma chave privada em um endereço público de Bitcoin
def chave_privada_para_endereco(chave_privada_hex):
    # Converter a chave privada de hexadecimal para bytes
    priv_key_bytes = bytes.fromhex(chave_privada_hex)
    
    # Gerar a chave pública a partir da chave privada
    sk = ecdsa.SigningKey.from_string(priv_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    pub_key_bytes = b'\04' + vk.to_string()
    
    # Realizar o SHA-256 da chave pública
    sha256_1 = hashlib.sha256(pub_key_bytes).digest()
    
    # Realizar o RIPEMD-160 do resultado do SHA-256
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_1)
    hash160 = ripemd160.digest()
    
    # Adicionar o prefixo de versão
    prefixo_versao = b'\00' + hash160
    
    # Realizar o SHA-256 duplo do prefixo de versão
    sha256_2 = hashlib.sha256(prefixo_versao).digest()
    sha256_3 = hashlib.sha256(sha256_2).digest()
    
    # Adicionar os 4 bytes de checksum
    checksum = sha256_3[:4]
    endereco_binario = prefixo_versao + checksum
    
    # Converter para base58
    endereco = base58.b58encode(endereco_binario)
    
    return {
        'chave_privada': chave_privada_hex,
        'sha256_1': sha256_1.hex(),
        'ripemd160': hash160.hex(),
        'sha256_2': sha256_2.hex(),
        'sha256_3': sha256_3.hex(),
        'checksum': checksum.hex(),
        'base58': endereco.decode('utf-8')
    }

# Processar as chaves privadas e converter para endereços públicos
enderecos_info = [chave_privada_para_endereco(chave) for chave in chaves_privadas_hex]

# Exibir as informações geradas para cada chave privada
for info in enderecos_info:
    print(f"Chave Privada: {info['chave_privada']}")
    print(f"SHA-256 1: {info['sha256_1']}")
    print(f"RIPEMD-160: {info['ripemd160']}")
    print(f"SHA-256 2: {info['sha256_2']}")
    print(f"SHA-256 3: {info['sha256_3']}")
    print(f"Checksum: {info['checksum']}")
    print(f"Base58: {info['base58']}")
    print("\n")

# Visualizar as chaves correspondentes em curvas elípticas
def plot_curva_eliptica(chave_privada_hex):
    priv_key_bytes = bytes.fromhex(chave_privada_hex)
    sk = ecdsa.SigningKey.from_string(priv_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    return vk

plt.figure(figsize=(10, 10))
for i, info in enumerate(enderecos_info):
    vk = plot_curva_eliptica(info['chave_privada'])
    pub_key_bytes = vk.to_string()
    x, y = ecdsa.util.string_to_number(pub_key_bytes[:32]), ecdsa.util.string_to_number(pub_key_bytes[32:])
    plt.plot(x, y, 'o', label=f'Chave {i+1}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curvas Elípticas das Chaves Privadas')
plt.legend()
plt.grid()
plt.show()
