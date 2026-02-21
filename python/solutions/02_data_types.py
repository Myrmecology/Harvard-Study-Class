"""
DATA TYPES - SOLUTIONS SET 02
==============================
Complete solutions to all 50 problems from 02_data_types.py

Each solution includes working code, explanations, and best practices.
Study these after attempting the problems yourself!
"""

# ============================================
# SECTION 1: STRING METHODS (1-15)
# ============================================

# Problem 1: String case methods
print("=" * 50)
print("Problem 1: String case methods")
print("=" * 50)

text = "Python Programming"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")           # PYTHON PROGRAMMING
print(f"Lower: {text.lower()}")           # python programming
print(f"Title: {text.title()}")           # Python Programming
print(f"Swapcase: {text.swapcase()}")     # pYTHON pROGRAMMING
print(f"Capitalize: {text.capitalize()}") # Python programming

"""
EXPLANATION:
- .upper() - all uppercase
- .lower() - all lowercase
- .title() - capitalize first letter of each word
- .swapcase() - swap case of each character
- .capitalize() - capitalize only first letter, rest lowercase
All return new strings (strings are immutable)
"""
print()


# Problem 2: String strip methods
print("=" * 50)
print("Problem 2: String strip methods")
print("=" * 50)

message = "   Hello World   "
print(f"Original: '{message}'")
print(f"strip(): '{message.strip()}'")      # Remove both sides
print(f"lstrip(): '{message.lstrip()}'")    # Remove left side
print(f"rstrip(): '{message.rstrip()}'")    # Remove right side

"""
EXPLANATION:
- .strip() - removes whitespace from both ends
- .lstrip() - removes from left (start)
- .rstrip() - removes from right (end)
Can specify characters to remove: .strip('xyz')
"""
print()


# Problem 3: String find method
print("=" * 50)
print("Problem 3: String find method")
print("=" * 50)

sentence = "Python is awesome. Python is powerful."
print(f"First 'Python': index {sentence.find('Python')}")      # 0
print(f"'awesome': index {sentence.find('awesome')}")          # 10
print(f"'Java': index {sentence.find('Java')}")                # -1 (not found)

# Alternative: index() method (raises error if not found)
# sentence.index('Java')  # Would raise ValueError

"""
EXPLANATION:
- .find(substring) - returns index of first occurrence
- Returns -1 if not found
- .index() similar but raises ValueError if not found
- Can specify start/end: .find('Python', 5)
"""
print()


# Problem 4: String count method
print("=" * 50)
print("Problem 4: String count method")
print("=" * 50)

text = "banana"
print(f"Count 'a': {text.count('a')}")     # 3
print(f"Count 'an': {text.count('an')}")   # 2

"""
EXPLANATION:
- .count(substring) - counts non-overlapping occurrences
- Case-sensitive
- Can specify range: .count('a', 0, 3)
"""
print()


# Problem 5: String startswith and endswith
print("=" * 50)
print("Problem 5: String startswith and endswith")
print("=" * 50)

filename = "document.pdf"
print(f"Starts with 'doc': {filename.startswith('doc')}")      # True
print(f"Ends with '.pdf': {filename.endswith('.pdf')}")        # True
print(f"Ends with '.txt': {filename.endswith('.txt')}")        # False

"""
EXPLANATION:
- .startswith(prefix) - checks if string starts with prefix
- .endswith(suffix) - checks if string ends with suffix
- Both return boolean
- Can check multiple: .endswith(('.pdf', '.doc'))
"""
print()


# Problem 6: String isalpha, isdigit, isalnum
print("=" * 50)
print("Problem 6: String validation methods")
print("=" * 50)

print(f"'Hello'.isalpha(): {'Hello'.isalpha()}")               # True
print(f"'12345'.isdigit(): {'12345'.isdigit()}")               # True
print(f"'Hello123'.isalnum(): {'Hello123'.isalnum()}")         # True
print(f"'Hello World'.isalpha(): {'Hello World'.isalpha()}")   # False (space!)

