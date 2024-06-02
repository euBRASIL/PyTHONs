def baby_step_giant_step(base, result, prime):
    # Calculando o tamanho dos baby steps e giant steps
    m = int(prime ** 0.5) + 1

    # Calculando os baby steps
    baby_steps = {}
    baby = 1
    for j in range(m):
        baby_steps[baby] = j
        baby = (baby * base) % prime

    # Calculando o inverso de base elevado a m (para usar nos giant steps)
    inv = pow(base, prime - m - 1, prime)

    # Calculando os giant steps e verificando correspondência nos baby steps
    giant = result
    for i in range(m):
        if giant in baby_steps:
            return i * m + baby_steps[giant]
        giant = (giant * inv) % prime

    return None  # Não foi encontrada nenhuma correspondência


# Exemplo de uso:
base = 5  # Base
result = 3  # Resultado após elevar a base a um expoente desconhecido
prime = 23  # Número primo (usado no módulo)

solution = baby_step_giant_step(base, result, prime)
if solution is not None:
    print("Solução aproximada do logaritmo discreto:", solution)
else:
    print("Não foi encontrada uma solução para o logaritmo discreto.")
