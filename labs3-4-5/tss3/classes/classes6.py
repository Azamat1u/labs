def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 5, 7, 8, 9, 11, 13, 17, 19, 20, 23]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(f"Prime numbers in the list: {prime_numbers}")