"""
EXPLANATION:
- .isalpha() - True if all characters are alphabetic
- .isdigit() - True if all characters are digits
- .isalnum() - True if all characters are alphanumeric
- Spaces and punctuation make these return False
Other methods: .isspace(), .islower(), .isupper()
"""
print()


# Problem 7: String split method
print("=" * 50)
print("Problem 7: String split method")
print("=" * 50)

sentence = "Python is easy to learn"
words = sentence.split()
print(f"Words: {words}")
print(f"Number of words: {len(words)}")

# Split by specific delimiter
csv = "apple,banana,cherry"
fruits = csv.split(',')
print(f"Fruits: {fruits}")

"""
EXPLANATION:
- .split() - splits by whitespace by default
- Returns list of strings
- Can specify delimiter: .split(',')
- Can limit splits: .split(' ', 2)
"""
print()


# Problem 8: String join method
print("=" * 50)
print("Problem 8: String join method")
print("=" * 50)

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"With spaces: {sentence}")

hyphenated = "-".join(words)
print(f"With hyphens: {hyphenated}")

"""
EXPLANATION:
- separator.join(iterable) - joins elements with separator
- More efficient than repeated concatenation
- Works with any iterable of strings
"""
print()


# Problem 9: String replace with count
print("=" * 50)
print("Problem 9: String replace with count")
print("=" * 50)

text = "I love cats. Cats are cute. Cats are friendly."
result = text.replace("Cats", "Dogs", 2)  # Replace first 2 occurrences
print(result)

"""
EXPLANATION:
- .replace(old, new, count) - replaces occurrences
- count parameter limits replacements
- Without count, replaces all occurrences
"""
print()


# Problem 10: String center, ljust, rjust
print("=" * 50)
print("Problem 10: String alignment methods")
print("=" * 50)

title = "Python"
print(f"Center: '{title.center(20)}'")
print(f"Left: '{title.ljust(20)}'")
print(f"Right: '{title.rjust(20)}'")

# With fill character
print(f"Center with *: '{title.center(20, '*')}'")

"""
EXPLANATION:
- .center(width) - centers string in width
- .ljust(width) - left justifies
- .rjust(width) - right justifies
- Can specify fill character (default is space)
"""
print()


# Problem 11: String zfill (zero padding)
print("=" * 50)
print("Problem 11: String zfill")
print("=" * 50)

number = "42"
padded = number.zfill(5)
print(f"Padded: {padded}")  # 00042

# Works with negative numbers too
negative = "-42"
print(f"Negative padded: {negative.zfill(5)}")  # -0042

"""
EXPLANATION:
- .zfill(width) - pads with zeros on left
- Useful for formatting numbers
- Handles negative signs correctly
"""
print()


# Problem 12: Check if string is uppercase/lowercase
print("=" * 50)
print("Problem 12: Case checking")
print("=" * 50)

text1 = "HELLO"
text2 = "hello"
text3 = "Hello"

print(f"'{text1}'.isupper(): {text1.isupper()}")  # True
print(f"'{text1}'.islower(): {text1.islower()}")  # False
print(f"'{text2}'.isupper(): {text2.isupper()}")  # False
print(f"'{text2}'.islower(): {text2.islower()}")  # True
print(f"'{text3}'.isupper(): {text3.isupper()}")  # False
print(f"'{text3}'.islower(): {text3.islower()}")  # False

"""
EXPLANATION:
- .isupper() - True if all cased characters are uppercase
- .islower() - True if all cased characters are lowercase
- Numbers and symbols are ignored
"""
print()


# Problem 13: String partition
print("=" * 50)
print("Problem 13: String partition")
print("=" * 50)

email = "user@example.com"
username, separator, domain = email.partition('@')
print(f"Username: {username}")
print(f"Separator: {separator}")
print(f"Domain: {domain}")

