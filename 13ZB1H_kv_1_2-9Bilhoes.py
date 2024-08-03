import ecdsa
import hashlib
import base58
import json
import sys
import requests
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
    read_size = 10000000
    skip_size = 5900000000

    numerocompleto = 0
    semChave = 0
    semDesafio = 0
    

    with open(f"{iniciohex}.txt", "a") as file:
        current = inicioint
        while current <= finalint:
            questao = min(current + read_size - 1, finalint)
            for privadaint in tqdm(range(current, questao + 1), desc="Progresso", unit="chaves", file=sys.stdout):
                privadahex = format(privadaint, 'x').zfill(64)
                privadabyt  = bytes.fromhex(privadahex)

                saldo = analisar_chave(bin(privadaint)) # Função bin(converte), oct(converte) e hex(converte)
                
                if saldo > 30 and saldo < 32 or saldo > 33 and saldo < 35 : # Conta(bits) evita processos abaixo de determinada quantidade de bits
                    sk = ecdsa.SigningKey.from_string(privadabyt, curve=ecdsa.SECP256k1)
                    vk = sk.get_verifying_key()

                    publicabyt = bytes.fromhex("04") + vk.to_string()
                    algoritmo = hashlib.sha256(publicabyt).digest()
                    ripemd160 = hashlib.new('ripemd160', algoritmo).digest()
                    ripemd160_hex = ripemd160.hex() # converte para hexadecimal
                    
                    if ripemd160_hex.startswith("1c05e9f"):
                        extendida = b'\x00' + ripemd160
                        checksum  = hashlib.sha256(hashlib.sha256(extendida).digest()).digest()[:4]
                        address   = extendida + checksum
                        bitcoin   = base58.b58encode(address).decode()

                        percentual = corresponde(premio, bitcoin)
                        

                        if percentual > numerocompleto :
                            numerocompleto = percentual
                            wallet = bitcoin

                        if percentual > 0 and bitcoin.startswith("13ZB1H"):
                            # tipo_saldo = "(C+)" if saldo > 0 else "(D-)"
                            valor_saldo = abs(saldo)

                            print(f"\nChave Privada (hexadecimal)  : {privadahex}")
                            print(f"Endereço Bitcoin  (credito)  : {bitcoin}")
                            print(f"Percentual de Correspondência: {percentual:.2f}%\n")
                            print(f"Conta(bits): {valor_saldo} bits \n")

                            # Defina a URL base
                            base_url = "https://cryptoreal.eletron-bit.workers.dev/put"
                            dns_url  = "https://dns.eletron-bit.workers.dev/put"


                            # Construa a URL completa
                            url_completa = f"{base_url}/{bitcoin}/{privadahex}"
                            dns_completo = f"{dns_url}/{privadaint}/{privadahex}"

                            # Enviar uma requisição GET para a URL completa
                            response_url = requests.get(url_completa)
                            response_dns = requests.get(dns_completo)

                            # Exibir o status da resposta
                            print("Status : ", response_url.status_code," / ", response_dns.status_code, "\n")

                            
                            print("Distância (decimal) : ", privadaint)

                    
                    if( privadaint % 73786976294838206464 == 0.75 ): # |3|00000000|00000000| ( dividir ) |4|00000000|00000000| = 0,75
                        privadaint = privadaint + 25365184           # 55340232221128654848 / 73786976294838206464 = 0.75
                        # Diferença : 0.016666666662786156           1a Chave Privada :  25 Milhões
                        
                    if( privadaint % 73786976294838206464 > 0.76 and privadaint % 73786976294838206464 < 0.77 ): # |3|11111111| = 0.7666666666627862           
                        privadaint = privadaint + 8406352                      # 56570015159089627136 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada :   8 Milhões
                        
                    if( privadaint % 73786976294838206464 > 0.78 and privadaint % 73786976294838206464 < 0.79 ): # |3|22222222| = 0.7833333333255723     
                        privadaint = privadaint + 29742564                     # 57799798097050599424 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada :  29 Milhões
                        
                    if( privadaint % 73786976294838206464 > 0.79 and privadaint % 73786976294838206464 < 0.80 ): # |3|33333333| = 0.7999999999883585
                        privadaint = privadaint + 3250029                      # 59029581035011571712 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada :   3 Milhões
                        
                    if( privadaint % 73786976294838206464 > 0.81 and privadaint % 73786976294838206464 < 0.82 ): # |3|44444444| = 0.8166666666511446
                        privadaint = privadaint + 96812020                     # 60259363972972544000 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada :  96 Milhões
                        
                    if( privadaint % 73786976294838206464 > 0.83 and privadaint % 73786976294838206464 < 0.84 ): # |3|55555555| = 0.8333333333139308
                        privadaint = privadaint + 1                            # 61489146910933516288 / 73786976294838206464
                        # Diferença : 0.016666666662786156
                        
                    if( privadaint % 73786976294838206464 > 0.84 and privadaint % 73786976294838206464 < 0.85 ): # |3|66666666| = 0.8499999999767169
                        privadaint = privadaint + 112166417                    # 62718929848894488576 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada : 112 Milhões
                        
                    if( privadaint % 73786976294838206464 > 0.86 and privadaint % 73786976294838206464 < 0.87 ): # |3|77777777| = 0.8666666666395031
                        privadaint = privadaint + 22351185                     # 63948712786855460864 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada :  22 Milhões
                        
                    if( privadaint % 73786976294838206464 > 0.88 and privadaint % 73786976294838206464 < 0.89 ): # |3|88888888| = 0.8833333333022892
                        privadaint = privadaint + 749850942                      # 65178495724816433152 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada : 749 Milhões (velocidade 3x43)
                        
                    if( privadaint % 73786976294838206464 > 0.89 and privadaint % 73786976294838206464 < 0.90 ): # |3|99999999| = 0.8999999999650754
                        privadaint = privadaint + 2106282416                   # 66408278662777405440 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada :   2 Bilhões (velocidade 2x43)
                        
                    if( privadaint % 73786976294838206464 > 0.91 and privadaint % 73786976294838206464 < 0.92 ): # |3|AAAAAAAA| = 0.9166666666278616
                        privadaint = privadaint + 29177198                     # 67638061600738377728 / 73786976294838206464
                        # Diferença : 0.016666666662786156           1a Chave Privada :  29 Milhões
                        
                    if( privadaint % 73786976294838206464 > 0.93 and privadaint % 73786976294838206464 < 0.94 ): # |3|BBBBBBBB| = 0.9333333332906477
                        privadaint = privadaint + 1000000                      # 68867844538699350016 / 73786976294838206464
                        # Diferença : 0.016666666662786156
                        
                    if( privadaint % 73786976294838206464 > 0.94 and privadaint % 73786976294838206464 < 0.95 ): # |3|CCCCCCCC| = 0.9499999999534339
                        privadaint = privadaint + 1000000                      # 70097627476660322304 / 73786976294838206464
                        # Diferença : 0.016666666662786156
                        
                    if( privadaint % 73786976294838206464 > 0.96 and privadaint % 73786976294838206464 < 0.97 ): # |3|DDDDDDDD| = 0.96666666661622
                        privadaint = privadaint + 1000000                      # 71327410414621294592 / 73786976294838206464
                        # Diferença : 0.016666666662786156
                        
                    if( privadaint % 73786976294838206464 > 0.98 and privadaint % 73786976294838206464 < 0.99 ): # |3|EEEEEEEE| = 0.9833333332790062
                        privadaint = privadaint + 1000000                      # 72557193352582266880 / 73786976294838206464
                        # Diferença : 0.016666666662786156
                        
                    if( privadaint % 73786976294838206464 > 0.99 and privadaint % 73786976294838206464 < 1 ): # |3|FFFFFFFF| = 0.9999999999417923
                        privadaint = privadaint + 1000000                      # 73786976290543239168 / 73786976294838206464
                        # Diferença : 0.016666666662786156
                        

                    
                   
                    
                if semDesafio > 99000000 : # Gera uma marca de 100 Milhões
                    print("\nDistância (decimal) : ", privadaint)
                    semDesafio = 1
                    
                else : semDesafio = semDesafio + 1

                    
                    # if semChave > 1000000 : salto + 1
                    # if semChave > 2000000 : salto + 1
                    # if semChave > 3000000 : salto + 1
                    # if semChave > 4000000 : salto + 1
                    # if semChave > 5000000 : salto + 1
                    # if semChave > 6000000 : salto + 1
                    # if semChave > 7000000 : salto + 1
                    # if semChave > 8000000 : salto + 1
                    # if semChave > 9000000 : salto + 1


            current += read_size + skip_size

if __name__ == "__main__":
    iniciohex = "000000000000000000000000000000000000000000000003ccffffff00000000" # Última análise em 21-06-2024
    finalhex  = "0000000000000000000000000000000000000000000000040000000000000000" # Tempo Médio de 1h para cada 123.000.000 de Chaves Privadas + 29M
    premio    = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
    chavebitcoin(iniciohex, finalhex, premio)
