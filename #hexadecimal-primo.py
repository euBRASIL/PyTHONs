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

def largest_prime_less_than_or_equal_to(n):
    if n <= 1:
        return None
    if is_prime(n):
        return n
    if n % 2 == 0:
        n -= 1
    else:
        n -= 2
    while n >= 2:
        if is_prime(n):
            return n
        n -= 2
    return None

numero_desejado = 1229782937960972288
primo_proximo = largest_prime_less_than_or_equal_to(numero_desejado)
print("O maior número primo menor ou igual a", numero_desejado, "é:", primo_proximo)
