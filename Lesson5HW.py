def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(5))  # True
print(is_prime(10)) # False

########

def digit_sum(k):
    if k == 0:
        return 0
    else:
        return k % 10 + digit_sum(k // 10)

# Misol uchun 
print(digit_sum(123))  # 6
print(digit_sum(987))  # 24

#####

def print_powers_of_two(N):
    power = 1
    while power <= N:
        print(power)
        power *= 2

# Example usage
N = 100  # Change this value as needed
print_powers_of_two(N)



