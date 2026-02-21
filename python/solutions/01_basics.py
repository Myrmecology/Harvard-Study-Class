"""
PYTHON BASICS - SOLUTIONS SET 01
=================================
Complete solutions to all 50 problems from 01_basics.py

Each solution includes:
- Working code
- Explanation of the concept
- Common mistakes to avoid
- Alternative approaches where applicable

Study these solutions AFTER attempting the problems yourself!
"""

# ============================================
# SECTION 1: VARIABLES & ASSIGNMENT (1-10)
# ============================================

# Problem 1: Create a variable
print("=" * 50)
print("Problem 1: Create a variable")
print("=" * 50)

name = "Alice"
print(name)

"""
EXPLANATION:
- Variables are containers for storing data values
- Use = (assignment operator) to assign a value
- Variable names should be descriptive
- Python is case-sensitive: 'name' and 'Name' are different
"""
print()


# Problem 2: Multiple variables
print("=" * 50)
print("Problem 2: Multiple variables")
print("=" * 50)

age = 25                    # Integer
height = 5.8                # Float
is_student = True           # Boolean

print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

"""
EXPLANATION:
- int: Whole numbers (no decimal point)
- float: Numbers with decimal points
- bool: True or False (note the capitalization!)
- Each data type serves different purposes
"""
print()


# Problem 3: Variable reassignment
print("=" * 50)
print("Problem 3: Variable reassignment")
print("=" * 50)

x = 10
print("x before:", x)

x = 20
print("x after:", x)

"""
EXPLANATION:
- Variables can be reassigned to new values
- The old value is replaced, not stored
- Python is dynamically typed - can reassign to different types
"""
print()


# Problem 4: Multiple assignment
print("=" * 50)
print("Problem 4: Multiple assignment")
print("=" * 50)

a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Alternative: Assign same value to multiple variables
# x = y = z = 0

"""
EXPLANATION:
- Python allows unpacking multiple assignments in one line
- Values are assigned in order: a=1, b=2, c=3
- This is called "tuple unpacking"
"""
print()


# Problem 5: Swapping variables
print("=" * 50)
print("Problem 5: Swapping variables")
print("=" * 50)

x = 5
y = 10
print(f"Before swap: x = {x}, y = {y}")

# Python way (simple and elegant)
x, y = y, x
print(f"After swap: x = {x}, y = {y}")

# Traditional way (using temp variable)
a = 5
b = 10
temp = a
a = b
b = temp
print(f"Traditional swap: a = {a}, b = {b}")

"""
EXPLANATION:
- Python's tuple unpacking makes swapping easy
- Traditional method uses temporary variable
- Python evaluates right side first, then assigns
"""
print()


# Problem 6: Variable naming
print("=" * 50)
print("Problem 6: Variable naming")
print("=" * 50)

user_age = 25                    # snake_case (Python convention)
userName = "John"                # camelCase (valid but not Pythonic)
CONSTANT_VALUE = 100             # UPPERCASE for constants

print(f"user_age: {user_age}")
print(f"userName: {userName}")
print(f"CONSTANT_VALUE: {CONSTANT_VALUE}")

"""
EXPLANATION:
- snake_case: Recommended for variables and functions
- camelCase: Valid but not Python convention
- UPPERCASE: Used for constants (values that shouldn't change)
- Names should be descriptive and meaningful
"""
print()


# Problem 7: Valid variable names
print("=" * 50)
print("Problem 7: Valid variable names")
print("=" * 50)

my_var = 1          # ✓ Valid
# 2nd_var = 2       # ✗ Invalid - can't start with number
# my-var = 3        # ✗ Invalid - can't use hyphens
_private = 4        # ✓ Valid - underscore prefix convention for "private"
MyVar = 5           # ✓ Valid - but typically used for classes

print(f"my_var: {my_var}")
print(f"_private: {_private}")
print(f"MyVar: {MyVar}")

"""
EXPLANATION:
Variable names must:
- Start with letter or underscore
- Contain only letters, numbers, and underscores
- Not be a Python keyword (like 'if', 'for', 'class')
- Be case-sensitive
"""
print()


