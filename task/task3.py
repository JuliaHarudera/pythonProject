def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]

    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, limit + 1, current):
                sieve[multiple] = False

    for number, is_prime in enumerate(sieve):
        if is_prime:
            yield number


limit = 50

for prime in generate_primes(limit):
    print(prime)