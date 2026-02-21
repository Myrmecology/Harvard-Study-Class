"""
DATA TYPES - EXERCISE SET 02
=============================
50 problems covering:
- Advanced string operations
- String methods and manipulation
- Numbers (int, float, complex)
- Type checking and conversion
- Built-in functions for data types
- Practical applications

INSTRUCTIONS:
1. Write solutions in python/my_solutions/02_data_types.py
2. Test your code frequently
3. Reference python/solutions/02_data_types.py if stuck

BUILD ON: Basics from 01_basics.py
"""

# ============================================
# SECTION 1: STRING METHODS (1-15)
# ============================================

# Problem 1: String case methods
# Create a string: text = "Python Programming"
# Print it in: uppercase, lowercase, title case, swap case, capitalize


# Problem 2: String strip methods
# Create: message = "   Hello World   "
# Use strip(), lstrip(), and rstrip() to remove whitespace
# Print each result


# Problem 3: String find method
# Create: sentence = "Python is awesome. Python is powerful."
# Find the index of first "Python" using find()
# Find the index of "awesome"
# Try to find "Java" (returns -1 if not found)


# Problem 4: String count method
# Create: text = "banana"
# Count how many times 'a' appears
# Count how many times 'an' appears


# Problem 5: String startswith and endswith
# Create: filename = "document.pdf"
# Check if it starts with "doc"
# Check if it ends with ".pdf"
# Check if it ends with ".txt"


# Problem 6: String isalpha, isdigit, isalnum
# Test these strings and print True/False for each check:
# "Hello" - is it alphabetic?
# "12345" - is it digits?
# "Hello123" - is it alphanumeric?
# "Hello World" - is it alphabetic? (spaces matter!)


# Problem 7: String split method
# Create: sentence = "Python is easy to learn"
# Split it into a list of words
# Print the list and the number of words


# Problem 8: String join method
# Create a list: words = ["Python", "is", "awesome"]
# Join them with spaces to create a sentence
# Join them with hyphens: "Python-is-awesome"


# Problem 9: String replace with count
# Create: text = "I love cats. Cats are cute. Cats are friendly."
# Replace only the first 2 occurrences of "Cats" with "Dogs"
# Print the result


# Problem 10: String center, ljust, rjust
# Create: title = "Python"
# Center it in 20 characters
# Left-justify it in 20 characters
# Right-justify it in 20 characters


# Problem 11: String zfill (zero padding)
# Create: number = "42"
# Pad it with zeros to make it 5 characters: "00042"


# Problem 12: Check if string is uppercase/lowercase
# Create: text1 = "HELLO", text2 = "hello", text3 = "Hello"
# Check isupper() and islower() for each


# Problem 13: String partition
# Create: email = "user@example.com"
# Use partition('@') to split it into three parts
# Print: username, separator, domain


# Problem 14: String translate (character mapping)
# Create a translation table that replaces: a->@, e->3, i->1, o->0
# Apply it to: "hello world"
# Print the result


# Problem 15: String format with multiple variables
# Create: name = "Alice", age = 25, city = "NYC"
# Create formatted string: "My name is Alice, I am 25 years old, and I live in NYC"
# Use three different methods: f-string, .format(), and %


# ============================================
# SECTION 2: ADVANCED STRING OPERATIONS (16-25)
# ============================================

# Problem 16: Reverse a string
# Create: word = "Python"
# Reverse it using slicing
# Print the reversed string


# Problem 17: Check for palindrome
# Create: word = "racecar"
# Check if it's a palindrome (reads same forwards and backwards)
# Print True or False


# Problem 18: Remove vowels from string
# Create: sentence = "Hello World"
# Remove all vowels (a, e, i, o, u) from it
# Print the result


# Problem 19: Count vowels and consonants
# Create: text = "Programming"
# Count how many vowels and consonants it has
# Print both counts


# Problem 20: String indexing practice
# Create: alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Print:
# - Every 3rd character
# - Characters from index 5 to 15
# - Last 5 characters
# - Reverse alphabet using slicing


# Problem 21: Capitalize first letter of each word (manual)
# Create: sentence = "python is amazing"
# Don't use .title() - manually capitalize first letter of each word
# Hint: Use split(), loop, and join()


# Problem 22: Remove duplicates from string (preserve order)
# Create: text = "hello"
# Remove duplicate characters: "helo"
# Print the result


# Problem 23: String compression
# Create: text = "aaabbbccc"
# Compress it to: "a3b3c3" (character followed by count)
# Print compressed string


# Problem 24: Check if two strings are anagrams
# Create: word1 = "listen", word2 = "silent"
# Check if they're anagrams (same letters, different order)
# Print True or False


# Problem 25: Extract numbers from string
# Create: text = "I have 2 cats and 3 dogs"
# Extract all numbers from it
# Print them as a list


# ============================================
# SECTION 3: NUMBER OPERATIONS (26-35)
# ============================================