"""
EXPLANATION:
- .partition(sep) - splits at first occurrence of separator
- Returns tuple: (before, separator, after)
- If separator not found, returns (string, '', '')
- .rpartition() starts from right
"""
print()


# Problem 14: String translate (character mapping)
print("=" * 50)
print("Problem 14: String translate")
print("=" * 50)

# Create translation table
translation = str.maketrans('aeio', '@310')
text = "hello world"
result = text.translate(translation)
print(f"Original: {text}")
print(f"Translated: {result}")  # h3ll0 w0rld

"""
EXPLANATION:
- str.maketrans() creates translation table
- .translate() applies the translation
- Useful for character replacements
- Can also remove characters with third parameter
"""
print()


# Problem 15: String format with multiple variables
print("=" * 50)
print("Problem 15: Multiple formatting methods")
print("=" * 50)

name = "Alice"
age = 25
city = "NYC"

# Method 1: f-string (recommended)
msg1 = f"My name is {name}, I am {age} years old, and I live in {city}"
print(f"f-string: {msg1}")

# Method 2: .format()
msg2 = "My name is {}, I am {} years old, and I live in {}".format(name, age, city)
print(f".format(): {msg2}")

# Method 3: % formatting (old style)
msg3 = "My name is %s, I am %d years old, and I live in %s" % (name, age, city)
print(f"% formatting: {msg3}")

"""
EXPLANATION:
- f-strings: Modern, readable (Python 3.6+)
- .format(): Versatile, backward compatible
- % formatting: Old style, still works
- f-strings are preferred for readability
"""
print()


# ============================================
# SECTION 2: ADVANCED STRING OPERATIONS (16-25)
# ============================================

# Problem 16: Reverse a string
print("=" * 50)
print("Problem 16: Reverse a string")
print("=" * 50)

word = "Python"
reversed_word = word[::-1]
print(f"Original: {word}")
print(f"Reversed: {reversed_word}")

"""
EXPLANATION:
- [::-1] is slice notation with step -1
- Reads string backwards
- Creates new string (doesn't modify original)
"""
print()


# Problem 17: Check for palindrome
print("=" * 50)
print("Problem 17: Check for palindrome")
print("=" * 50)

word = "racecar"
is_palindrome = word == word[::-1]
print(f"'{word}' is palindrome: {is_palindrome}")

# Case-insensitive palindrome check
word2 = "RaceCar"
is_palindrome2 = word2.lower() == word2.lower()[::-1]
print(f"'{word2}' is palindrome (case-insensitive): {is_palindrome2}")

"""
EXPLANATION:
- Compare string with its reverse
- Use .lower() for case-insensitive check
- Palindrome reads same forwards and backwards
"""
print()


# Problem 18: Remove vowels from string
print("=" * 50)
print("Problem 18: Remove vowels from string")
print("=" * 50)

sentence = "Hello World"
vowels = "aeiouAEIOU"
no_vowels = ""
for char in sentence:
    if char not in vowels:
        no_vowels += char
print(f"Original: {sentence}")
print(f"No vowels: {no_vowels}")

# Alternative: List comprehension (more Pythonic)
no_vowels2 = ''.join([char for char in sentence if char not in vowels])
print(f"Using comprehension: {no_vowels2}")

"""
EXPLANATION:
- Loop through each character
- Check if not a vowel
- Build new string without vowels
- List comprehension is more concise
"""
print()


# Problem 19: Count vowels and consonants
print("=" * 50)
print("Problem 19: Count vowels and consonants")
print("=" * 50)

text = "Programming"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Text: {text}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

"""
EXPLANATION:
- Check if character is alphabetic first
- Then check if vowel or consonant
- Ignore non-alphabetic characters
"""
print()


# Problem 20: String indexing practice
print("=" * 50)
print("Problem 20: String indexing practice")
print("=" * 50)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(f"Every 3rd character: {alphabet[::3]}")
print(f"Characters 5-15: {alphabet[5:15]}")
print(f"Last 5 characters: {alphabet[-5:]}")
print(f"Reversed: {alphabet[::-1]}")

