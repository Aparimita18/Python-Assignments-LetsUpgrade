def display_table_and_prime(number, limit):
    # Display table of the given number
    print(f"Table of {number}:")
    for i in range(1, limit + 1):
        print(f"{number} * {i} = {number * i}")

    # Find and print prime numbers from the table
    print(f"\nPrime numbers from the table of {number}:")
    for i in range(1, limit + 1):
        result = number * i
        if is_prime(result):
            print(result)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Test the function
number = 7
limit = 10
display_table_and_prime(number, limit)