# Problem 8: Delete a variable
print("=" * 50)
print("Problem 8: Delete a variable")
print("=" * 50)

temp = 42
print(f"temp before deletion: {temp}")

del temp
# print(temp)  # This would raise NameError: name 'temp' is not defined

print("temp has been deleted (uncommenting print(temp) would cause an error)")

"""
EXPLANATION:
- del removes variable from memory
- Attempting to access deleted variable causes NameError
- Useful for freeing memory with large data structures
- In practice, rarely needed (Python has garbage collection)
"""
print()


# Problem 9: Check variable type
print("=" * 50)
print("Problem 9: Check variable type")
print("=" * 50)

mystery = 3.14
print(f"mystery value: {mystery}")
print(f"mystery type: {type(mystery)}")

"""
EXPLANATION:
- type() returns the data type of a variable
- Useful for debugging and understanding code
- Returns class type: <class 'float'>, <class 'int'>, etc.
"""
print()


# Problem 10: Global vs Local scope (preview)
print("=" * 50)
print("Problem 10: Global vs Local scope")
print("=" * 50)

global_var = "I'm global"

def my_function():
    print(f"Inside function: {global_var}")

print(f"Outside function: {global_var}")
my_function()

"""
EXPLANATION:
- Global variables are accessible everywhere
- Functions can read global variables
- To modify global variables inside functions, use 'global' keyword
- We'll learn more about scope with functions later
"""
print()


# ============================================
# SECTION 2: DATA TYPES - NUMBERS (11-20)
# ============================================

# Problem 11: Integer arithmetic
print("=" * 50)
print("Problem 11: Integer arithmetic")
print("=" * 50)

a = 15
b = 4

print(f"a + b = {a + b}")      # Addition: 19
print(f"a - b = {a - b}")      # Subtraction: 11
print(f"a * b = {a * b}")      # Multiplication: 60
print(f"a / b = {a / b}")      # Division: 3.75 (always returns float)
print(f"a // b = {a // b}")    # Floor division: 3 (integer division)
print(f"a % b = {a % b}")      # Modulus: 3 (remainder)

"""
EXPLANATION:
- / always returns float, even if result is whole number
- // returns integer (floor division)
- % returns remainder
- These operators follow standard precedence rules
"""
print()


# Problem 12: Float arithmetic
print("=" * 50)
print("Problem 12: Float arithmetic")
print("=" * 50)

x = 10.5
y = 2.5

print(f"x + y = {x + y}")      # 13.0
print(f"x - y = {x - y}")      # 8.0
print(f"x * y = {x * y}")      # 26.25
print(f"x / y = {x / y}")      # 4.2
print(f"x // y = {x // y}")    # 4.0 (floor division with floats)
print(f"x % y = {x % y}")      # 0.5
print(f"x ** y = {x ** y}")    # 10.5^2.5 = 361.52...

"""
EXPLANATION:
- Float operations maintain decimal precision
- ** is the exponentiation operator
- Floor division with floats still returns float
- Be aware of floating-point precision limitations
"""
print()


# Problem 13: Order of operations
print("=" * 50)
print("Problem 13: Order of operations")
print("=" * 50)

result = (5 + 3) * 2 - 8 / 4
print(f"(5 + 3) * 2 - 8 / 4 = {result}")

# Step by step:
# (5 + 3) = 8
# 8 * 2 = 16
# 8 / 4 = 2.0
# 16 - 2.0 = 14.0

"""
EXPLANATION:
PEMDAS/BODMAS order:
1. Parentheses/Brackets
2. Exponents/Orders
3. Multiplication and Division (left to right)
4. Addition and Subtraction (left to right)
"""
print()


# Problem 14: Exponentiation
print("=" * 50)
print("Problem 14: Exponentiation")
print("=" * 50)

result = 2 ** 10
print(f"2^10 = {result}")

"""
EXPLANATION:
- ** is the power operator
- 2^10 = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 1024
- Don't confuse with ^ (which is XOR bitwise operator in Python)
"""
print()


# Problem 15: Modulus operator
print("=" * 50)
print("Problem 15: Modulus operator")
print("=" * 50)

