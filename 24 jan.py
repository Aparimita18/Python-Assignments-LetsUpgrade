# Example set
fruits_set = {'apple', 'banana', 'cherry', 'date'}

# Adding elements to a set
fruits_set.add('orange')
print("After adding an element:", fruits_set)

# Removing elements from a set
fruits_set.remove('banana')
print("After removing an element:", fruits_set)

# Checking if an element exists in a set
print("Does 'cherry' exist?", 'cherry' in fruits_set)
print("Does 'grape' exist?", 'grape' in fruits_set)

# Example dictionary
student_dict = {'name': 'John', 'age': 20, 'major': 'Computer Science'}

# Accessing values in a dictionary
print("Name:", student_dict['name'])
print("Age:", student_dict['age'])
print("Major:", student_dict['major'])

# Modifying values in a dictionary
student_dict['age'] = 21
print("Modified dictionary:", student_dict)

# Adding new key-value pairs to a dictionary
student_dict['university'] = 'ABC University'
print("After adding a new pair:", student_dict)

# Removing a key-value pair from a dictionary
removed_value = student_dict.pop('major')
print("Removed value:", removed_value)
print("After removing a pair:", student_dict)
