import ecdsa
import hashlib
import base58
import json
import sys
from tqdm import tqdm

# global contabits

def corresponde(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    min_len = min(len_str1, len_str2)
    matching_chars = sum(1 for c1, c2 in zip(str1, str2) if c1 == c2)
    return (matching_chars / min_len) * 100

def analisar_chave(chave):
    credito = 0
    for bit in chave:
        if bit == '1':
            credito += 1
        else:
            credito -= 1
    return credito

def chavebitcoin(iniciohex, finalhex, premio):
    inicioint = int(iniciohex, 16)
    finalint  = int(finalhex, 16)
    step = 10000000  # Define o tamanho do passo para iterar de |10|000|000|

    numerocompleto = 0
    wallet = ""

    # Criar arquivo JSON com os resultados
    resultados_json = []  # Lista para armazenar os resultados
    with open(f"{iniciohex}.json", "a") as json_file:
        json.dump(resultados_json, json_file, indent=4)

    with open(f"{iniciohex}.txt", "a") as file:
        for batman in range(inicioint, finalint + 1, step):
            questao = min(batman + step - 1, finalint)
            for privadaint in tqdm(range(batman, questao + 1), desc="Progresso", unit="chaves", file=sys.stdout):
                privadahex = format(privadaint, 'x').zfill(64)
                privadabyt  = bytes.fromhex(privadahex)

                sk = ecdsa.SigningKey.from_string(privadabyt, curve=ecdsa.SECP256k1)
                vk = sk.get_verifying_key()

                publicabyt = bytes.fromhex("04") + vk.to_string()
                algoritmo = hashlib.sha256(publicabyt).digest()
                ripemd160 = hashlib.new('ripemd160', algoritmo).digest()
                extendida = b'\x00' + ripemd160
                checksum  = hashlib.sha256(hashlib.sha256(extendida).digest()).digest()[:4]
                address   = extendida + checksum
                bitcoin   = base58.b58encode(address).decode()

                percentual = corresponde(premio, bitcoin)
                saldo = analisar_chave(privadahex)
                
                if saldo > 0:
                    if percentual > numerocompleto :
                        numerocompleto = percentual
                        wallet = bitcoin

                    if percentual > 26 and bitcoin.startswith("13"):
                        tipo_saldo = "(C+)" if saldo > 0 else "(D-)"
                        valor_saldo = abs(saldo)

                        print(f"\nChave Privada (hexadecimal): {privadahex}")
                        print(f"Endereço Bitcoin(credito): {bitcoin}")
                        print(f"Percentual de Correspondência: {percentual:.2f}%\n")
                        print(f"Conta(bits): {valor_saldo} bits {tipo_saldo}\n")

                        file.write(f"Chave Privada (hexadecimal): {privadahex}\n")
                        file.write(f"Endereco Bitcoin (credito): {bitcoin}\n")
                        file.write(f"Percentual de Correspondencia: {percentual:.2f}%\n")
                        file.write(f"Conta(bits): {valor_saldo} bits {tipo_saldo}\n")
                        file.write("\n")

                        resultados_json.append({
                            "Chave Privada (hexadecimal)": privadahex,
                            "Endereco Bitcoin para crédito": bitcoin,
                            "Percentual de Correspondencia": f"{percentual:.2f}%"
                        })
                
                elif saldo < 0:
                    if percentual > numerocompleto :
                        numerocompleto = percentual
                        wallet = bitcoin

                    if percentual > 26 and bitcoin.startswith("13"):
                        tipo_saldo = "(C+)" if saldo > 0 else "(D-)"
                        valor_saldo = abs(saldo)

                        print(f"\nChave Privada (hexadecimal): {privadahex}")
                        print(f"Endereço Bitcoin (debito): {bitcoin}")
                        print(f"Percentual de Correspondência: {percentual:.2f}%\n")
                        print(f"Conta(bits): {valor_saldo} bits {tipo_saldo}\n")

                        file.write(f"Chave Privada (hexadecimal): {privadahex}\n")
                        file.write(f"Endereco Bitcoin (debito): {bitcoin}\n")
                        file.write(f"Percentual de Correspondencia: {percentual:.2f}%\n")
                        file.write(f"Conta(bits): {valor_saldo} bits {tipo_saldo}\n")
                        file.write("\n")

                        resultados_json.append({
                            "Chave Privada (hexadecimal)": privadahex,
                            "Endereco Bitcoin (debito) ": bitcoin,
                            "Percentual de Correspondencia": f"{percentual:.2f}%"
                        })

if __name__ == "__main__":
    iniciohex = "0000000000000000000000000000000000000000000000030000000000000000" 
    finalhex  = "0000000000000000000000000000000000000000000000040000000000000000"
    premio    = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
    chavebitcoin(iniciohex, finalhex, premio)


