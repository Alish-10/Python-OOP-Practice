# #lab week 2

# #comaparison  and conditions

is_true = True
is_true = 5>4
print( is_true)

# logical operators
# if- conditions
age = 19
age_group = "child"
if age > 18:
    age_group = "adult"
print(f"The age group is {age_group}")

#summary task 
color_list = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]
print("Original color list:", color_list)
print("Second color in the list:", color_list[1])
color_list[0] = "cyan"
print("Updated color list:", color_list)
print("Length of the color list:", len(color_list))
if "red" in color_list:
    print("Red is in the color list.")
else:
    print("Red is not in the color list.")

selected_color = color_list[1:3]
print("Selected colors from the list:", selected_color)


Task User Input and Conditions
user_input = input("Please enter your age: ")
try:
    age = int(user_input)
    if age < 0:
        print("Age cannot be negative.")
    elif age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
except ValueError:
    print("Invalid input. Please enter a valid age as a number.")
    
    

# Task Temperature Conversion with User Input
while True:
    celsius_input = float(input("Please enter the temperature in Celsius: "))
    convert_to = input("Which unit do you want to convert to? (F for Fahrenheit, K for Kelvin): ")

    if convert_to.upper() == "F":
        degree_f = (celsius_input * 9/5) + 32
        print(f"{celsius_input} degree Celsius is equal to {degree_f} Fahrenheit.")
    elif convert_to.upper() == "K":
        degree_k = celsius_input + 273.15
        print(f"{celsius_input} degree Celsius is equal to {degree_k} Kelvin.")
    else:
        print("Invalid choice. Please enter 'F' for Fahrenheit or 'K' for Kelvin.")

    again = input("Do you want to convert another temperature? (yes/no): ")
    if again.lower() == "no":
        print("Thank you for using the Temperature Converter!")
        break