remainder = 17 % 5
print(f"17 % 5 = {remainder}")

# 17 ÷ 5 = 3 remainder 2
# So 17 % 5 = 2

"""
EXPLANATION:
- % returns the remainder of division
- Useful for checking divisibility (if x % 2 == 0, x is even)
- Common in cycling through indices
"""
print()


# Problem 16: Absolute value
print("=" * 50)
print("Problem 16: Absolute value")
print("=" * 50)

number = -42
absolute = abs(number)
print(f"abs({number}) = {absolute}")

"""
EXPLANATION:
- abs() returns absolute value (distance from zero)
- Always positive (or zero)
- Works with int and float
"""
print()


# Problem 17: Rounding numbers
print("=" * 50)
print("Problem 17: Rounding numbers")
print("=" * 50)

pi = 3.14159
rounded = round(pi, 2)
print(f"round({pi}, 2) = {rounded}")

# Alternative: No decimal places
rounded_int = round(pi)
print(f"round({pi}) = {rounded_int}")

"""
EXPLANATION:
- round(number, decimals) rounds to specified decimal places
- Without second argument, rounds to nearest integer
- Uses "banker's rounding" (rounds .5 to nearest even number)
"""
print()


# Problem 18: Integer division vs regular division
print("=" * 50)
print("Problem 18: Integer vs regular division")
print("=" * 50)

regular = 7 / 2
floor = 7 // 2

print(f"7 / 2 = {regular}")    # 3.5 (float)
print(f"7 // 2 = {floor}")     # 3 (int)

"""
EXPLANATION:
- / always returns float
- // returns floor (rounds down to nearest integer)
- 7 / 2 = 3.5
- 7 // 2 = 3 (not 4!)
"""
print()


# Problem 19: Mixed type arithmetic
print("=" * 50)
print("Problem 19: Mixed type arithmetic")
print("=" * 50)

result = 10 + 3.5
print(f"10 + 3.5 = {result}")
print(f"Type: {type(result)}")

"""
EXPLANATION:
- When mixing int and float, result is float
- Python automatically converts (type coercion)
- This is called "type promotion"
"""
print()


# Problem 20: Complex expressions
print("=" * 50)
print("Problem 20: Complex expressions")
print("=" * 50)

result = ((10 + 5) * 2) ** 2 / 10 - 5
print(f"((10 + 5) * 2) ** 2 / 10 - 5 = {result}")

# Step by step:
# (10 + 5) = 15
# 15 * 2 = 30
# 30 ** 2 = 900
# 900 / 10 = 90.0
# 90.0 - 5 = 85.0

"""
EXPLANATION:
- Follow PEMDAS carefully
- Use parentheses to make intention clear
- Complex expressions are evaluated inside-out
"""
print()


# ============================================
# SECTION 3: DATA TYPES - STRINGS (21-30)
# ============================================

# Problem 21: String creation
print("=" * 50)
print("Problem 21: String creation")
print("=" * 50)

single = 'Hello'
double = "World"
triple = '''Multi-line
string
example'''

print(f"Single quotes: {single}")
print(f"Double quotes: {double}")
print(f"Triple quotes:\n{triple}")

"""
EXPLANATION:
- Single and double quotes are interchangeable
- Use one when the string contains the other
- Triple quotes allow multi-line strings
- Triple quotes also used for docstrings
"""
print()


# Problem 22: String concatenation
print("=" * 50)
print("Problem 22: String concatenation")
print("=" * 50)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Alternative methods:
full_name2 = f"{first_name} {last_name}"  # f-string (preferred)
full_name3 = " ".join([first_name, last_name])  # join method

"""
EXPLANATION:
- + operator concatenates strings
- Must add space manually
- f-strings are modern and readable
- join() is efficient for multiple strings
"""
print()


# Problem 23: String repetition
print("=" * 50)
print("Problem 23: String repetition")
print("=" * 50)

star = "*"
stars = star * 10
print(stars)

# Practical use: Creating separators
print("-" * 30)

"""
EXPLANATION:
- * operator repeats strings
- Creates new string (doesn't modify original)
- Useful for formatting and patterns
"""
print()


