import speech_recognition as sr

# Recognizer
# Microphone

rec = sr.Recognizer()
# Funciona como abrir um Arquivo
# mic = sr.Microphone()

print(sr.Microphone().list_microphone_names())

with sr.Microphone() as mic:
	rec.adjust_for_ambient_noise(mic)
	print("Pode falar que eu vou gravar ...\n")
	audio = rec.listen(mic)
	texto = rec.recognize_google(audio, language="pt-BR")
	print(texto)
