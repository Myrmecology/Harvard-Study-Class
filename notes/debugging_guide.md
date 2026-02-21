# 🐛 Debugging Guide

Systematic approach to finding and fixing bugs in your code.

---

## 🎯 The Debugging Mindset

**Remember:**
- Bugs are learning opportunities
- Every bug teaches you something
- Stay calm and methodical
- Document what you learn

**Golden Rule:**
> "If you can't explain the bug, you don't understand it yet."

---

## 📋 Systematic Debugging Process

### **Step 1: Reproduce the Bug**
```
✅ Can you make it happen again?
✅ What are the exact steps?
✅ Does it happen every time?
✅ What's the expected vs actual behavior?
```

### **Step 2: Isolate the Problem**
```
✅ When did it start working incorrectly?
✅ What changed recently?
✅ Which function/module is involved?
✅ What's the smallest code that shows the bug?
```

### **Step 3: Form a Hypothesis**
```
✅ What do you think is causing it?
✅ Why would that cause this behavior?
✅ Can you test your hypothesis?
```

### **Step 4: Test Your Hypothesis**
```
✅ Add debug output
✅ Use a debugger
✅ Check assumptions
✅ Verify data at each step
```

### **Step 5: Fix and Verify**
```
✅ Make the smallest change possible
✅ Test the fix thoroughly
✅ Ensure you didn't break anything else
✅ Document the fix
```

---

## 🔍 Python Debugging Tools

### **Print Debugging (Simple but Effective)**
```python
# Basic print
print("Value of x:", x)

# Print with type
print(f"x = {x}, type = {type(x)}")

# Print in loops
for i, item in enumerate(items):
    print(f"[{i}] {item}")

# Debug specific conditions
if x < 0:
    print(f"WARNING: Negative value: {x}")

# Use repr() for exact representation
print(repr(my_string))  # Shows quotes, escape chars

# Separator for visibility
print("=" * 50)
print("DEBUG: Function called")
print("=" * 50)
```

### **Assert Statements**
```python
# Verify assumptions
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All must be numbers"
    return sum(numbers) / len(numbers)

# Invariants
assert balance >= 0, f"Balance went negative: {balance}"

# Postconditions
result = complex_calculation()
assert result is not None, "Function returned None unexpectedly"
```

### **Using pdb (Python Debugger)**
```python
# Add breakpoint in code
import pdb; pdb.set_trace()  # Python < 3.7
breakpoint()  # Python 3.7+

# Common pdb commands:
# n (next)     - Execute next line
# s (step)     - Step into function
# c (continue) - Continue execution
# l (list)     - Show source code
# p variable   - Print variable
# pp variable  - Pretty print variable
# w (where)    - Show stack trace
# q (quit)     - Exit debugger
```

### **Logging (Better than Print)**
```python
import logging

# Basic setup
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Log levels (least to most severe)
logging.debug("Detailed information")       # DEBUG
logging.info("General information")         # INFO
logging.warning("Warning message")          # WARNING
logging.error("Error occurred")             # ERROR
logging.critical("Critical problem")        # CRITICAL

# Log with variables
logging.info(f"Processing user {user_id}")

# Log exceptions
try:
    risky_operation()
except Exception as e:
    logging.error(f"Failed: {e}", exc_info=True)  # Includes traceback
```

### **Traceback Analysis**
```python
"""
Example traceback:

Traceback (most recent call last):
  File "script.py", line 10, in <module>
    result = divide(10, 0)
  File "script.py", line 5, in divide
    return a / b
ZeroDivisionError: division by zero

Reading traceback (bottom to top):
1. Error type: ZeroDivisionError
2. Error location: line 5 in divide function
3. What triggered it: line 10 called divide(10, 0)
"""

# Get traceback programmatically
import traceback

try:
    problematic_code()
except Exception:
    traceback.print_exc()
```

---

## 🔧 Common Python Bugs

