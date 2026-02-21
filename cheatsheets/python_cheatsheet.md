# 🐍 Python Quick Reference Cheatsheet

Essential Python syntax and patterns for quick lookup.

---

## 📝 Basic Syntax

### **Variables & Data Types**
```python
# Variables
name = "Alice"          # str
age = 25               # int
height = 5.8           # float
is_student = True      # bool

# Type checking
type(age)              # <class 'int'>
isinstance(age, int)   # True
```

### **Strings**
```python
# Creation
s = "Hello"
multi = """Multi
line"""

# Common methods
s.upper()              # "HELLO"
s.lower()              # "hello"
s.strip()              # Remove whitespace
s.split()              # Split into list
" ".join(['a','b'])    # "a b"
s.replace('H', 'J')    # "Jello"

# Formatting
f"Name: {name}, Age: {age}"
"Name: {}, Age: {}".format(name, age)

# Slicing
s[0]       # 'H'
s[-1]      # 'o'
s[0:2]     # 'He'
s[::-1]    # 'olleH' (reverse)
```

### **Numbers**
```python
# Operations
10 + 3     # 13
10 - 3     # 7
10 * 3     # 30
10 / 3     # 3.333... (float)
10 // 3    # 3 (floor division)
10 % 3     # 1 (modulus)
10 ** 3    # 1000 (power)

# Functions
abs(-5)    # 5
round(3.7) # 4
max(1,2,3) # 3
min(1,2,3) # 1
```

---

## 🔀 Control Flow

### **Conditionals**
```python
# if-elif-else
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Ternary
result = "Even" if x % 2 == 0 else "Odd"

# Comparison operators: ==, !=, <, >, <=, >=
# Logical operators: and, or, not
```

### **Loops**
```python
# for loop
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)

for item in [1, 2, 3]:
    print(item)

for i, val in enumerate(['a','b','c']):
    print(i, val)          # 0 a, 1 b, 2 c

# while loop
while x < 10:
    x += 1

# Loop control
break      # Exit loop
continue   # Skip to next iteration
pass       # Do nothing (placeholder)
```

---

## 📦 Data Structures

### **Lists**
```python
# Creation
lst = [1, 2, 3]
empty = []

# Methods
lst.append(4)          # Add to end
lst.extend([5, 6])     # Add multiple
lst.insert(0, 0)       # Insert at index
lst.remove(3)          # Remove by value
lst.pop()              # Remove last (return value)
lst.pop(0)             # Remove at index
lst.sort()             # Sort in place
lst.reverse()          # Reverse in place
lst.clear()            # Remove all

# Operations
len(lst)               # Length
3 in lst               # Check membership
lst[0]                 # Access
lst[1:3]               # Slice
lst + [7, 8]           # Concatenate

# Comprehension
[x**2 for x in range(5)]              # [0, 1, 4, 9, 16]
[x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### **Tuples**
```python
# Immutable sequence
t = (1, 2, 3)
single = (1,)          # Note the comma!

# Unpacking
a, b, c = t
```

### **Dictionaries**
```python
# Creation
d = {'name': 'Alice', 'age': 25}
empty = {}

# Access
d['name']              # 'Alice'
d.get('age', 0)        # 25 (or 0 if not found)

# Methods
d.keys()               # dict_keys(['name', 'age'])
d.values()             # dict_values(['Alice', 25])
d.items()              # dict_items([('name', 'Alice'), ('age', 25)])
d.pop('age')           # Remove and return
d.update({'city': 'NYC'})  # Add/update

# Comprehension
{x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
```

### **Sets**
```python
# Unordered, unique elements
s = {1, 2, 3}
empty = set()

# Operations
s.add(4)
s.remove(2)
s.discard(5)           # No error if not found

# Set operations
a | b                  # Union
a & b                  # Intersection
a - b                  # Difference
a ^ b                  # Symmetric difference
```

---

## 🔧 Functions
```python
# Basic function
def greet(name):
    return f"Hello, {name}"

# Default parameters
def greet(name="Guest"):
    return f"Hello, {name}"

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

# *args and **kwargs
def func(*args, **kwargs):
    print(args)        # Tuple of positional args
    print(kwargs)      # Dict of keyword args

# Lambda
square = lambda x: x**2
```

---

## 📂 File I/O
```python
# Read file
with open('file.txt', 'r') as f:
    content = f.read()           # Read all
    # OR
    lines = f.readlines()        # List of lines
    # OR
    for line in f:               # Iterate
        print(line.strip())

# Write file
with open('file.txt', 'w') as f:
    f.write("Hello\n")
    f.writelines(['Line 1\n', 'Line 2\n'])

# Append
with open('file.txt', 'a') as f:
    f.write("New line\n")

# Modes: 'r' read, 'w' write, 'a' append, 'b' binary, '+' read/write
```

---

## 🎯 Object-Oriented Programming
```python
# Class definition
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name       # Instance attribute
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # String representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"

# Create object
dog = Dog("Buddy", 3)
dog.bark()

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, training):
        super().__init__(name, age)
        self.training = training
```

---

## ⚡ Common Patterns

### **Swapping**
```python
a, b = b, a
```

### **Check if list is empty**
```python
if not lst:          # Pythonic way
    print("Empty")
```

### **Enumerate**
```python
for i, val in enumerate(['a', 'b', 'c']):
    print(f"{i}: {val}")
```

### **Zip**
```python
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
```

### **Map, Filter, Reduce**
```python
# Map
list(map(lambda x: x**2, [1,2,3]))  # [1, 4, 9]

# Filter
list(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # [1, 2]

# Reduce (from functools)
from functools import reduce
reduce(lambda x, y: x+y, [1,2,3,4])  # 10
```

### **Try-Except**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Always runs")
```

---

## 📚 Useful Built-in Functions
```python
# Type conversion
int(), float(), str(), bool(), list(), tuple(), dict(), set()

# Math
abs(), round(), min(), max(), sum(), pow()

# Sequences
len(), sorted(), reversed(), enumerate(), zip()

# Other
type(), isinstance(), range(), input(), print()
```

---

## 🔤 String Methods Quick Reference
```python
s.upper(), s.lower(), s.capitalize(), s.title()
s.strip(), s.lstrip(), s.rstrip()
s.split(), s.join()
s.replace(old, new)
s.find(sub), s.index(sub), s.count(sub)
s.startswith(prefix), s.endswith(suffix)
s.isalpha(), s.isdigit(), s.isalnum()
```

---

## 📊 List Methods Quick Reference
```python
lst.append(x), lst.extend(iterable)
lst.insert(i, x), lst.remove(x), lst.pop([i])
lst.sort(), lst.reverse(), lst.clear()
lst.count(x), lst.index(x)
lst.copy()
```

---

**Print this cheatsheet and keep it handy while coding!**

*Updated: February 2026*