# working with python fuctions calls and returns

#task one
#using a function to greet a friend
def greet_friend(name):
    print(f"Hello, {name}!")
name_list = ["John", "Jack", "Jane"]
for name in name_list:
    greet_friend(name)
    

# Task two: Tax Calculation
def calculate_tax(income, tax_rate):
    tax_amount = income * tax_rate
    return tax_amount

# Example usage:
tax1 = calculate_tax(50000, 0.2)
print(f"Calculated tax for £50,000 at 20%: £{tax1}")

# Try with different values
tax2 = calculate_tax(30000, 0.15)
print(f"Calculated tax for £30,000 at 15%: £{tax2}")

tax3 = calculate_tax(100000, 0.25)
print(f"Calculated tax for £100,000 at 25%: £{tax3}")

# Task: Compound Interest Calculator Function
def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None
    for year in range(1, duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year:.2f} £")
    return int(principal * (1 + interest_rate) ** duration)

# Example usage:
final_value = compound_interest(1000, 5, 0.05)
print(f"Final investment value after 5 years: £{final_value}")

# Try with invalid interest rate
compound_interest(1000, 5, 1.2)

# Try with invalid duration
compound_interest(1000, -2, 0.05)


#Task: fixing errors in the code
#syntax error
print("hello world")
# NameError

favourite_color = "blue"
print("My favourite color is", favourite_color)

## TypeError
numeber1 = 5
number2 = 3
result = numeber1 + number2
print("The sum is:", result)

#index error
fruits = ["apple", "banana", "cherry"]
print(fruits[2])

#indentation error
time= 11
if time < 12:
    print("Good morning!")
    
# Task: Todo List Manager