# Problem 24: String length
print("=" * 50)
print("Problem 24: String length")
print("=" * 50)

message = "Hello, World!"
length = len(message)
print(f"Length of '{message}' is {length}")

"""
EXPLANATION:
- len() counts characters in string
- Includes spaces and punctuation
- Returns integer
"""
print()


# Problem 25: String indexing
print("=" * 50)
print("Problem 25: String indexing")
print("=" * 50)

word = "Python"
print(f"First character: {word[0]}")    # 'P'
print(f"Last character: {word[-1]}")    # 'n'
print(f"Third character: {word[2]}")    # 't'

"""
EXPLANATION:
- Indexing starts at 0
- Negative indices count from end (-1 is last)
- word[0] = 'P', word[1] = 'y', word[2] = 't', etc.
- IndexError if index out of range
"""
print()


# Problem 26: String slicing
print("=" * 50)
print("Problem 26: String slicing")
print("=" * 50)

text = "Hello, World!"
print(f"First 5 characters: {text[0:5]}")    # "Hello"
print(f"Last 6 characters: {text[-6:]}")     # "World!"
print(f"Every second character: {text[::2]}") # "Hlo ol!"

"""
EXPLANATION:
- Slicing syntax: string[start:stop:step]
- start is inclusive, stop is exclusive
- Omitting start begins at 0
- Omitting stop goes to end
- step determines increment (default 1)
"""
print()


# Problem 27: String methods - upper/lower
print("=" * 50)
print("Problem 27: String methods - upper/lower")
print("=" * 50)

message = "Hello World"
print(f"Upper: {message.upper()}")      # "HELLO WORLD"
print(f"Lower: {message.lower()}")      # "hello world"
print(f"Title: {message.title()}")      # "Hello World"

# Note: original string unchanged (strings are immutable)
print(f"Original: {message}")

"""
EXPLANATION:
- Strings are immutable (can't be changed)
- Methods return new strings
- .upper() - all uppercase
- .lower() - all lowercase
- .title() - capitalize first letter of each word
"""
print()


# Problem 28: String methods - replace
print("=" * 50)
print("Problem 28: String methods - replace")
print("=" * 50)

sentence = "I love cats"
new_sentence = sentence.replace("cats", "dogs")
print(new_sentence)

"""
EXPLANATION:
- .replace(old, new) returns new string
- Original string unchanged
- Replaces all occurrences
- Can add third parameter for max replacements
"""
print()


# Problem 29: String formatting - f-strings
print("=" * 50)
print("Problem 29: String formatting - f-strings")
print("=" * 50)

name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)

# Can include expressions:
print(f"In 5 years, I'll be {age + 5} years old.")

"""
EXPLANATION:
- f-strings (Python 3.6+) are the modern way
- Place f before quote, use {} for variables
- Can include expressions inside {}
- More readable than .format() or % formatting
"""
print()


# Problem 30: Escape characters
print("=" * 50)
print("Problem 30: Escape characters")
print("=" * 50)

print("She said, \"Hello!\"")
print("How are you?")

# Alternative using single quotes:
print('She said, "Hello!"')

"""
EXPLANATION:
- \ is escape character
- \" creates literal quote inside string
- \n creates newline
- Other: \t (tab), \\ (backslash), \' (single quote)
"""
print()


# ============================================
# SECTION 4: DATA TYPES - BOOLEANS (31-35)
# ============================================

# Problem 31: Boolean values
print("=" * 50)
print("Problem 31: Boolean values")
print("=" * 50)

is_raining = True
is_sunny = False

print(f"Is it raining? {is_raining}")
print(f"Is it sunny? {is_sunny}")

"""
EXPLANATION:
- Only two boolean values: True and False
- Must be capitalized
- Used in conditional logic
- Result of comparison operations
"""
print()


# Problem 32: Comparison operators
print("=" * 50)
print("Problem 32: Comparison operators")
print("=" * 50)

