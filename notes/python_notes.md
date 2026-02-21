# 🐍 Python Study Notes

Comprehensive notes on Python concepts, best practices, and common patterns.

---

## 📚 Table of Contents

1. [Python Fundamentals](#fundamentals)
2. [Data Structures Deep Dive](#data-structures)
3. [Functions & Scope](#functions)
4. [Object-Oriented Programming](#oop)
5. [Error Handling](#errors)
6. [File Operations](#files)
7. [Advanced Topics](#advanced)
8. [Best Practices](#best-practices)
9. [Common Pitfalls](#pitfalls)

---

## <a name="fundamentals"></a>🎯 Python Fundamentals

### **The Zen of Python**
```python
import this
```

Key principles:
- **Readability counts** - Code is read more than written
- **Explicit is better than implicit** - Be clear in your intent
- **Simple is better than complex** - Keep it straightforward
- **There should be one obvious way to do it** - Python way

### **Python is Dynamically Typed**
```python
x = 5          # x is an integer
x = "hello"    # Now x is a string (totally fine!)
```

### **Everything is an Object**
```python
x = 5
type(x)        # <class 'int'>
x.bit_length() # Even integers have methods!
```

### **Indentation Matters**
```python
# ✅ Correct
if True:
    print("Indented")

# ❌ Wrong
if True:
print("Not indented")  # IndentationError
```

---

## <a name="data-structures"></a>📦 Data Structures Deep Dive

### **Mutable vs Immutable**

**Immutable (Cannot Change):**
- int, float, str, tuple, frozenset
- Changing creates new object

**Mutable (Can Change):**
- list, dict, set
- Modifying changes in-place
```python
# Immutable example
x = "hello"
id(x)  # Memory address: 140123456789
x = x + " world"
id(x)  # Different address: 140123999999

# Mutable example
lst = [1, 2, 3]
id(lst)  # 140124567890
lst.append(4)
id(lst)  # Same address: 140124567890
```

### **List Comprehensions**
```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# With if-else
parity = ["even" if x % 2 == 0 else "odd" for x in range(5)]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]

# When NOT to use: Complex logic that hurts readability
```

### **Dictionary Best Practices**
```python
# Use .get() with default
value = d.get('key', 'default')  # ✅ Safe
# value = d['key']  # ❌ KeyError if not exists

# defaultdict for auto-initialization
from collections import defaultdict
counts = defaultdict(int)
counts['a'] += 1  # No KeyError, starts at 0

# Counter for counting
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})
```

### **Sets for Membership Testing**
```python
# Fast lookup: O(1) vs O(n) for list
large_set = set(range(1000000))
500000 in large_set  # Very fast

large_list = list(range(1000000))
500000 in large_list  # Much slower
```

---

## <a name="functions"></a>🔧 Functions & Scope

### **LEGB Rule (Scope Resolution)**
**L**ocal → **E**nclosing → **G**lobal → **B**uilt-in
```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Prints: local
    
    inner()
    print(x)  # Prints: enclosing

outer()
print(x)  # Prints: global
```

### **Mutable Default Arguments Trap**
```python
# ❌ WRONG - Mutable default
def append_to_list(item, lst=[]):
    lst.append(item)
    return lst

append_to_list(1)  # [1]
append_to_list(2)  # [1, 2]  ← SURPRISE! Same list!

# ✅ CORRECT
def append_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### **Args and Kwargs**
```python
def func(*args, **kwargs):
    print(args)    # Tuple of positional args
    print(kwargs)  # Dict of keyword args

func(1, 2, 3, name="Alice", age=25)
# args: (1, 2, 3)
# kwargs: {'name': 'Alice', 'age': 25}

# Unpacking
numbers = [1, 2, 3]
func(*numbers)  # Same as func(1, 2, 3)

data = {'name': 'Bob', 'age': 30}
func(**data)  # Same as func(name='Bob', age=30)
```

### **Lambda Functions**
```python
# Good use: Simple, one-line operations
squares = list(map(lambda x: x**2, range(5)))
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# Bad use: Complex logic
# ❌ Don't do this
complex = lambda x: x**2 if x > 0 else -x**2 if x < 0 else 0

# ✅ Use regular function instead
def complex(x):
    if x > 0:
        return x**2
    elif x < 0:
        return -x**2
    return 0
```

---

## <a name="oop"></a>🏗️ Object-Oriented Programming

### **Class Basics**
```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def __str__(self):
        # String representation for users
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        # String representation for developers
        return f"Dog(name='{self.name}', age={self.age})"
```

### **Inheritance**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Polymorphism
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())
```

### **Properties**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0
temp.celsius = 30        # Uses setter
```

---

## <a name="errors"></a>🚨 Error Handling

### **Try-Except-Else-Finally**
```python
try:
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError as e:
    print(f"Type error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred")  # Only runs if no exception
finally:
    print("Always runs")  # Cleanup code
```

### **Raising Exceptions**
```python
def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

# Custom exceptions
class InsufficientFundsError(Exception):
    pass

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError(f"Need {amount}, have {balance}")
    return balance - amount
```

### **Context Managers**
```python
# Automatically closes file
with open('file.txt', 'r') as f:
    content = f.read()
# File is closed here, even if error occurred

# Custom context manager
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start}s")

with timer():
    # Code to time
    sum(range(1000000))
```

---

## <a name="files"></a>📂 File Operations

### **Reading Files**
```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read line by line (memory efficient for large files)
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Read all lines into list
with open('file.txt', 'r') as f:
    lines = f.readlines()
```

### **Writing Files**
```python
# Write (overwrites)
with open('file.txt', 'w') as f:
    f.write("Hello\n")
    f.write("World\n")

# Append
with open('file.txt', 'a') as f:
    f.write("New line\n")

# Write list of lines
lines = ["Line 1\n", "Line 2\n"]
with open('file.txt', 'w') as f:
    f.writelines(lines)
```

### **CSV and JSON**
```python
# CSV
import csv

# Read CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['column_name'])

# Write CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 25])

# JSON
import json

# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Write JSON
data = {'name': 'Alice', 'age': 25}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

---

## <a name="advanced"></a>⚡ Advanced Topics

### **Decorators**
```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start}s")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)

slow_function()  # Prints execution time
```

### **Generators**
```python
# Generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# Generator expression
squares = (x**2 for x in range(1000000))  # Memory efficient!
```

### **List vs Generator**
```python
# List - creates all items in memory
numbers = [x**2 for x in range(1000000)]  # Uses lots of memory

# Generator - creates items on demand
numbers = (x**2 for x in range(1000000))  # Uses minimal memory
```

---

## <a name="best-practices"></a>✨ Best Practices

### **PEP 8 Style Guide**
```python
# ✅ Good naming
user_name = "Alice"
is_valid = True
calculate_total()

# ❌ Bad naming
userName = "Alice"    # Use snake_case, not camelCase
x = "Alice"           # Not descriptive
calculateTotal()      # Use snake_case

# Constants in UPPERCASE
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30
```

### **Pythonic Code**
```python
# ✅ Pythonic
if item in collection:
    ...

# ❌ Not Pythonic
if collection.count(item) > 0:
    ...

# ✅ Pythonic
for i, item in enumerate(items):
    print(i, item)

# ❌ Not Pythonic
for i in range(len(items)):
    print(i, items[i])

# ✅ Pythonic - EAFP (Easier to Ask Forgiveness than Permission)
try:
    value = dictionary[key]
except KeyError:
    value = default

# ❌ Not Pythonic - LBYL (Look Before You Leap)
if key in dictionary:
    value = dictionary[key]
else:
    value = default
```

### **Type Hints (Python 3.5+)**
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

from typing import List, Dict, Optional, Union

def process_items(items: List[int]) -> Dict[str, int]:
    return {"count": len(items), "sum": sum(items)}

def find_user(user_id: int) -> Optional[str]:
    # Returns str or None
    return users.get(user_id)
```

---

## <a name="pitfalls"></a>⚠️ Common Pitfalls

### **1. Mutable Default Arguments**
See Functions section above ☝️

### **2. Late Binding Closures**
```python
# ❌ Problem
funcs = [lambda: i for i in range(5)]
[f() for f in funcs]  # [4, 4, 4, 4, 4] - All return 4!

# ✅ Solution
funcs = [lambda i=i: i for i in range(5)]
[f() for f in funcs]  # [0, 1, 2, 3, 4]
```

### **3. Modifying List While Iterating**
```python
# ❌ Wrong
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # Skips elements!

# ✅ Correct
items = [1, 2, 3, 4, 5]
items = [item for item in items if item % 2 != 0]
```

### **4. Using `is` for Value Comparison**
```python
# ❌ Wrong
if x is True:  # Checks identity, not value
    ...

# ✅ Correct
if x == True:  # Better
if x:          # Even better (Pythonic)
```

### **5. Not Using `with` for Files**
```python
# ❌ Wrong
f = open('file.txt')
content = f.read()
f.close()  # Might not run if error occurs

# ✅ Correct
with open('file.txt') as f:
    content = f.read()
# Automatically closed
```

---

## 📚 Additional Resources

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Real Python](https://realpython.com/)
- [Python Tutor](http://pythontutor.com/) - Visualize code execution
- [Awesome Python](https://awesome-python.com/) - Curated resources

---

**Keep updating these notes as you learn!**

*Last updated: February 2026*