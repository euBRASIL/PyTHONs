import math

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def hex_to_decimal(hex_value):
    return int(hex_value, 16)

def sigmoid_for_hex(hex_value):
    decimal_value = hex_to_decimal(hex_value)
    scaled_value = decimal_value / 15.0  # Normaliza para intervalo entre 0 e 1
    return sigmoide(scaled_value)

# Função para imprimir o tabuleiro com os valores sigmóides
def print_chessboard():
    print("╔═════════════════════════╗")
    for i in range(16):
        row = "║"
        for j in range(16):
            hex_value = hex(i * 16 + j)[2:].upper().zfill(2)
            sigmoid_result = sigmoid_for_hex(hex_value)
            # Ajusta o valor para encaixar no espaço
            value_str = f"{sigmoid_result:.2f}".ljust(5)
            row += f" {value_str}"
        row += " ║"
        print(row)
    print("╚═════════════════════════╝")

# Imprime o tabuleiro
print_chessboard()
