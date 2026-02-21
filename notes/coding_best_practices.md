# ✨ Coding Best Practices

Write clean, maintainable, and professional code that others (and future you) will love.

---

## 🎯 Core Principles

### **The Zen of Clean Code**
1. **Readability counts** - Code is read 10x more than written
2. **Simple is better than clever** - Don't show off
3. **Explicit beats implicit** - Be clear about intent
4. **Consistency matters** - Follow patterns
5. **Code for humans, not machines** - Computers understand any code; humans don't

### **The Boy Scout Rule**
> "Always leave the code better than you found it."

Even small improvements add up:
- Fix a typo
- Improve a variable name
- Add a comment
- Remove unused code

---

## 📝 Naming Conventions

### **Variables**
```python
# ✅ GOOD - Descriptive, clear
user_age = 25
total_price = 99.99
is_authenticated = True
customer_email_list = []

# ❌ BAD - Vague, unclear
a = 25
x = 99.99
flag = True
data = []
```

### **Functions**
```python
# ✅ GOOD - Verb + noun, describes action
def calculate_total_price(items):
    ...

def send_confirmation_email(user):
    ...

def is_valid_email(email):
    ...

# ❌ BAD - Unclear purpose
def process(data):
    ...

def do_stuff():
    ...

def go():
    ...
```

### **Constants**
```python
# ✅ GOOD - UPPERCASE with underscores
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"

# ❌ BAD
max_retry = 3
Timeout = 30
```

### **Classes**
```python
# ✅ GOOD - PascalCase, nouns
class UserAccount:
    pass

class ShoppingCart:
    pass

class PaymentProcessor:
    pass

# ❌ BAD
class user:  # Should be uppercase
    pass

class process_payment:  # Should be noun, PascalCase
    pass
```

### **Naming Rules of Thumb**
```
✅ Use full words, not abbreviations
   user_count ✓     usr_cnt ✗

✅ Boolean variables should read like questions
   is_valid ✓       valid ✗
   has_permission ✓ permission ✗

✅ Functions should start with verbs
   get_user() ✓     user() ✗
   calculate() ✓    result() ✗

✅ Be consistent across codebase
   get_user() and get_product() ✓
   get_user() and fetch_product() ✗
```

---

## 🧹 Code Organization

### **Function Length**
```python
# ✅ GOOD - Short, focused function
def calculate_discount(price, discount_rate):
    """Calculate discount amount."""
    return price * discount_rate

# ❌ BAD - Too long, does too much (avoid)
def process_order(order):
    """This function is too long..."""
    # 100+ lines of code
    # Multiple responsibilities
    # Hard to understand
```

**Rule of thumb:**
- Functions should do ONE thing
- Ideally under 20 lines
- If you can't name it clearly, it does too much

### **File Organization**
```python
# Good file structure:

# 1. Docstring
"""
Module for user authentication.

This module handles user login, logout, and session management.
"""

# 2. Imports
import os
import sys
from datetime import datetime

# 3. Constants
MAX_LOGIN_ATTEMPTS = 3
SESSION_TIMEOUT = 3600

# 4. Classes
class User:
    ...

# 5. Functions
def authenticate_user(username, password):
    ...

# 6. Main execution
if __name__ == "__main__":
    main()
```

### **Avoid Deep Nesting**
```python
# ❌ BAD - Too deeply nested
def process_data(data):
    if data:
        if data.is_valid:
            if data.has_permission:
                if data.is_active:
                    return process(data)
    return None

# ✅ GOOD - Early returns
def process_data(data):
    if not data:
        return None
    if not data.is_valid:
        return None
    if not data.has_permission:
        return None
    if not data.is_active:
        return None
    
    return process(data)

# ✅ EVEN BETTER - Combined conditions
def process_data(data):
    if not (data and data.is_valid and 
            data.has_permission and data.is_active):
        return None
    
    return process(data)
```

---

## 💬 Comments & Documentation

### **When to Comment**
```python
# ✅ GOOD - Explain WHY, not WHAT
# Using binary search because list is sorted and large (10M+ items)
index = binary_search(sorted_list, target)

# Workaround for API bug (returns null instead of empty array)
results = api_call() or []

# ❌ BAD - Obvious from code
# Increment i by 1
i += 1

# Add item to list
items.append(item)
```

