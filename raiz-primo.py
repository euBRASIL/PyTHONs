from decimal import Decimal, getcontext

# Define a precisão decimal
getcontext().prec = 100  # Ajuste a precisão conforme necessário

# Função para encontrar uma aproximação da raiz quadrada usando o método de Newton
def square_root(n, precision=10):
    x = Decimal(n) / 2  # Estimativa inicial: metade do número
    for _ in range(precision):
        x = (x + Decimal(n) / x) / 2  # Aplica o método de Newton
    return x

# Número primo gigantesco para encontrar a raiz quadrada
p = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


# Encontrar uma aproximação da raiz quadrada do número primo gigantesco
approx_sqrt = square_root(p)

# Imprimir a aproximação da raiz quadrada
print("Aproximação da raiz quadrada:", approx_sqrt)
