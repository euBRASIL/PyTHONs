import pyttsx3
import openai


openai.api_key = "APIKEY"
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)



def conversar(texto):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Suponha que você é um instrutor de Python."},
            {"role": "user", "content": texto},
        ],
        temperature=0.7,
    )
    return resposta['choices'][0]['message']['content']


while True:
    prompt = input("Usuário: ")
    resposta_chatgpt = conversar(prompt)

    engine.say(resposta_chatgpt)
    engine.runAndWait()

    print("Bot: " + resposta_chatgpt)
