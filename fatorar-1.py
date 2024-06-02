def prime_factorization_steps(n):
    factors = []
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
            print(f"Passo {len(factors)}: {n}")  # Mostra o resultado intermediário
        else:
            divisor += 1
    
    return factors

# Número para fatorar
number = 115792089237316195423570985008687907853269984665640564039457584007913129639936

# Fatoração do número
factors = prime_factorization_steps(number)

# Calcular o produto dos fatores primos
result = 1
for factor in factors:
    result *= factor

# Imprimir o resultado da fatoração
print("Resultado da fatoração:", result)
