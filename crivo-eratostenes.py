def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)

    return primes

# Exemplo de uso
limit = 10000
prime_numbers = sieve_of_eratosthenes(limit)
print("Números primos até", limit, ":", prime_numbers)