print(f"5 > 3: {5 > 3}")              # True
print(f"10 <= 10: {10 <= 10}")        # True
print(f"7 == 7: {7 == 7}")            # True
print(f"4 != 5: {4 != 5}")            # True
print(f"'hello' == 'Hello': {'hello' == 'Hello'}")  # False (case-sensitive)

"""
EXPLANATION:
Comparison operators:
- > greater than
- < less than
- >= greater than or equal
- <= less than or equal
- == equal to (comparison)
- != not equal to
"""
print()


# Problem 33: Logical operators - AND
print("=" * 50)
print("Problem 33: Logical operators - AND")
print("=" * 50)

a = True
b = False

print(f"True and False: {a and b}")      # False
print(f"True and True: {a and True}")    # True
print(f"False and False: {False and False}")  # False

"""
EXPLANATION:
- AND returns True only if BOTH are True
- Truth table:
  True and True = True
  True and False = False
  False and True = False
  False and False = False
"""
print()


# Problem 34: Logical operators - OR
print("=" * 50)
print("Problem 34: Logical operators - OR")
print("=" * 50)

x = True
y = False

print(f"True or False: {x or y}")        # True
print(f"False or False: {False or False}")  # False
print(f"True or True: {True or True}")   # True

"""
EXPLANATION:
- OR returns True if AT LEAST ONE is True
- Truth table:
  True or True = True
  True or False = True
  False or True = True
  False or False = False
"""
print()


# Problem 35: Logical operators - NOT
print("=" * 50)
print("Problem 35: Logical operators - NOT")
print("=" * 50)

value = True
print(f"not True: {not value}")    # False
print(f"not False: {not False}")   # True

"""
EXPLANATION:
- NOT reverses the boolean value
- not True = False
- not False = True
- Can combine: not (x and y)
"""
print()


# ============================================
# SECTION 5: INPUT/OUTPUT (36-40)
# ============================================

# Problem 36: Basic print statement
print("=" * 50)
print("Problem 36: Basic print statement")
print("=" * 50)

print("Hello, World!")

"""
EXPLANATION:
- print() displays output to console
- Automatically adds newline at end
- Can print any data type
"""
print()


# Problem 37: Print multiple items
print("=" * 50)
print("Problem 37: Print multiple items")
print("=" * 50)

name = "Alice"
age = 25
city = "New York"

print(name, age, city)

"""
EXPLANATION:
- Separate multiple items with commas
- Python adds spaces between items automatically
- Can mix different data types
"""
print()


# Problem 38: Print with custom separator
print("=" * 50)
print("Problem 38: Print with custom separator")
print("=" * 50)

print("apple", "banana", "cherry", sep=", ")

"""
EXPLANATION:
- sep parameter changes separator (default is space)
- Useful for custom formatting
- Can use any string as separator
"""
print()


# Problem 39: Print without newline
print("=" * 50)
print("Problem 39: Print without newline")
print("=" * 50)

print("Hello", end=" ")
print("World")

"""
EXPLANATION:
- end parameter controls what comes after (default is '\n')
- end=" " prints space instead of newline
- Useful for printing on same line
"""
print()


# Problem 40: User input
print("=" * 50)
print("Problem 40: User input")
print("=" * 50)

# Uncomment to test (requires interactive input):
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# For automated testing:
user_name = "Test User"
print(f"Hello, {user_name}!")

"""
EXPLANATION:
- input() prompts user for input
- Always returns string (even if number entered)
- Program waits for user to press Enter
- To get numbers, must convert: int(input("Enter number: "))
"""
print()


# ============================================
# SECTION 6: TYPE CONVERSION (41-45)
# ============================================

# Problem 41: String to integer
print("=" * 50)
print("Problem 41: String to integer")
print("=" * 50)

num_str = "42"
num_int = int(num_str)
result = num_int + 8
print(f"int('{num_str}') + 8 = {result}")

"""
EXPLANATION:
- int() converts to integer
- String must contain valid integer
- ValueError if conversion fails
"""
print()


# Problem 42: Integer to string
print("=" * 50)
print("Problem 42: Integer to string")
print("=" * 50)

age = 25
message = "I am " + str(age) + " years old"
print(message)

