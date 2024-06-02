def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(num):
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

def prime_gap(num):
    next_prime_num = next_prime(num)
    gap = next_prime_num - num
    return gap, next_prime_num

# Exemplo de uso
numero = 1229782937960972288
gap, proximo_primo = prime_gap(numero)
print(f'O próximo número primo após {numero} é {proximo_primo} e a distância decimal é {gap}.')