"""
EXPLANATION:
- [::3] - every 3rd character (step = 3)
- [5:15] - slice from index 5 to 14
- [-5:] - last 5 characters
- [::-1] - reverse the string
"""
print()


# Problem 21: Capitalize first letter of each word (manual)
print("=" * 50)
print("Problem 21: Manual capitalization")
print("=" * 50)

sentence = "python is amazing"
words = sentence.split()
capitalized_words = []
for word in words:
    capitalized = word[0].upper() + word[1:]
    capitalized_words.append(capitalized)
result = " ".join(capitalized_words)
print(f"Original: {sentence}")
print(f"Capitalized: {result}")

# One-liner with list comprehension
result2 = " ".join([word[0].upper() + word[1:] for word in sentence.split()])
print(f"One-liner: {result2}")

"""
EXPLANATION:
- Split into words
- Capitalize first letter, keep rest
- Join back together
- word[0].upper() + word[1:] is the pattern
"""
print()


# Problem 22: Remove duplicates from string (preserve order)
print("=" * 50)
print("Problem 22: Remove duplicates")
print("=" * 50)

text = "hello"
seen = set()
result = []
for char in text:
    if char not in seen:
        seen.add(char)
        result.append(char)
unique = ''.join(result)
print(f"Original: {text}")
print(f"Unique: {unique}")

# Alternative: dict.fromkeys() preserves order (Python 3.7+)
unique2 = ''.join(dict.fromkeys(text))
print(f"Using dict: {unique2}")

"""
EXPLANATION:
- Use set to track seen characters
- Only add if not seen before
- dict.fromkeys() is elegant alternative
- Order is preserved
"""
print()


# Problem 23: String compression
print("=" * 50)
print("Problem 23: String compression")
print("=" * 50)

text = "aaabbbccc"
compressed = ""
count = 1
for i in range(len(text)):
    if i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1
print(f"Original: {text}")
print(f"Compressed: {compressed}")

"""
EXPLANATION:
- Count consecutive identical characters
- Append character + count
- Reset count when character changes
- Common interview question
"""
print()


# Problem 24: Check if two strings are anagrams
print("=" * 50)
print("Problem 24: Check for anagrams")
print("=" * 50)

word1 = "listen"
word2 = "silent"
is_anagram = sorted(word1) == sorted(word2)
print(f"'{word1}' and '{word2}' are anagrams: {is_anagram}")

# Alternative: count characters
from collections import Counter
is_anagram2 = Counter(word1) == Counter(word2)
print(f"Using Counter: {is_anagram2}")

"""
EXPLANATION:
- Anagrams have same letters in different order
- Sorting both strings should give same result
- Counter counts character frequencies
- Both methods work well
"""
print()


# Problem 25: Extract numbers from string
print("=" * 50)
print("Problem 25: Extract numbers from string")
print("=" * 50)

text = "I have 2 cats and 3 dogs"
numbers = []
for word in text.split():
    if word.isdigit():
        numbers.append(int(word))
print(f"Text: {text}")
print(f"Numbers: {numbers}")

# Alternative: regex (more powerful)
import re
numbers2 = [int(x) for x in re.findall(r'\d+', text)]
print(f"Using regex: {numbers2}")

"""
EXPLANATION:
- Split and check if each word is digit
- Regular expressions (re) are more flexible
- \d+ matches one or more digits
- Convert to int after extraction
"""
print()


# ============================================
# SECTION 3: NUMBER OPERATIONS (26-35)
# ============================================

# Problem 26: Complex numbers
print("=" * 50)
print("Problem 26: Complex numbers")
print("=" * 50)

z1 = 3 + 4j
z2 = 1 - 2j

addition = z1 + z2
subtraction = z1 - z2
multiplication = z1 * z2

print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Real part of z1: {z1.real}")
print(f"Imaginary part of z1: {z1.imag}")