### **Docstrings**
```python
# ✅ GOOD - Clear documentation
def calculate_shipping_cost(weight, distance, express=False):
    """
    Calculate shipping cost based on package weight and distance.
    
    Args:
        weight (float): Package weight in kilograms
        distance (int): Shipping distance in kilometers
        express (bool): Whether to use express shipping (default: False)
    
    Returns:
        float: Shipping cost in dollars
    
    Raises:
        ValueError: If weight or distance is negative
    
    Examples:
        >>> calculate_shipping_cost(2.5, 100)
        15.50
        >>> calculate_shipping_cost(2.5, 100, express=True)
        25.00
    """
    if weight < 0 or distance < 0:
        raise ValueError("Weight and distance must be positive")
    
    base_cost = weight * 2 + distance * 0.1
    return base_cost * 1.5 if express else base_cost
```

### **Comment Anti-Patterns**
```python
# ❌ Commented-out code (delete it - use git!)
# def old_function():
#     return "outdated"

# ❌ Redundant comments
x = x + 1  # Increment x

# ❌ Misleading comments
# Calculate average
total = sum(numbers)  # This doesn't calculate average!

# ❌ TODO comments that never get done
# TODO: Fix this later (written 2 years ago)
```

---

## 🏗️ Code Structure

### **DRY Principle (Don't Repeat Yourself)**
```python
# ❌ BAD - Repetitive code
def calculate_circle_area(radius):
    return 3.14159 * radius * radius

def calculate_circle_circumference(radius):
    return 2 * 3.14159 * radius

def calculate_sphere_volume(radius):
    return (4/3) * 3.14159 * radius * radius * radius

# ✅ GOOD - Use constant
PI = 3.14159

def calculate_circle_area(radius):
    return PI * radius ** 2

def calculate_circle_circumference(radius):
    return 2 * PI * radius

def calculate_sphere_volume(radius):
    return (4/3) * PI * radius ** 3
```

### **Single Responsibility Principle**
```python
# ❌ BAD - Function does multiple things
def process_user_data(user):
    # Validate user
    if not user.email:
        raise ValueError("Email required")
    
    # Save to database
    db.save(user)
    
    # Send welcome email
    email.send(user.email, "Welcome!")
    
    # Log activity
    logger.info(f"User {user.id} created")

# ✅ GOOD - Separate concerns
def validate_user(user):
    if not user.email:
        raise ValueError("Email required")

def save_user(user):
    db.save(user)

def send_welcome_email(user):
    email.send(user.email, "Welcome!")

def log_user_creation(user):
    logger.info(f"User {user.id} created")

def create_user(user):
    validate_user(user)
    save_user(user)
    send_welcome_email(user)
    log_user_creation(user)
```

### **Keep It Simple**
```python
# ❌ BAD - Over-engineered
def is_even(num):
    return True if num % 2 == 0 else False

# ✅ GOOD - Simple
def is_even(num):
    return num % 2 == 0

# ❌ BAD - Unnecessary complexity
numbers = []
for i in range(10):
    if i % 2 == 0:
        numbers.append(i)

# ✅ GOOD - Pythonic
numbers = [i for i in range(10) if i % 2 == 0]

# ✅ EVEN BETTER - Built-in
numbers = list(range(0, 10, 2))
```

---

## 🔒 Error Handling

### **Handle Errors Explicitly**
```python
# ❌ BAD - Bare except catches everything
try:
    result = risky_operation()
except:
    pass  # Silent failure, hard to debug

# ✅ GOOD - Specific exceptions
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    return default_value
except ConnectionError as e:
    logger.error(f"Connection failed: {e}")
    raise
```

### **Fail Fast**
```python
# ❌ BAD - Late validation
def process_payment(amount):
    # ... 50 lines of code ...
    if amount <= 0:
        raise ValueError("Amount must be positive")

# ✅ GOOD - Early validation
def process_payment(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    
    # ... actual processing ...
```

### **Provide Helpful Error Messages**
```python
# ❌ BAD - Vague error
if not user:
    raise ValueError("Error")

# ✅ GOOD - Specific, actionable
if not user:
    raise ValueError(
        f"User with ID {user_id} not found. "
        f"Please check the ID and try again."
    )
```

---

## 🧪 Testing Mindset

