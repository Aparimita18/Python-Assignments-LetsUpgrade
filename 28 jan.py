def calculate_average(numbers):
    # Inner function to calculate the sum of numbers
    def calculate_sum():
        return sum(numbers)

    # Inner function to calculate the length of numbers
    def calculate_length():
        return len(numbers)

    # Calculate average using inner functions
    sum_of_numbers = calculate_sum()
    length_of_numbers = calculate_length()

    if length_of_numbers == 0:
        return None

    average = sum_of_numbers / length_of_numbers
    return average


# Test the function
number_list = [1, 2, 3, 4, 5]
average_result = calculate_average(number_list)
print("Average:", average_result)

# Lambda function example
multiply = lambda x, y: x * y
product = multiply(3, 4)
print("Product:", product)