# Better way with f-string:
message2 = f"I am {age} years old"
print(message2)

"""
EXPLANATION:
- str() converts to string
- Necessary for concatenation with strings
- f-strings handle conversion automatically
"""
print()


# Problem 43: String to float
print("=" * 50)
print("Problem 43: String to float")
print("=" * 50)

price_str = "19.99"
price_float = float(price_str)
total = price_float * 2
print(f"float('{price_str}') * 2 = {total}")

"""
EXPLANATION:
- float() converts to floating-point number
- String must contain valid number
- Can include decimal point
"""
print()


# Problem 44: Float to integer
print("=" * 50)
print("Problem 44: Float to integer")
print("=" * 50)

decimal = 7.8
integer = int(decimal)
print(f"int({decimal}) = {integer}")

# Note: Truncates, doesn't round!
print(f"int(7.9) = {int(7.9)}")  # 7, not 8

"""
EXPLANATION:
- int() truncates (removes decimal part)
- Does NOT round
- Use round() first if you want rounding
"""
print()


# Problem 45: Boolean conversions
print("=" * 50)
print("Problem 45: Boolean conversions")
print("=" * 50)

print(f"bool(1): {bool(1)}")          # True
print(f"bool(0): {bool(0)}")          # False
print(f"bool('Hello'): {bool('Hello')}")  # True
print(f"bool(''): {bool('')}")        # False (empty string)
print(f"bool(None): {bool(None)}")    # False

"""
EXPLANATION:
Falsy values (convert to False):
- 0, 0.0
- Empty sequences: "", [], {}
- None

Everything else is Truthy (converts to True):
- Non-zero numbers
- Non-empty sequences
"""
print()


# ============================================
# SECTION 7: MIXED PRACTICE (46-50)
# ============================================

# Problem 46: Calculate area of a rectangle
print("=" * 50)
print("Problem 46: Calculate area of rectangle")
print("=" * 50)

length = 10
width = 5
area = length * width
print(f"The area of the rectangle is {area}")

"""
EXPLANATION:
- Formula: area = length × width
- Simple multiplication
- Practical application of variables
"""
print()


# Problem 47: Temperature conversion
print("=" * 50)
print("Problem 47: Temperature conversion")
print("=" * 50)

celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

"""
EXPLANATION:
- Formula: F = (C × 9/5) + 32
- Remember order of operations
- Reverse formula: C = (F - 32) × 5/9
"""
print()


# Problem 48: Simple interest calculator
print("=" * 50)
print("Problem 48: Simple interest calculator")
print("=" * 50)

principal = 1000
rate = 5
time = 2
interest = (principal * rate * time) / 100
print(f"Simple interest: ${interest}")

"""
EXPLANATION:
- Formula: SI = (P × R × T) / 100
- P = Principal amount
- R = Rate of interest per year
- T = Time in years
"""
print()


# Problem 49: Average of three numbers
print("=" * 50)
print("Problem 49: Average of three numbers")
print("=" * 50)

num1 = 10
num2 = 20
num3 = 30
average = (num1 + num2 + num3) / 3
print(f"Average: {average}")

"""
EXPLANATION:
- Average = sum / count
- Add all numbers, divide by how many
- Use parentheses to ensure correct order
"""
print()


# Problem 50: BMI Calculator
print("=" * 50)
print("Problem 50: BMI Calculator")
print("=" * 50)

weight_kg = 70
height_m = 1.75
bmi = weight_kg / (height_m ** 2)
print(f"BMI: {round(bmi, 2)}")

"""
EXPLANATION:
- Formula: BMI = weight(kg) / height(m)²
- ** operator for squaring
- round() for clean output
- BMI categories:
  < 18.5: Underweight
  18.5-24.9: Normal
  25-29.9: Overweight
  >= 30: Obese
"""
print()


print("=" * 50)
print("🎉 CONGRATULATIONS! 🎉")
print("You've reviewed all 50 solutions!")
print("=" * 50)
print("\nNext steps:")
print("1. Practice these concepts in my_solutions/")
print("2. Experiment with variations")
print("3. Move to 02_data_types.py")
print("=" * 50)