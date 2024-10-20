import hashlib
from decimal import Decimal, getcontext
from tqdm import tqdm

# Configura a precisão decimal para 78 casas
getcontext().prec = 78
CasaDecimal = 76

# Variáveis e constantes
target_hash = "739437bb3dd6d1983e66629c5f08c70e52769371"
fragmentos = ["739437", "bb3", "dd6d", "1983", "e66629", "c5f08", "c70", "e52769371"]

campoFinito = Decimal('115792089237316195423570985008687907853269984665640564039457584007908834671663')
porCento = Decimal('0.24' + '0' * 65 + '3110396332')  # Percentual inicial com 76 zeros
totaLoop = 1_000_000_000  # Máximo de iterações






def buscar_fragmentos(hashRIPEMD):

    """Busca as posições de fragmentos dentro do hash."""
    fragmentos = ["739437", "bb3", "dd6d", "1983", "e66629", "c5f08", "c70", "e52769371"]
    
    return {
        parte: (inicio, inicio + len(parte) - 1) 
        for parte in fragmentos 
        if (inicio := hashRIPEMD.find(parte)) != -1
    }





for _ in tqdm(range(totaLoop), desc="euBRASIL v:1.6", unit=" RIPEMD-160"):
                                                                # Calcula o valor proporcional ao percentual
    resultado = (porCento * campoFinito).to_integral_value()    # Garante que seja um valor inteiro

    """Gera um número inteiro com exatamente 77 dígitos a partir do valor dado."""
    numero = str(int(resultado % Decimal('1' + '0' * 77)))      # Usa o módulo para garantir 77 dígitos
    chavePublica = numero.zfill(77)                             # Preenche com zeros à esquerda, se necessário


    """Retorna o hash RIPEMD-160 de uma string de dados."""
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(chavePublica.encode('utf-8'))
    hash_resultado = ripemd160.hexdigest()


    # Exibe o progresso atual
    # print(f"{porCento:.77f}% : \nChave Pública: {chavePublica}, \nRIPEMD-160: {hash_resultado}")

    
    if hash_resultado.startswith("739437"):
        # Verifica se o hash gerado começa com o alvo
        posicionarFragmento = buscar_fragmentos(hash_resultado)

        print(f"\n")
        print(f"{porCento:.77f}% : \nChave Pública: {chavePublica}, \nRIPEMD-160: {hash_resultado}")
        print(f"Posicionar Fragmentos: {posicionarFragmento} \n")
    

    porCento += Decimal('0.' + '0' * CasaDecimal + '1')
        

