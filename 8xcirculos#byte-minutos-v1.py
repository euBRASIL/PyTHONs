import random

# Defina os valores mínimo e máximo em minutos
minutos_min = 200000000
minutos_max = 400000000

# Defina o número de chaves a serem geradas
num_chaves = 10  # Você pode ajustar isso para a quantidade desejada

# Função para representar uma chave em formato de círculos e minutos
def representar_chave(chave):
    minutos = int(chave[:8])
    circulos = chave[8:]
    
    representacao = f'{minutos} minutos, círculos: {circulos}'
    return representacao

# Gere e exiba as chaves privadas
for _ in range(num_chaves):
    minutos = random.randint(minutos_min, minutos_max)  # Gera minutos aleatórios dentro do intervalo
    minutos_str = f'{minutos:08}'

    # Gera círculos aleatórios nas próximas 8 casas hexadecimais dentro do intervalo
    circulos_hex = ''.join(random.choice("0123456789ABCDEF") for _ in range(8))

    chave_privada = minutos_str + circulos_hex
    representacao = representar_chave(chave_privada)
    print(representacao)
