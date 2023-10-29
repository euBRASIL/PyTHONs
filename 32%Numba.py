import ecdsa
import hashlib
import base58
import json
import sys
from tqdm import tqdm
from numba import njit

def corresponde(str1, str2):
    lenstr1 = len(str1)
    lenstr2 = len(str2)

    caractere = min(lenstr1, lenstr2)
    palavra = sum(1 for cara, caro in zip(str1, str2) if cara == caro)

    return (palavra / caractere) * 100


def chavebitcoin(inicioint, finalint, premio):
    numerocompleto = 0
    wallet = ""

    resultados_json = []

    for batman in range(inicioint, finalint + 1, step):
        questao = min(batman + step - 1, finalint)
        for privadaint in tqdm(range(batman, questao + 1), desc="Progresso", unit="chaves", file=sys.stdout):
            privadahex = format(privadaint, 'x').zfill(64)
            privadaby = bytes.fromhex(privadahex)

            sk = ecdsa.SigningKey.from_string(privadaby, curve=ecdsa.SECP256k1)
            vk = sk.get_verifying_key()

            wif = base58.b58encode_check(b'\x80' + privadaby).decode()

            publicaby = vk.to_string()
            algoritmo = hashlib.sha256(publicaby).digest()
            ripemd160 = hashlib.new('ripemd160', algoritmo).digest()
            extendida = b'\x00' + ripemd160
            checksum = hashlib.sha256(hashlib.sha256(extendida).digest()).digest()[:4]
            address = extendida + checksum
            bitcoin = base58.b58encode(address).decode()

            percentual = corresponde(premio, bitcoin)
            if percentual > numerocompleto:
                numerocompleto = percentual
                wallet = bitcoin

            if percentual > 26 and bitcoin.startswith("13"):
                print("\nChave Privada (hexadecimal):", privadahex)
                print("Chave Privada (WIF):", wif)
                print("Endereço Bitcoin:", bitcoin)
                print("Percentual de Correspondência: {:.2f}%\n")

if __name__ == "__main__":
    iniciohex = "000000000000000000000000000000000000000000000003000222220071222a"
    finalhex =  "0000000000000000000000000000000000000000000000030002222211111111"
    premio =    "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
    
    inicioint = int(iniciohex, 32)
    finalint = int(finalhex, 32)
    step = 10000000
    
    chavebitcoin(inicioint, finalint, premio)
