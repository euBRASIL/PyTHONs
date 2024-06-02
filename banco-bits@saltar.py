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
        
        if bit == '1' :
            credito = credito + 1

    return credito
    
    
def chavebitcoin(iniciohex, finalhex, premio):
    inicioint = int(iniciohex, 16)
    finalint  = int(finalhex, 16)
    step = 110000000  # Define o tamanho do passo para iterar de |10|000|000|

    numerocompleto = 0
    semChave = 0
    
    # wallet = ""
    
    salto = 11 # Este é um saldo relacional com os 9x números possiveis sem o Zero
    

    # Criar arquivo JSON com os resultados
    resultados_json = []  # Lista para armazenar os resultados
    with open(f"{iniciohex}.json", "a") as json_file:
        json.dump(resultados_json, json_file, indent=4)

    with open(f"{iniciohex}.txt", "a") as file:
        for batman in range(inicioint, finalint + 1, step):
            questao = min(batman + step - 1, finalint)
            for privadaint in tqdm(range(batman, questao + 1, salto), desc="Progresso", unit="chaves", file=sys.stdout):
                privadahex = format(privadaint, 'x').zfill(64)
                privadabyt  = bytes.fromhex(privadahex)

                saldo = analisar_chave(bin(privadaint)) # Função bin(converte), oct(converte) e hex(converte)
                
                if saldo > 25 : # Conta(bits) evita processos abaixo de determinada quantidade de bits

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
                    

                    if percentual > numerocompleto :
                        numerocompleto = percentual
                        wallet = bitcoin

                    if percentual > 26 and bitcoin.startswith("13"):
                        # tipo_saldo = "(C+)" if saldo > 0 else "(D-)"
                        valor_saldo = abs(saldo)

                        print(f"\nChave Privada (hexadecimal)  : {privadahex}")
                        print(f"Endereço Bitcoin  (credito)  : {bitcoin}")
                        print(f"Percentual de Correspondência: {percentual:.2f}%\n")
                        print(f"Conta(bits): {valor_saldo} bits \n")

                        file.write(f"Chave Privada (hexadecimal): {privadahex}\n")
                        file.write(f"Endereco Bitcoin (credito) : {bitcoin}\n")
                        file.write(f"Percentual de Correspondencia: {percentual:.2f}%\n")
                        file.write(f"Conta(bits): {valor_saldo} bits \n")
                        file.write("\n")

                        resultados_json.append({
                            "Chave Privada (hexadecimal)": privadahex,
                            "Endereco Bitcoin para crédito": bitcoin,
                            "Percentual de Correspondencia": f"{percentual:.2f}%"
                        })
                            
                        if( privadaint % 60259363973000000000 > 99000000 ): # Valor acumalativo de 100% / Distância de 100 milhões
                            privadaint = privadaint + 100000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 90000000 ): # Valor acumalativo de 90% / Distância de 90 milhões           
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 80000000 ) : # Valor acumalativo de 80% / Distância de 80 milhões      
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 70000000 ) : # Valor acumalativo de 70% / Distância de 70 milhões
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 60000000 ) : # Valor acumalativo de 60% / Distância de 60 milhões
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 50000000 ) : # Valor acumalativo de 50% / Distância de 50 milhões
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 40000000 ) : # Valor acumalativo de 40% / Distância de 40 milhões
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 30000000 ) : # Valor acumalativo de 30% / Distância de 30 milhões
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 20000000 ) : # Valor acumalativo de 20% / Distância de 20 milhões
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                            
                        if( privadaint % 60259363973000000000 > 10000000 ) : # Valor acumalativo de 10% / Distância de 10 milhões
                            privadaint = privadaint + 1000000 # Salto de 1% em uma Análise de 10.000.000 de Chaves Privadas
                        
                        
                        print("Distância (decimal) : ", privadaint)
                        semChave = 0
                        
                    else :
                        semChave = semChave + 1
                        
                        if semChave > 99000000 : privadaint + 10000000
                        if semChave > 90000000 : privadaint + 10000000
                        if semChave > 80000000 : privadaint + 10000000
                        if semChave > 70000000 : privadaint + 10000000
                        if semChave > 60000000 : privadaint + 10000000
                        if semChave > 50000000 : privadaint + 10000000
                        if semChave > 40000000 : privadaint + 10000000
                        if semChave > 30000000 : privadaint + 10000000
                        if semChave > 20000000 : privadaint + 10000000
                        if semChave > 10000000 : privadaint + 10000000

if __name__ == "__main__":
    iniciohex = "0000000000000000000000000000000000000000000000036666666600000000" 
    finalhex  = "0000000000000000000000000000000000000000000000036666666700000000" # Analisou em menos de 5 horas
    premio    = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
    chavebitcoin(iniciohex, finalhex, premio)