"""
EXPLANATION:
- j or J suffix denotes imaginary unit
- Python supports complex number arithmetic
- .real and .imag access components
- Useful in scientific computing
"""
print()


# Problem 27: Number methods
print("=" * 50)
print("Problem 27: Number methods")
print("=" * 50)

import math

number = 3.7
print(f"Number: {number}")
print(f"Ceiling: {math.ceil(number)}")   # 4
print(f"Floor: {math.floor(number)}")    # 3
print(f"Absolute: {abs(-number)}")       # 3.7

"""
EXPLANATION:
- math.ceil() rounds up
- math.floor() rounds down
- abs() gets absolute value
- Import math module first
"""
print()


# Problem 28: Convert between number systems
print("=" * 50)
print("Problem 28: Number system conversion")
print("=" * 50)

decimal = 42
print(f"Decimal: {decimal}")
print(f"Binary: {bin(decimal)}")     # 0b101010
print(f"Octal: {oct(decimal)}")      # 0o52
print(f"Hexadecimal: {hex(decimal)}") # 0x2a

# Convert back to decimal
binary_str = bin(decimal)
back_to_decimal = int(binary_str, 2)
print(f"Back to decimal: {back_to_decimal}")

"""
EXPLANATION:
- bin() converts to binary (base 2)
- oct() converts to octal (base 8)
- hex() converts to hexadecimal (base 16)
- Returns string with prefix (0b, 0o, 0x)
- int(string, base) converts back
"""
print()


# Problem 29: Random numbers
print("=" * 50)
print("Problem 29: Random numbers")
print("=" * 50)

import random

print(f"Random float [0, 1): {random.random()}")
print(f"Random int [1, 100]: {random.randint(1, 100)}")

fruits = ["apple", "banana", "cherry"]
print(f"Random choice: {random.choice(fruits)}")

"""
EXPLANATION:
- random.random() - float between 0 and 1
- random.randint(a, b) - int between a and b (inclusive)
- random.choice(seq) - random element from sequence
- Import random module first
"""
print()


# Problem 30: Number formatting
print("=" * 50)
print("Problem 30: Number formatting")
print("=" * 50)

pi = 3.14159265359
print(f"2 decimals: {pi:.2f}")
print(f"5 decimals: {pi:.5f}")
print(f"Scientific: {pi:.2e}")
print(f"Percentage: {0.875:.1%}")

"""
EXPLANATION:
- :.2f - 2 decimal places
- :.5f - 5 decimal places
- :.2e - scientific notation
- :.1% - percentage format
"""
print()


# Problem 31: Check if number is even or odd
print("=" * 50)
print("Problem 31: Even or odd")
print("=" * 50)

number = 17
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

# One-liner
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")

"""
EXPLANATION:
- Use modulus operator %
- If number % 2 == 0, it's even
- Otherwise it's odd
- Ternary operator for concise version
"""
print()


# Problem 32: Find maximum and minimum
print("=" * 50)
print("Problem 32: Maximum and minimum")
print("=" * 50)

num1 = 45
num2 = 23
num3 = 67

maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)