### **1. Indentation Errors**
```python
# ❌ Wrong
def greet():
print("Hello")  # IndentationError

# ✅ Correct
def greet():
    print("Hello")
```

### **2. Name Errors (Typos)**
```python
# ❌ Wrong
name = "Alice"
print(nmae)  # NameError: name 'nmae' is not defined

# ✅ Use IDE with spell checking
# ✅ Read error message carefully
```

### **3. Type Errors**
```python
# ❌ Wrong
age = input("Age: ")  # Returns string!
if age > 18:  # TypeError: can't compare str and int
    print("Adult")

# ✅ Correct
age = int(input("Age: "))
if age > 18:
    print("Adult")
```

### **4. Index Errors**
```python
# ❌ Wrong
items = [1, 2, 3]
print(items[3])  # IndexError: list index out of range

# ✅ Check length first
if len(items) > 3:
    print(items[3])

# ✅ Or use get for dicts
my_dict.get('key', 'default')
```

### **5. Key Errors (Dictionaries)**
```python
# ❌ Wrong
user = {'name': 'Alice'}
print(user['age'])  # KeyError: 'age'

# ✅ Use .get()
print(user.get('age', 'Unknown'))

# ✅ Or check first
if 'age' in user:
    print(user['age'])
```

### **6. Attribute Errors**
```python
# ❌ Wrong
my_list = [1, 2, 3]
my_list.append(4)
my_list.add(5)  # AttributeError: 'list' has no attribute 'add'

# ✅ Know your data structures
# Lists: append, extend, insert
# Sets: add, update
```

### **7. Import Errors**
```python
# ❌ Wrong
import non_existent_module  # ModuleNotFoundError

# ✅ Check spelling
# ✅ Install module: pip install module_name
# ✅ Verify it's in requirements.txt
```

### **8. Infinite Loops**
```python
# ❌ Wrong
i = 0
while i < 10:
    print(i)
    # Forgot to increment i!

# ✅ Correct
i = 0
while i < 10:
    print(i)
    i += 1  # Don't forget!

# ✅ Or use for loop
for i in range(10):
    print(i)
```

### **9. Mutable Default Arguments**
```python
# ❌ Wrong
def append_to_list(item, lst=[]):
    lst.append(item)
    return lst

# ✅ Correct
def append_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### **10. Scope Issues**
```python
# ❌ Wrong
def increment():
    counter += 1  # UnboundLocalError

counter = 0
increment()

# ✅ Correct
def increment():
    global counter
    counter += 1

# ✅ Better: Return value
def increment(counter):
    return counter + 1

counter = increment(counter)
```

---

## 🎯 Debugging Strategies

### **Binary Search Debugging**
```python
# If bug is in large code block, split in half

# Original (bug somewhere here)
# ... 100 lines of code ...

# Add checkpoint in middle
print("CHECKPOINT: Reached line 50")

# Bug before checkpoint? → Search first half
# Bug after checkpoint? → Search second half
# Repeat until found
```

### **Rubber Duck Debugging**
```
1. Get a rubber duck (or any object)
2. Explain your code line by line to the duck
3. When you can't explain a line clearly, that's likely the bug
4. Often you'll find the bug just by explaining!
```

### **Divide and Conquer**
```python
# Complex function with bug
def complex_function(data):
    step1 = process_data(data)
    step2 = transform(step1)
    step3 = validate(step2)
    return finalize(step3)

# Debug by checking each step
def complex_function(data):
    step1 = process_data(data)
    print(f"After step1: {step1}")
    
    step2 = transform(step1)
    print(f"After step2: {step2}")
    
    step3 = validate(step2)
    print(f"After step3: {step3}")
    
    return finalize(step3)
```

### **Minimal Reproducible Example**
```python
# Start with simplest code that shows bug

# Original complex code
# ... 500 lines ...

# Minimal example
def problematic_function(x):
    return x / 0  # Bug isolated!
