# Example list
fruits = ['apple', 'banana', 'cherry', 'date']

# Accessing elements in a list
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# Modifying elements in a list
fruits[2] = 'grape'
print("Modified list:", fruits)

# Adding elements to a list
fruits.append('orange')
print("After adding an element:", fruits)

# Removing elements from a list
removed_fruit = fruits.pop(1)
print("Removed fruit:", removed_fruit)
print("After removing an element:", fruits)

# Example tuple
student = ('John', 20, 'Computer Science')

# Accessing elements in a tuple
print("Name:", student[0])
print("Age:", student[1])
print("Major:", student[2])

# Unpacking a tuple
name, age, major = student
print("Unpacked values:", name, age, major)
