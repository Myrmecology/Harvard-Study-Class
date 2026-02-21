"""
PYTHON BASICS - EXERCISE SET 01
================================
50 foundational Python problems covering:
- Variables and assignment
- Data types (int, float, str, bool)
- Basic operations
- Input/Output
- Comments and documentation
- Type conversion
- Basic debugging

INSTRUCTIONS:
1. Read each problem carefully
2. Write your solution in python/my_solutions/01_basics.py
3. Run your code to test it
4. Check python/solutions/01_basics.py if you get stuck

TIP: Type the code yourself - don't copy/paste! Muscle memory is built through repetition.
"""

# ============================================
# SECTION 1: VARIABLES & ASSIGNMENT (1-10)
# ============================================

# Problem 1: Create a variable
# Create a variable called 'name' and assign it your name as a string.
# Print the variable.


# Problem 2: Multiple variables
# Create three variables: age (integer), height (float), and is_student (boolean).
# Assign appropriate values and print all three.


# Problem 3: Variable reassignment
# Create a variable 'x' with value 10.
# Then reassign it to 20.
# Print x before and after reassignment.


# Problem 4: Multiple assignment
# Assign the values 1, 2, and 3 to variables a, b, and c in a single line.
# Print all three variables.


# Problem 5: Swapping variables
# Create two variables: x = 5 and y = 10
# Swap their values (x should become 10, y should become 5)
# Print both variables after swapping.


# Problem 6: Variable naming
# Create variables following Python naming conventions:
# - user_age (snake_case) = 25
# - userName (camelCase - not recommended but valid) = "John"
# - CONSTANT_VALUE (uppercase for constants) = 100
# Print all three.


# Problem 7: Valid variable names
# Which of these are valid variable names in Python?
# Test by trying to create them (comment out invalid ones):
# my_var = 1
# 2nd_var = 2
# my-var = 3
# _private = 4
# MyVar = 5


# Problem 8: Delete a variable
# Create a variable 'temp' with value 42.
# Print it, then delete it using 'del'.
# Try to print it again (this should cause an error - that's expected!).


# Problem 9: Check variable type
# Create a variable 'mystery' with value 3.14
# Use type() to check what data type it is.
# Print the result.


# Problem 10: Global vs Local scope (preview)
# Create a variable 'global_var' with value "I'm global"
# Print it outside and inside a function (we'll learn functions later, just follow the pattern):
# def my_function():
#     print(global_var)
# my_function()


# ============================================
# SECTION 2: DATA TYPES - NUMBERS (11-20)
# ============================================

# Problem 11: Integer arithmetic
# Create two integers: a = 15, b = 4
# Print the results of: a + b, a - b, a * b, a / b, a // b (floor division), a % b (modulus)


# Problem 12: Float arithmetic
# Create two floats: x = 10.5, y = 2.5
# Print the results of all arithmetic operations: +, -, *, /, //, %, ** (power)


# Problem 13: Order of operations
# Calculate: (5 + 3) * 2 - 8 / 4
# Print the result and verify it follows PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)


# Problem 14: Exponentiation
# Calculate 2 to the power of 10 (2^10) using the ** operator.
# Print the result.


# Problem 15: Modulus operator
# Find the remainder when 17 is divided by 5 using the % operator.
# Print the result.


# Problem 16: Absolute value
# Create a variable with value -42.
# Use the abs() function to get its absolute value.
# Print the result.


# Problem 17: Rounding numbers
# Create a float: pi = 3.14159
# Use round() to round it to 2 decimal places.
# Print the result.


# Problem 18: Integer division vs regular division
# Calculate 7 / 2 and 7 // 2
# Print both results and observe the difference.


# Problem 19: Mixed type arithmetic
# Calculate: 10 (int) + 3.5 (float)
# Print the result and check its type using type()


# Problem 20: Complex expressions
# Calculate: ((10 + 5) * 2) ** 2 / 10 - 5
# Print the result.


# ============================================
# SECTION 3: DATA TYPES - STRINGS (21-30)
# ============================================

# Problem 21: String creation
# Create three strings using:
# - Single quotes: 'Hello'
# - Double quotes: "World"
# - Triple quotes: '''Multi-line string'''
# Print all three.


# Problem 22: String concatenation
# Create two variables: first_name = "John", last_name = "Doe"
# Concatenate them with a space in between.
# Print the full name.


# Problem 23: String repetition
# Create a string: star = "*"
# Print it repeated 10 times using the * operator.


# Problem 24: String length
# Create a string: message = "Hello, World!"
# Use len() to find its length.
# Print the length.


