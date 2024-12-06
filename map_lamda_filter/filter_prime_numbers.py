number = [2, 3, 4, 5, 6, 7, 8, 9]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


prime_num = list(filter(is_prime, number))
print(prime_num)