```

---

## 🔬 Testing to Prevent Bugs

### **Write Tests**
```python
# Simple assertion tests
def add(a, b):
    return a + b

# Test it
assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0
print("All tests passed!")

# Using unittest
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

### **Edge Cases to Test**
```python
# Always test:
- Empty input: [], "", 0
- Single item: [1], "a"
- Negative numbers: -1, -100
- Zero: 0
- Very large numbers: 999999
- None values
- Boundary conditions
- Invalid input
```

---

## 📚 Error Messages Decoded

### **Common Errors & Solutions**

| Error | Meaning | Solution |
|-------|---------|----------|
| `SyntaxError` | Code isn't valid Python | Check parentheses, colons, indentation |
| `IndentationError` | Spacing is wrong | Use consistent tabs/spaces |
| `NameError` | Variable doesn't exist | Check spelling, define variable first |
| `TypeError` | Wrong type used | Convert types or check logic |
| `ValueError` | Right type, wrong value | Validate input |
| `IndexError` | Index out of range | Check list length |
| `KeyError` | Dictionary key missing | Use .get() or check existence |
| `AttributeError` | Object lacks attribute | Check object type, spelling |
| `ZeroDivisionError` | Divided by zero | Check divisor isn't zero |
| `FileNotFoundError` | File doesn't exist | Check path and filename |
| `ModuleNotFoundError` | Can't import module | Install with pip |

---

## 💡 Pro Debugging Tips

### **1. Read the Error Message**
```
Most common mistake: Not reading the full error!

Error tells you:
- What went wrong
- Where it happened (line number)
- Often how to fix it
```

### **2. Check Recent Changes**
```
Bug just appeared?
→ What did you change?
→ Undo recent changes
→ Add them back one at a time
```

### **3. Google Is Your Friend**
```
Copy exact error message
Add "python" to search
Look for Stack Overflow answers
Check official documentation
```

### **4. Use Version Control**
```bash
# See what changed
git diff

# Find when bug was introduced
git bisect start
git bisect bad          # Current version has bug
git bisect good v1.0    # Old version was fine
# Git will find the breaking commit
```

### **5. Take a Break**
```
Stuck for 30+ minutes?
→ Take a 10-minute break
→ Explain problem to someone
→ Sleep on it
→ Fresh eyes find bugs faster
```

---

## 🛠️ Debugging Checklist

When stuck, work through this list:

- [ ] Read the error message completely
- [ ] Check the line number in error
- [ ] Print values of variables involved
- [ ] Check variable types with `type()`
- [ ] Verify function is being called
- [ ] Check function receives correct arguments
- [ ] Look for typos in variable names
- [ ] Verify indentation is correct
- [ ] Check if imports are successful
- [ ] Test with simpler input
- [ ] Google the exact error message
- [ ] Check Stack Overflow
- [ ] Review recent code changes
- [ ] Explain code to rubber duck
- [ ] Take a break and return fresh

---

## 📝 Debugging Log Template

Keep a log of bugs you fix:
```markdown
## Bug: [Brief Description]
**Date:** 2026-02-21
**Severity:** High/Medium/Low
**File:** filename.py, line 42

**Problem:**
Description of what went wrong

**Root Cause:**
What actually caused the bug

**Solution:**
How you fixed it

**Lessons Learned:**
- What to watch for next time
- How to prevent similar bugs

**Time to Fix:** 30 minutes
```

---

## 🎓 Learning from Bugs

**After fixing a bug, ask yourself:**
1. Why did this happen?
2. How can I prevent it in the future?
3. Should I add a test for this case?
4. Are there similar bugs elsewhere?
5. What did I learn?

**Common patterns you'll notice:**
- Same types of bugs repeat
- Certain areas are bug-prone
- Some fixes create new bugs
- Prevention is easier than fixing

---

**Remember: Every bug makes you a better programmer!**

*Last updated: February 2026*