# Problem 25: String indexing
# Create a string: word = "Python"
# Access and print:
# - First character (index 0)
# - Last character (index -1)
# - Third character (index 2)


# Problem 26: String slicing
# Create a string: text = "Hello, World!"
# Use slicing to extract and print:
# - First 5 characters
# - Last 6 characters
# - Every second character


# Problem 27: String methods - upper/lower
# Create a string: message = "Hello World"
# Print it in:
# - All uppercase
# - All lowercase
# - Title case (first letter of each word capitalized)


# Problem 28: String methods - replace
# Create a string: sentence = "I love cats"
# Replace "cats" with "dogs"
# Print the new string.


# Problem 29: String formatting - f-strings (Python 3.6+)
# Create variables: name = "Alice", age = 25
# Use an f-string to print: "My name is Alice and I am 25 years old."


# Problem 30: Escape characters
# Print the following exactly (including quotes and newline):
# She said, "Hello!"
# How are you?


# ============================================
# SECTION 4: DATA TYPES - BOOLEANS (31-35)
# ============================================

# Problem 31: Boolean values
# Create two boolean variables: is_raining = True, is_sunny = False
# Print both.


# Problem 32: Comparison operators
# Compare the following and print the results (True or False):
# - 5 > 3
# - 10 <= 10
# - 7 == 7
# - 4 != 5
# - "hello" == "Hello"


# Problem 33: Logical operators - AND
# Create: a = True, b = False
# Print the results of:
# - a and b
# - a and True
# - False and False


# Problem 34: Logical operators - OR
# Create: x = True, y = False
# Print the results of:
# - x or y
# - False or False
# - True or True


# Problem 35: Logical operators - NOT
# Create: value = True
# Print the result of: not value
# Also print: not False


# ============================================
# SECTION 5: INPUT/OUTPUT (36-40)
# ============================================

# Problem 36: Basic print statement
# Print "Hello, World!" to the console.


# Problem 37: Print multiple items
# Print three variables in one print statement: name, age, city
# Separate them with spaces.


# Problem 38: Print with custom separator
# Print three words: "apple", "banana", "cherry"
# Use a comma as separator (hint: use sep parameter)


# Problem 39: Print without newline
# Print "Hello" and "World" on the same line with a space between them.
# Use end parameter to prevent newline.


# Problem 40: User input
# Ask the user for their name using input()
# Store it in a variable and print: "Hello, [name]!"
# (Note: When testing, you'll need to type input in the console)


# ============================================
# SECTION 6: TYPE CONVERSION (41-45)
# ============================================

# Problem 41: String to integer
# Create a string: num_str = "42"
# Convert it to an integer and add 8 to it.
# Print the result.


# Problem 42: Integer to string
# Create an integer: age = 25
# Convert it to a string and concatenate it with: "I am " and " years old"
# Print the result.


# Problem 43: String to float
# Create a string: price_str = "19.99"
# Convert it to a float and multiply it by 2.
# Print the result.


# Problem 44: Float to integer
# Create a float: decimal = 7.8
# Convert it to an integer (this will truncate, not round).
# Print the result.


# Problem 45: Boolean conversions
# Test what converts to True/False:
# - bool(1)
# - bool(0)
# - bool("Hello")
# - bool("")
# - bool(None)
# Print all results.


# ============================================
# SECTION 7: MIXED PRACTICE (46-50)
# ============================================

# Problem 46: Calculate area of a rectangle
# Create variables: length = 10, width = 5
# Calculate the area (length * width)
# Print: "The area of the rectangle is [area]"


# Problem 47: Temperature conversion
# Create a variable: celsius = 25
# Convert to Fahrenheit using formula: (celsius * 9/5) + 32
# Print the result with a descriptive message.


# Problem 48: Simple interest calculator
# Create variables: principal = 1000, rate = 5, time = 2
# Calculate simple interest: (principal * rate * time) / 100
# Print the interest amount.


# Problem 49: Average of three numbers
# Create three variables: num1 = 10, num2 = 20, num3 = 30
# Calculate their average.
# Print the result.


# Problem 50: BMI Calculator
# Create variables: weight_kg = 70, height_m = 1.75
# Calculate BMI: weight / (height ** 2)
# Print the BMI with 2 decimal places.


"""
CONGRATULATIONS! 🎉
You've completed the Python Basics exercise set!

Next steps:
1. Review your solutions
2. Compare with python/solutions/01_basics.py
3. Move on to python/exercises/02_data_types.py

Remember: The goal is understanding, not just completion!
"""