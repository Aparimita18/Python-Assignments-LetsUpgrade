#to display table of a number
def display_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

# Example usage
display_table(5, 10)


#to print prime numbers upto a limit
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_prime_numbers(limit):
    for number in range(2, limit + 1):
        if is_prime(number):
            print(number)

# Example usage
print_prime_numbers(20)
