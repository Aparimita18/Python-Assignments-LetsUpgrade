# File: mymodule.py
def multiply_by_two_decorator(function):
    def wrapper():
        result = function()
        return result * 2
    return wrapper

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# File: main.py
import mymodule

@mymodule.multiply_by_two_decorator
def greet():
    return 5

greeting = greet()
print("Greeting:", greeting)

fib = mymodule.fibonacci_generator(10)
for number in fib:
    print(number)
