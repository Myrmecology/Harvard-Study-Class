# 🎯 Technical Interview Preparation Guide

Comprehensive guide to preparing for software engineering technical interviews.

---

## 📚 Table of Contents

1. [Interview Process Overview](#process)
2. [Data Structures & Algorithms](#dsa)
3. [Common Problem Patterns](#patterns)
4. [Behavioral Questions](#behavioral)
5. [System Design](#system-design)
6. [Python-Specific](#python)
7. [Problem-Solving Framework](#framework)
8. [Practice Schedule](#schedule)
9. [Day-Before & Day-Of Tips](#tips)

---

## <a name="process"></a>🎭 Interview Process Overview

### **Typical Interview Stages**

**1. Phone Screen (30-45 min)**
- Behavioral questions
- 1-2 easy coding problems
- Culture fit assessment

**2. Technical Phone/Video (45-60 min)**
- Live coding (shared editor)
- 1-2 medium problems
- Code quality matters

**3. Onsite/Virtual Onsite (4-6 hours)**
- Multiple rounds:
  - Coding (2-3 rounds)
  - System design (1-2 rounds)
  - Behavioral (1 round)
  - Optional: Domain-specific

**4. Offer Stage**
- Negotiation
- Team matching
- Final decision

### **What Interviewers Look For**

✅ **Problem-solving ability** - Can you break down problems?  
✅ **Communication** - Can you explain your thinking?  
✅ **Code quality** - Is your code clean and readable?  
✅ **Testing** - Do you think about edge cases?  
✅ **Optimization** - Can you improve your solution?  
✅ **Collaboration** - Do you take feedback well?  

---

## <a name="dsa"></a>💾 Data Structures & Algorithms

### **Must-Know Data Structures**

| Data Structure | Operations to Know | Time Complexity |
|----------------|-------------------|-----------------|
| **Array/List** | Access, insert, delete | O(1), O(n), O(n) |
| **Hash Table** | Insert, lookup, delete | O(1) average |
| **Stack** | Push, pop, peek | O(1) |
| **Queue** | Enqueue, dequeue | O(1) |
| **Linked List** | Insert, delete, search | O(1), O(1), O(n) |
| **Binary Tree** | Insert, delete, search | O(log n) balanced |
| **Heap** | Insert, extract-min/max | O(log n) |
| **Graph** | BFS, DFS, shortest path | Varies |

### **Must-Know Algorithms**

**Sorting:**
- Merge Sort: O(n log n)
- Quick Sort: O(n log n) average
- Know when to use which

**Searching:**
- Binary Search: O(log n)
- BFS/DFS for graphs: O(V + E)

**Other Important:**
- Two Pointers
- Sliding Window
- Dynamic Programming basics
- Recursion

### **Big O Complexity Cheat Sheet**

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array access, hash lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Loop through array |
| O(n log n) | Linearithmic | Merge sort, quick sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive fibonacci |
| O(n!) | Factorial | Permutations |

---

## <a name="patterns"></a>🧩 Common Problem Patterns

### **1. Two Pointers**
```python
# Example: Two Sum in sorted array
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# When to use: Sorted arrays, finding pairs/triplets
```

### **2. Sliding Window**
```python
# Example: Max sum of k consecutive elements
def max_sum_subarray(arr, k):
    max_sum = window_sum = sum(arr[:k])
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# When to use: Subarrays, substrings with constraints
```

### **3. Hash Map / Dictionary**
```python
# Example: Two Sum
def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

# When to use: Need fast lookups, counting, grouping
```

### **4. Binary Search**
```python
# Template
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# When to use: Sorted data, search space reduction
```

### **5. BFS (Breadth-First Search)**
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node)  # Process node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# When to use: Shortest path, level-order traversal, graphs
```

### **6. DFS (Depth-First Search)**
```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)  # Process node
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# When to use: Path finding, tree traversal, backtracking
```

### **7. Dynamic Programming**
```python
# Example: Fibonacci with memoization
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# Pattern: Optimal substructure + overlapping subproblems
# When to use: Optimization problems, counting problems
```

### **8. Backtracking**
```python
# Example: Generate all subsets
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

# When to use: Permutations, combinations, constraint satisfaction
```

---

## <a name="behavioral"></a>💬 Behavioral Questions

### **STAR Method**

**S**ituation - Set the context  
**T**ask - Describe the challenge  
**A**ction - What you did  
**R**esult - Outcome and learning  

### **Common Questions & Approaches**

**"Tell me about yourself"**
```
Structure:
1. Current role/education (30 sec)
2. Relevant experience (1 min)
3. Why this company/role (30 sec)
4. Personal interest/passion (15 sec)

Total: ~2 minutes
```

**"Tell me about a challenging project"**
```
- Pick technical challenge you overcame
- Show problem-solving skills
- Highlight collaboration if applicable
- End with what you learned
```

**"Describe a conflict with a teammate"**
```
- Choose example where you resolved it positively
- Show empathy and communication skills
- Focus on mutual understanding
- Emphasize team success
```

**"Why this company?"**
```
Research:
✅ Company mission/values
✅ Recent product launches
✅ Engineering blog posts
✅ Tech stack
✅ Culture

Be specific, not generic!
```

### **Questions to Ask Interviewer**

**About the Role:**
- What does a typical day look like?
- What are the biggest challenges for this role?
- What does success look like in the first 6 months?

**About the Team:**
- How is the team structured?
- What's the collaboration style?
- How do you handle technical disagreements?

**About Growth:**
- What learning opportunities are available?
- How do you support career development?
- What's the promotion process?

**About the Company:**
- What's the most exciting project coming up?
- How do you measure success?
- What's the engineering culture like?

**⚠️ Avoid:**
- Questions about salary/benefits (save for recruiter)
- Questions answered on company website
- Negative questions about work-life balance

---

## <a name="system-design"></a>🏗️ System Design

### **System Design Interview Structure**

**1. Clarify Requirements (5 min)**
- Functional requirements: What should it do?
- Non-functional: Scale, performance, availability
- Constraints: Users, requests, data size

**2. High-Level Design (10 min)**
- Draw main components
- Data flow
- APIs

**3. Deep Dive (20 min)**
- Scaling strategies
- Database choice
- Caching
- Load balancing

**4. Discuss Tradeoffs (5 min)**
- What could fail?
- How to handle failures?
- Monitoring/metrics

### **Common System Design Topics**

**Must Know:**
- Load balancers
- Caching (Redis, Memcached)
- Database sharding
- CAP theorem basics
- Rate limiting
- CDN

**Good to Know:**
- Message queues (Kafka, RabbitMQ)
- Microservices vs Monolith
- API design
- Consistency patterns
- Replication strategies

### **Classic Questions**

- Design Twitter
- Design URL shortener
- Design Instagram
- Design Uber
- Design Netflix
- Design messaging system

### **Framework for Any System Design**
```
1. Requirements
   - Who uses it?
   - How many users?
   - What features?
   
2. Estimation
   - Traffic: QPS, peak load
   - Storage: How much data?
   - Bandwidth

3. API Design
   - REST endpoints
   - Request/response formats

4. Data Model
   - What to store?
   - SQL vs NoSQL?
   - Schema design

5. High-Level Architecture
   - Client → Load Balancer → App Servers → Database
   - Add cache, CDN as needed

6. Scale
   - Database replication
   - Sharding strategy
   - Caching layers
   - Load balancing

7. Monitoring & Reliability
   - Logging
   - Metrics
   - Alerts
```

---

## <a name="python"></a>🐍 Python-Specific Interview Topics

### **Python Basics**

**Know these cold:**
```python
# List comprehensions
squares = [x**2 for x in range(10)]

# Dictionary comprehensions
counts = {x: x**2 for x in range(5)}

# Lambda functions
sorted(items, key=lambda x: x[1])

# *args and **kwargs
def func(*args, **kwargs):
    pass

# Decorators
@timer
def my_function():
    pass

# Context managers
with open('file.txt') as f:
    content = f.read()

# Generators
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

### **Common Python Interview Questions**

**"What's the difference between list and tuple?"**
- List: mutable, [], slower
- Tuple: immutable, (), faster, can be dict key

**"Explain GIL (Global Interpreter Lock)"**
- Mutex that allows only one thread to execute Python bytecode at a time
- Impacts multi-threaded performance
- Use multiprocessing for CPU-bound tasks

**"How does Python manage memory?"**
- Reference counting
- Garbage collection for circular references
- Memory pools for small objects

**"What are Python decorators?"**
```python
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start}")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

**"Shallow vs Deep Copy?"**
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)      # Copies outer list only
deep = copy.deepcopy(original)     # Copies everything

shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - modified!

deep[0][0] = 999
print(original)  # [[1, 2], [3, 4]] - unchanged
```

---

## <a name="framework"></a>🎯 Problem-Solving Framework

### **Step-by-Step Approach**

**1. Understand the Problem (5 min)**
```
✅ Restate the problem in your own words
✅ Ask clarifying questions:
   - Input format and constraints?
   - Expected output?
   - Edge cases?
   - Performance requirements?
✅ Work through 2-3 examples by hand
✅ Identify edge cases
```

**2. Plan Your Approach (5 min)**
```
✅ Think of brute force solution first
✅ Identify the pattern (two pointers, sliding window, etc.)
✅ Discuss time/space complexity
✅ Consider optimization
✅ Get interviewer's feedback before coding
```

**3. Write Code (15 min)**
```
✅ Start with function signature
✅ Handle edge cases upfront
✅ Write clean, readable code
✅ Use meaningful variable names
✅ Add comments for complex logic
✅ Think out loud as you code
```

**4. Test Your Code (5 min)**
```
✅ Trace through with your example
✅ Test edge cases:
   - Empty input
   - Single element
   - Duplicates
   - Large numbers
   - Negative numbers
✅ Check for off-by-one errors
```

**5. Optimize (5 min)**
```
✅ Analyze time complexity
✅ Analyze space complexity
✅ Discuss potential improvements
✅ Trade-offs of different approaches
```

### **Template for Thinking Out Loud**
```
"Let me make sure I understand the problem..."
[Restate problem]

"So if I have this input... the output should be..."
[Work through example]

"I'm thinking of using [approach] because..."
[Explain reasoning]

"The time complexity would be... and space complexity..."
[Analyze]

"Before I start coding, does this approach make sense?"
[Get confirmation]

[While coding]
"I'm creating a variable here to track..."
"This loop will iterate through..."
"I'm checking this edge case because..."

[After coding]
"Let me trace through with an example..."
"I should also check edge cases like..."
```

---

## <a name="schedule"></a>📅 Practice Schedule

### **8-Week Study Plan**

**Week 1-2: Fundamentals**
- Arrays & Strings (10 problems)
- Hash Tables (10 problems)
- Two Pointers (5 problems)
- Review Big O notation

**Week 3-4: Core Data Structures**
- Linked Lists (10 problems)
- Stacks & Queues (8 problems)
- Trees (12 problems)
- Practice explaining solutions

**Week 5-6: Algorithms**
- Recursion (8 problems)
- Sorting & Searching (10 problems)
- BFS/DFS (10 problems)
- Dynamic Programming basics (8 problems)

**Week 7: Advanced Topics**
- Graphs (8 problems)
- Heaps (5 problems)
- Tries (3 problems)
- Mock interviews

**Week 8: Review & Mock Interviews**
- Review weak areas
- 3-5 mock interviews
- Practice behavioral questions
- System design practice

### **Daily Practice Routine**

**Weekdays (2 hours):**
- 1-2 LeetCode problems (1.5 hrs)
- Review solutions (30 min)

**Weekends (3-4 hours):**
- 3-4 problems (2 hrs)
- Mock interview or system design (1 hr)
- Review week's problems (1 hr)

### **Problem Difficulty Distribution**

**Beginner:** 70% Easy, 30% Medium  
**Intermediate:** 40% Easy, 50% Medium, 10% Hard  
**Advanced:** 20% Easy, 60% Medium, 20% Hard  

---

## <a name="tips"></a>⚡ Day-Before & Day-Of Tips

### **Day Before Interview**

**✅ DO:**
- Review your resume
- Practice 1-2 easy problems (confidence boost)
- Prepare questions for interviewer
- Test your equipment (camera, mic, internet)
- Get good sleep
- Prepare your space (quiet, clean)

**❌ DON'T:**
- Cram new topics
- Practice hard problems
- Stay up late
- Drink excessive caffeine

### **Day Of Interview**

**1 Hour Before:**
- Review key concepts (quick refresher)
- Do a warm-up problem (easy)
- Use bathroom
- Get water nearby
- Close distracting apps/tabs

**During Interview:**

**✅ DO:**
- Greet warmly, show enthusiasm
- Ask clarifying questions
- Think out loud
- Communicate your thought process
- Take hints gracefully
- Test your code
- Admit when stuck and ask for help
- Show you're coachable

**❌ DON'T:**
- Jump into coding immediately
- Stay silent while thinking
- Ignore hints
- Argue with interviewer
- Give up easily
- Panic if stuck

**If You Get Stuck:**
```
"I'm thinking through a couple of approaches..."
"Could you give me a hint about...?"
"Let me try a different approach..."
"Can I talk through my thought process?"
```

**After the Interview:**
- Send thank you email within 24 hours
- Reflect on what went well/poorly
- Note questions asked for future prep

---

## 🎯 Resources for Practice

### **Problem Practice**
- [LeetCode](https://leetcode.com/) - Top choice
- [HackerRank](https://www.hackerrank.com/)
- [CodeSignal](https://codesignal.com/)

### **Mock Interviews**
- [Pramp](https://www.pramp.com/) - FREE peer practice
- [Interviewing.io](https://interviewing.io/) - Anonymous with engineers
- [Exponent](https://www.tryexponent.com/)

### **Study Guides**
- [Tech Interview Handbook](https://www.techinterviewhandbook.org/)
- [Blind 75](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)
- [Grind 75](https://www.techinterviewhandbook.org/grind75)

### **System Design**
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)

### **Books**
- *Cracking the Coding Interview* - Gayle Laakmann McDowell
- *Elements of Programming Interviews* - Python version

---

## 📋 Interview Checklist

**Technical Preparation:**
- [ ] Comfortable with arrays, strings, hash tables
- [ ] Know BFS, DFS, binary search
- [ ] Understand time/space complexity
- [ ] Can explain solutions clearly
- [ ] Practiced 100+ problems
- [ ] Done 5+ mock interviews

**Behavioral Preparation:**
- [ ] Prepared STAR stories
- [ ] Researched company thoroughly
- [ ] Have questions for interviewer
- [ ] Can explain resume clearly
- [ ] Prepared "why this company" answer

**Logistics:**
- [ ] Confirmed interview time/format
- [ ] Tested equipment
- [ ] Have backup (phone/laptop)
- [ ] Quiet, professional space
- [ ] Pen and paper ready
- [ ] Water nearby

---

## 💪 Mindset & Motivation

### **Remember:**

✨ **You don't need to be perfect** - You need to show you can think  
✨ **Interviews are practice** - Each one makes you better  
✨ **Rejection is normal** - Even great engineers get rejected  
✨ **Communication matters more than you think** - Show your process  
✨ **It's okay to ask for help** - Shows you're collaborative  

### **Growth Mindset**

❌ "I'm not good at coding interviews"  
✅ "I'm getting better with each practice session"

❌ "This problem is too hard"  
✅ "This problem will help me learn new patterns"

❌ "I failed that interview"  
✅ "I learned what to improve for next time"

---

**You've got this! Every expert was once a beginner.** 🚀

*Last updated: February 2026*