### **Write Testable Code**
```python
# ❌ BAD - Hard to test
def process_and_save():
    data = read_from_database()
    result = complex_calculation(data)
    write_to_database(result)
    send_email(result)
    # Can't test without database and email

# ✅ GOOD - Testable functions
def complex_calculation(data):
    return result  # Pure function, easy to test

def process_and_save():
    data = read_from_database()
    result = complex_calculation(data)  # Can test this!
    write_to_database(result)
    send_email(result)
```

### **Test Edge Cases**
```python
# Always test:
def divide(a, b):
    """Test cases needed:
    - Normal: divide(10, 2) -> 5
    - Zero divisor: divide(10, 0) -> ???
    - Negative: divide(-10, 2) -> -5
    - Float: divide(5, 2) -> 2.5
    - Large numbers
    - Zero dividend: divide(0, 5) -> 0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

## 🚀 Performance Considerations

### **Premature Optimization is Evil**
```
1. Make it work ✅
2. Make it right ✅
3. Make it fast ✅ (only if needed)

Don't optimize until:
- You've measured performance
- You've identified bottlenecks
- It's actually a problem
```

### **But Don't Be Wasteful**
```python
# ❌ BAD - Inefficient
for i in range(len(users)):
    if users[i].id == target_id:
        return users[i]

# ✅ GOOD - Pythonic and efficient
for user in users:
    if user.id == target_id:
        return user

# ❌ BAD - Repeated work
for item in items:
    expensive_function()  # Called every iteration!

# ✅ GOOD - Calculate once
result = expensive_function()
for item in items:
    use(result)
```

---

## 🔐 Security Best Practices

### **Never Trust User Input**
```python
# ❌ BAD - SQL Injection risk
query = f"SELECT * FROM users WHERE name = '{user_input}'"

# ✅ GOOD - Parameterized query
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (user_input,))
```

### **Don't Hardcode Secrets**
```python
# ❌ BAD - Secrets in code
API_KEY = "sk_live_abc123..."
DATABASE_PASSWORD = "mypassword123"

# ✅ GOOD - Use environment variables
import os
API_KEY = os.environ.get('API_KEY')
DATABASE_PASSWORD = os.environ.get('DB_PASSWORD')
```

### **Validate and Sanitize**
```python
# ✅ GOOD - Validate input
def create_user(email, age):
    if not is_valid_email(email):
        raise ValueError("Invalid email format")
    
    if not (0 <= age <= 150):
        raise ValueError("Age must be between 0 and 150")
    
    # Proceed with validated data
```

---

## 📊 Code Review Checklist

Before committing code, review:

**Functionality:**
- [ ] Code works as intended
- [ ] Edge cases handled
- [ ] Errors handled gracefully

**Readability:**
- [ ] Variable names are clear
- [ ] Functions have single responsibility
- [ ] Code is DRY (no repetition)
- [ ] Comments explain "why", not "what"

**Quality:**
- [ ] No magic numbers (use constants)
- [ ] No commented-out code
- [ ] No debug print statements
- [ ] Follows style guide (PEP 8)

**Testing:**
- [ ] Tests written for new code
- [ ] All tests pass
- [ ] Edge cases tested

**Security:**
- [ ] No hardcoded secrets
- [ ] User input validated
- [ ] SQL injection prevented

---

## 🎯 Quick Win Improvements

### **Use Built-ins**
```python
# ❌ Reinventing the wheel
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# ✅ Use built-in
total = sum(numbers)
```

### **List Comprehensions**
```python
# ❌ Verbose
squares = []
for i in range(10):
    squares.append(i**2)

# ✅ Concise
squares = [i**2 for i in range(10)]
```

### **F-Strings**
```python
# ❌ Old style
message = "Hello, " + name + "! You are " + str(age)

# ✅ Modern
message = f"Hello, {name}! You are {age}"
```

### **Context Managers**
```python
# ❌ Manual cleanup
f = open('file.txt')
content = f.read()
f.close()

# ✅ Automatic cleanup
with open('file.txt') as f:
    content = f.read()
```

---

## 📚 Resources for Further Learning

- [PEP 8 - Python Style Guide](https://pep8.org/)
- [Clean Code by Robert Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/)
- [Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)

---

**Remember: Good code is code that's easy to change!**

*Last updated: February 2026*