print(f"Numbers: {num1}, {num2}, {num3}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

# Works with lists too
numbers = [45, 23, 67]
print(f"Max from list: {max(numbers)}")

"""
EXPLANATION:
- max() returns largest value
- min() returns smallest value
- Works with multiple arguments or iterables
- Can use with any comparable types
"""
print()


# Problem 33: Calculate power and square root
print("=" * 50)
print("Problem 33: Power and roots")
print("=" * 50)

import math

number = 16
print(f"Number: {number}")
print(f"16^3: {number ** 3}")
print(f"Square root: {math.sqrt(number)}")
print(f"Cube root: {number ** (1/3)}")

# Alternative for square root
print(f"Square root (alt): {number ** 0.5}")

"""
EXPLANATION:
- ** is power operator
- math.sqrt() calculates square root
- nth root = number ** (1/n)
- x ** 0.5 is same as sqrt(x)
"""
print()


# Problem 34: Sum and product of digits
print("=" * 50)
print("Problem 34: Sum and product of digits")
print("=" * 50)

number = 1234
digits = [int(d) for d in str(number)]

digit_sum = sum(digits)
digit_product = 1
for digit in digits:
    digit_product *= digit

print(f"Number: {number}")
print(f"Sum of digits: {digit_sum}")
print(f"Product of digits: {digit_product}")

# Alternative for product
from math import prod
digit_product2 = prod(digits)
print(f"Product (using math.prod): {digit_product2}")

"""
EXPLANATION:
- Convert number to string to iterate digits
- Convert each digit back to int
- sum() for addition
- Loop or math.prod() for multiplication
"""
print()


# Problem 35: Check if number is prime
print("=" * 50)
print("Problem 35: Check if prime")
print("=" * 50)

number = 17
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

print(f"{number} is prime: {is_prime}")

"""
EXPLANATION:
- Prime: only divisible by 1 and itself
- Numbers < 2 are not prime
- Only check up to sqrt(n) for efficiency
- If any divisor found, not prime
"""
print()


# ============================================
# SECTION 4: TYPE CHECKING & CONVERSION (36-40)
# ============================================

# Problem 36: Check types of various values
print("=" * 50)
print("Problem 36: Type checking")
print("=" * 50)

integer = 42
floating = 3.14
string = "Hello"
boolean = True
lst = [1, 2, 3]
tpl = (1, 2, 3)
dct = {"key": "value"}

# Using type()
print(f"type(42): {type(integer)}")
print(f"type(3.14): {type(floating)}")
print(f"type('Hello'): {type(string)}")

# Using isinstance()
print(f"isinstance(42, int): {isinstance(integer, int)}")
print(f"isinstance(3.14, float): {isinstance(floating, float)}")
print(f"isinstance([1,2,3], list): {isinstance(lst, list)}")

"""
EXPLANATION:
- type() returns the exact type
- isinstance() checks if object is instance of class
- isinstance() works with inheritance
- isinstance() can check multiple types
"""
print()


# Problem 37: Safe type conversion
print("=" * 50)
print("Problem 37: Safe type conversion")
print("=" * 50)

# Safe conversion function
def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        return None

print(f"'123' -> {safe_int_convert('123')}")
print(f"'12.5' -> {safe_int_convert('12.5')}")
print(f"'hello' -> {safe_int_convert('hello')}")

# Converting float string
float_str = "12.5"
result = int(float(float_str))
print(f"'12.5' -> float -> int: {result}")

"""
EXPLANATION:
- Use try/except for safe conversion
- ValueError raised if conversion fails
- Convert to float first if decimal string
- Return None or default value on failure
"""
print()


# Problem 38: Convert between numeric types
print("=" * 50)
print("Problem 38: Numeric type conversion")
print("=" * 50)

x = 5
print(f"Original (int): {x}, type: {type(x)}")

x_float = float(x)
print(f"As float: {x_float}, type: {type(x_float)}")

x_complex = complex(x_float)
print(f"As complex: {x_complex}, type: {type(x_complex)}")

"""
EXPLANATION:
- float() converts to floating-point
- complex() converts to complex number
- Conversion generally goes: int → float → complex
- Some precision may be lost going backwards
"""
print()


# Problem 39: String to list and back
print("=" * 50)
print("Problem 39: String ↔ List conversion")
print("=" * 50)

sentence = "Python is fun"
char_list = list(sentence)
print(f"As list: {char_list}")

back_to_string = ''.join(char_list)
print(f"Back to string: {back_to_string}")

# Word list
word_list = sentence.split()
print(f"Word list: {word_list}")

"""
EXPLANATION:
- list() converts string to list of characters
- ''.join() converts list back to string
- split() creates list of words
- ' '.join() creates string from words
"""
print()


# Problem 40: Type conversion in expressions
print("=" * 50)
print("Problem 40: Expression type conversion")
print("=" * 50)

result1 = 5 + 3.0
print(f"5 + 3.0 = {result1}, type: {type(result1)}")

result2 = 10 / 2
print(f"10 / 2 = {result2}, type: {type(result2)}")

result3 = 10 // 2
print(f"10 // 2 = {result3}, type: {type(result3)}")

result4 = True + 5
print(f"True + 5 = {result4}, type: {type(result4)}")

"""
EXPLANATION:
- int + float = float (type promotion)
- / always returns float
- // returns int (if both operands are int)
- True = 1, False = 0 in numeric context
"""
print()


# ============================================
# SECTION 5: BUILT-IN FUNCTIONS (41-45)
# ============================================

# Problem 41: Using ord() and chr()
print("=" * 50)
print("Problem 41: ord() and chr()")
print("=" * 50)

print(f"ASCII of 'A': {ord('A')}")
print(f"Character for 65: {chr(65)}")

# Useful for encryption/encoding
print(f"ASCII of 'a': {ord('a')}")
print(f"Difference between 'A' and 'a': {ord('a') - ord('A')}")

"""
EXPLANATION:
- ord() returns Unicode/ASCII code point
- chr() returns character for code point
- Useful for character manipulation
- 'A' = 65, 'a' = 97 (difference of 32)
"""
print()


# Problem 42: Using divmod()
print("=" * 50)
print("Problem 42: divmod()")
print("=" * 50)

quotient, remainder = divmod(17, 5)
print(f"17 ÷ 5:")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")

# Equivalent to:
q = 17 // 5
r = 17 % 5
print(f"Using // and %: {q}, {r}")

"""
EXPLANATION:
- divmod(a, b) returns (a//b, a%b)
- More efficient than separate operations
- Returns tuple of (quotient, remainder)
- Useful for time/currency calculations
"""
print()


# Problem 43: Using pow() with three arguments
print("=" * 50)
print("Problem 43: Modular exponentiation")
print("=" * 50)

# Calculate (2^10) % 1000
result = pow(2, 10, 1000)
print(f"(2^10) % 1000 = {result}")

# Why use pow() with 3 args?
# It's more efficient for large numbers
large_result = pow(2, 100, 1000)
print(f"(2^100) % 1000 = {large_result}")

"""
EXPLANATION:
- pow(base, exp, mod) efficiently computes (base^exp) % mod
- Much faster for large exponents
- Used in cryptography
- Avoids overflow issues
"""
print()


# Problem 44: Using sum() with different iterables
print("=" * 50)
print("Problem 44: sum() function")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum of {numbers}: {total}")

# With start value
total_with_start = sum(numbers, 10)
print(f"Sum with start=10: {total_with_start}")

# Sum of range
range_sum = sum(range(1, 11))  # 1+2+...+10
print(f"Sum of 1 to 10: {range_sum}")

"""
EXPLANATION:
- sum(iterable) adds all elements
- sum(iterable, start) adds start to sum
- Works with any numeric iterable
- Default start is 0
"""
print()


# Problem 45: Using all() and any()
print("=" * 50)
print("Problem 45: all() and any()")
print("=" * 50)

values = [True, True, False]
print(f"Values: {values}")
print(f"all(values): {all(values)}")  # False
print(f"any(values): {any(values)}")  # True

# Practical use
numbers = [2, 4, 6, 8]
all_even = all(n % 2 == 0 for n in numbers)
print(f"All numbers even: {all_even}")

"""
EXPLANATION:
- all() returns True if ALL elements are True
- any() returns True if ANY element is True
- Short-circuits (stops early when possible)
- Useful for validation
"""
print()


# ============================================
# SECTION 6: PRACTICAL APPLICATIONS (46-50)
# ============================================

# Problem 46: Validate email format (simple)
print("=" * 50)
print("Problem 46: Email validation")
print("=" * 50)

email = "user@example.com"
has_at = '@' in email
has_dot = '.' in email
at_before_dot = email.find('@') < email.rfind('.')

is_valid = has_at and has_dot and at_before_dot
print(f"Email: {email}")
print(f"Valid: {is_valid}")

# Test invalid email
invalid = "user.example.com"
is_valid2 = '@' in invalid and '.' in invalid and invalid.find('@') < invalid.rfind('.')
print(f"Email: {invalid}")
print(f"Valid: {is_valid2}")

"""
EXPLANATION:
- Check for @ and .
- Ensure @ comes before last .
- This is simple validation (not comprehensive)
- Use regex for production email validation
"""
print()


# Problem 47: Parse a URL
print("=" * 50)
print("Problem 47: Parse URL")
print("=" * 50)

url = "https://www.example.com/page?id=123"

# Extract protocol
protocol = url.split('://')[0]
print(f"Protocol: {protocol}")

# Extract domain and path
rest = url.split('://')[1]
domain = rest.split('/')[0]
print(f"Domain: {domain}")

# Extract path
if '?' in rest:
    path = '/' + rest.split('/')[1].split('?')[0]
    query = rest.split('?')[1]
else:
    path = '/' + '/'.join(rest.split('/')[1:])
    query = None

print(f"Path: {path}")
print(f"Query: {query}")

# Better way: use urllib
from urllib.parse import urlparse
parsed = urlparse(url)
print(f"\nUsing urlparse:")
print(f"Protocol: {parsed.scheme}")
print(f"Domain: {parsed.netloc}")
print(f"Path: {parsed.path}")
print(f"Query: {parsed.query}")

"""
EXPLANATION:
- Manual parsing using split()
- urllib.parse is more robust
- urlparse() returns named tuple
- Better for production code
"""
print()


# Problem 48: Format a phone number
print("=" * 50)
print("Problem 48: Format phone number")
print("=" * 50)

phone = "1234567890"
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(f"Original: {phone}")
print(f"Formatted: {formatted}")

# Function for reusability
def format_phone(number):
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"

print(f"Using function: {format_phone('9876543210')}")

"""
EXPLANATION:
- Use string slicing to extract parts
- Format using f-string
- Create function for reusability
- Validate length before formatting in production
"""
print()


# Problem 49: Password strength checker
print("=" * 50)
print("Problem 49: Password strength checker")
print("=" * 50)

password = "MyPass123!"

# Check criteria
has_length = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

is_strong = all([has_length, has_upper, has_lower, has_digit, has_special])

print(f"Password: {password}")
print(f"Length >= 8: {has_length}")
print(f"Has uppercase: {has_upper}")
print(f"Has lowercase: {has_lower}")
print(f"Has digit: {has_digit}")
print(f"Has special: {has_special}")
print(f"Strength: {'Strong' if is_strong else 'Weak'}")

"""
EXPLANATION:
- Check each criterion separately
- Use any() to check for at least one
- Combine all checks with all()
- Provides clear feedback on requirements
"""
print()


# Problem 50: Calculate tip and total bill
print("=" * 50)
print("Problem 50: Tip calculator")
print("=" * 50)

bill = 85.50
tip_percent = 18

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount

print(f"Bill: ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")

# Function version
def calculate_tip(bill, percent):
    tip = bill * (percent / 100)
    return tip, bill + tip

t, tot = calculate_tip(100, 20)
print(f"\nFor $100 bill with 20% tip:")
print(f"Tip: ${t:.2f}, Total: ${tot:.2f}")

"""
EXPLANATION:
- Calculate percentage of bill
- Add to original bill
- Format to 2 decimal places for currency
- Create function for reusability
"""
print()


print("=" * 50)
print("🎊 CONGRATULATIONS! 🎊")
print("Data Types module completed!")
print("=" * 50)
print("\nKey concepts mastered:")
print("✓ String manipulation methods")
print("✓ Advanced string operations")
print("✓ Number types and operations")
print("✓ Type checking and conversion")
print("✓ Built-in functions")
print("✓ Practical applications")
print("\nNext: python/exercises/03_conditionals_loops.py")
print("=" * 50)