# Problem 26: Complex numbers
# Create: z1 = 3 + 4j, z2 = 1 - 2j
# Perform: addition, subtraction, multiplication
# Print real and imaginary parts of result


# Problem 27: Number methods
# For number 3.7:
# - Round up using math.ceil()
# - Round down using math.floor()
# - Get absolute value
# Import math module first!


# Problem 28: Convert between number systems
# Create: decimal = 42
# Convert to binary using bin()
# Convert to octal using oct()
# Convert to hexadecimal using hex()


# Problem 29: Random numbers
# Import random module
# Generate:
# - Random float between 0 and 1
# - Random integer between 1 and 100
# - Random choice from list: ["apple", "banana", "cherry"]


# Problem 30: Number formatting
# Create: pi = 3.14159265359
# Format it to show:
# - 2 decimal places
# - 5 decimal places
# - In scientific notation
# Use f-strings with format specifiers


# Problem 31: Check if number is even or odd
# Create: number = 17
# Use modulus operator to check if even or odd
# Print "Even" or "Odd"


# Problem 32: Find maximum and minimum
# Create: num1 = 45, num2 = 23, num3 = 67
# Find and print the maximum using max()
# Find and print the minimum using min()


# Problem 33: Calculate power and square root
# Import math
# For number 16:
# - Calculate 16^3
# - Calculate square root of 16
# - Calculate cube root (16^(1/3))


# Problem 34: Sum and product of digits
# Create: number = 1234
# Calculate sum of digits: 1+2+3+4 = 10
# Calculate product of digits: 1*2*3*4 = 24
# Hint: Convert to string first


# Problem 35: Check if number is prime
# Create: number = 17
# Check if it's prime (only divisible by 1 and itself)
# Print True or False


# ============================================
# SECTION 4: TYPE CHECKING & CONVERSION (36-40)
# ============================================

# Problem 36: Check types of various values
# Create variables with different types:
# - integer, float, string, boolean, list, tuple, dict
# Use type() and isinstance() to check their types


# Problem 37: Safe type conversion
# Try to convert these strings to int:
# - "123" (should work)
# - "12.5" (will fail - use try/except or convert to float first)
# - "hello" (will fail)
# Handle errors gracefully


# Problem 38: Convert between numeric types
# Create: x = 5 (int)
# Convert to float, then to complex
# Print each conversion and its type


# Problem 39: String to list and back
# Create: sentence = "Python is fun"
# Convert to list of characters
# Convert back to string
# Print both


# Problem 40: Type conversion in expressions
# What's the result type of:
# - 5 + 3.0
# - 10 / 2
# - 10 // 2
# - True + 5
# Print each result and its type


# ============================================
# SECTION 5: BUILT-IN FUNCTIONS (41-45)
# ============================================

# Problem 41: Using ord() and chr()
# Get ASCII value of 'A' using ord()
# Get character for ASCII 65 using chr()
# Print both


# Problem 42: Using divmod()
# For 17 divided by 5:
# Use divmod() to get quotient and remainder in one call
# Print both values


# Problem 43: Using pow() with three arguments
# Calculate: (2^10) % 1000
# Use pow(2, 10, 1000) for efficient modular exponentiation
# Print the result


# Problem 44: Using sum() with different iterables
# Create: numbers = [1, 2, 3, 4, 5]
# Calculate sum using sum()
# Add a start value: sum(numbers, 10)
# Print both results


# Problem 45: Using all() and any()
# Create: values = [True, True, False]
# Check if all are True using all()
# Check if any are True using any()
# Print both results


# ============================================
# SECTION 6: PRACTICAL APPLICATIONS (46-50)
# ============================================

# Problem 46: Validate email format (simple)
# Create: email = "user@example.com"
# Check if it contains '@' and '.'
# Check if '@' comes before '.'
# Print "Valid" or "Invalid"


# Problem 47: Parse a URL
# Create: url = "https://www.example.com/page?id=123"
# Extract:
# - Protocol (https)
# - Domain (www.example.com)
# - Path (/page)
# - Query (id=123)
# Use string methods


# Problem 48: Format a phone number
# Create: phone = "1234567890"
# Format it as: "(123) 456-7890"
# Use string slicing and concatenation


# Problem 49: Password strength checker
# Create: password = "MyPass123!"
# Check if it has:
# - At least 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character
# Print "Strong" or "Weak"


# Problem 50: Calculate tip and total bill
# Create: bill = 85.50, tip_percent = 18
# Calculate:
# - Tip amount
# - Total bill (bill + tip)
# Format output to 2 decimal places


"""
EXCELLENT WORK! 🎉
You've completed Data Types exercises!

Key concepts mastered:
✓ String manipulation methods
✓ Advanced string operations
✓ Number types and operations
✓ Type checking and conversion
✓ Built-in functions
✓ Practical applications

Next: python/exercises/03_conditionals_loops.py
"""