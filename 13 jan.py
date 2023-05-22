# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice the list to get even numbers
even_numbers = numbers[1::2]

# Print the even numbers
print("Even numbers:", even_numbers)

# Iterate through the even numbers and check if they are divisible by 3
for number in even_numbers:
    if number % 3 == 0:
        print(number, "is divisible by 3")
    else:
        print(number, "is not divisible by 3")
