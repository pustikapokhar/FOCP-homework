'''Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''
import math

def factors(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

# Test the function
print(factors(12))  # Output: [1, 2, 3, 4, 6, 12]
print(factors(25))  # Output: [1, 5, 25]
print(factors(36))  # Output: [1, 2, 3, 4, 6, 9, 36]
print(factors(49))  # Output: [1, 7, 49]
