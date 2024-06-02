import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/9cbf53862dadd478b0c02799c21bf20d/ai/run/"
headers = {"Authorization": "Bearer ntYfR80FOjze9EJOjv6UK1A8iENQYaqQuC9QwkqE"}

pergunta = input("Digite a sua pergunta para o CloudFlare ChatGPT3.5 ?")

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

    


inputs = [
    { "role": "system", "content": f"{pergunta}" },
    { "role": "user", "content": "Liste todas as etapas com um pequeno resumo"}
];
output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
print(output['result'])

if( output['success'] == True ) : print( "ChatGPT : Ok" )