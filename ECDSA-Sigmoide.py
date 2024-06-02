# Função para verificar se um número é um quadrado perfeito em um corpo finito
def is_quadratic_residue(n, p):
    return pow(n, (p - 1) // 2, p) == 1

# Função para calcular a raiz quadrada modular
def modular_sqrt(a, p):
    if is_quadratic_residue(a, p):
        return pow(a, (p + 1) // 4, p)
    else:
        raise ValueError("Não há raiz quadrada modular para este número.")

# Função para calcular a inclinação da tangente em um ponto na curva elíptica
def tangent_slope(x, y, a, p):
    return (3 * x**2 + a) * pow(2 * y, -1, p) % p

# Parâmetros da curva elíptica
a = 2
p = 17

# Ponto inicial
x_0, y_0 = 3, 1

# Definindo o número máximo de iterações
max_iter = 10

# Loop para encontrar o ponto
for i in range(max_iter):
    # Calculando a inclinação da tangente em (x_0, y_0)
    m = tangent_slope(x_0, y_0, a, p)
    
    # Calculando a coordenada x do próximo ponto
    x_1 = (m**2 - x_0 - x_0) % p
    
    # Calculando a coordenada y do próximo ponto
    y_1 = (m * (x_0 - x_1) - y_0) % p
    
    # Exibindo o resultado
    print(f"Iteração {i+1}:")
    print(f"Ponto atual: ({x_0}, {y_0})")
    print(f"Inclinação da tangente: {m}")
    print(f"Próximo ponto: ({x_1}, {y_1})\n")
    
    # Atualizando as coordenadas do ponto
    x_0, y_0 = x_1, y_1
