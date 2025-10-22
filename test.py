def unique_prime_factorization(n):
    factors = []
    
    # Handle 2 as a special case
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2
    
    # Check odd numbers up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    
    # If n is greater than 2, it must be prime
    if n > 2:
        factors.append(n)
    
    return factors

print(unique_prime_factorization(25))