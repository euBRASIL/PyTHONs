import requests

# Endereço Bitcoin
address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"

# URL da API do Blockchain.info para obter informações sobre UTXOs
url = f"https://blockchain.info/unspent?active={address}"

# Fazendo a requisição à API
response = requests.get(url)

# Verificando se a requisição foi bem sucedida
if response.status_code == 200:
    data = response.json()
    utxos = data['unspent_outputs']
    for utxo in utxos:
        print("Hash do Script:", utxo['script'])
else:
    print("Erro ao obter informações sobre UTXOs:", response.status_code)
