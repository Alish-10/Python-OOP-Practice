
# Python Lab Week 1
# Variables and Data Types
my_int = 5
my_float = 5.5
my_bool = True

print("Integer:", my_int)
print("Float:", my_float)
print("Boolean:", my_bool)

my_int_float = float(my_int)
my_float_int = int(my_float)
my_bool_int = int(my_bool)

print("my_int_float:", my_int_float)
print("my_float_int:", my_float_int)
print("my_bool_int:", my_bool_int)

# Arithmetic Operations

result_addition = 10 + 5
print("Addition:", result_addition)

#Subtraction
result_subtraction = 20 - 8
print("Subtraction:", result_subtraction)

#Multiplication
result_multiplication = 6 * 4
print("Multiplication:", result_multiplication)

#Division
result_division = 15 / 3
print("Division:", result_division)

#Floor Division
result_floor_division = 17 // 4
print("Floor Division:", result_floor_division)
#Modulus
result_modulus = 17 % 4
print("Modulus:", result_modulus)

#Exponentiation
result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)


# Calculating the Average
num1 = 20
num2 = 12
average = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is", average)

# String Operations
my_string = "This class covers OOP."
print("Original String:", my_string)

#uppercase
my_uppercase_string = my_string.upper()
print("Uppercase String:", my_uppercase_string)

#lowercase
my_lowercase_string = my_string.lower()
print("Lowercase String:", my_lowercase_string)

#replacing
my_new_string = my_string.replace("OOP", "Object-Oriented Programming")
print("Replaced String:", my_new_string)

#length
my_string_length = len(my_string)
print("Length of String:", my_string_length)

#string concatenation

class_name = "OOP"
number_of_students = 20
my_string = "Welcome to the " + class_name + " module. There are " + str(number_of_students) + " students in this class."
print(my_string)


# Task F-strings
my_name = "Alish"
number_of_classes = 3
campus = "London Campus"
my_f_string = f"Hello, my name is {my_name}. I am taking {number_of_classes} classes at the {campus}."
print(my_f_string)

#Task Temperature Conversion


celsius_input = 45 

degree_f = (celsius_input * 9/5) + 32

degree_k = celsius_input + 273.15

print("Welcome to the Temperature Converter!")
print(f"The temperature you have entered is {celsius_input} degree Celsius.")
print("Converted Temperatures:")
print(f"{celsius_input} degree Celsius is equal to {degree_f} Fahrenheit.")
print(f"{celsius_input} degree Celsius is equal to {degree_k} Kelvin.")
print("Thank you for using the Temperature Converter!")
