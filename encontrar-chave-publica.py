import requests

def get_utxo_info(address):
    # API endpoint para buscar informações de transações não gastas (UTXO)
    api_url = f'https://blockchain.info/unspent?active={address}'
    
    try:
        response = requests.get(api_url)
        data = response.json()
        if 'unspent_outputs' in data and len(data['unspent_outputs']) > 0:
            # Extrair informações da primeira transação não gasta
            utxo = data['unspent_outputs'][0]
            return utxo
        else:
            print("Nenhuma transação não gasta encontrada para este endereço.")
            return None
    except Exception as e:
        print("Ocorreu um erro ao buscar informações da transação:", e)
        return None

def print_utxo_info(utxo):
    if utxo:
        print("Informações da UTXO:")
        print(f"Hash da Transação: {utxo['tx_hash']}")
        print(f"Índice da Saída: {utxo['tx_output_n']}")
        print(f"Valor (em satoshis): {utxo['value']}")
        print(f"Script Público: {utxo['script']}")
    else:
        print("Não foi possível encontrar informações da UTXO.")

# Endereço Bitcoin fornecido
address = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'

# Buscar informações da UTXO associada ao endereço
utxo_info = get_utxo_info(address)

# Exibir informações da UTXO
print_utxo_info(utxo_info)
