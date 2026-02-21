# 🧮 Algorithms & Data Structures

Master computer science fundamentals through implementation and problem-solving.

---

## 📚 Topics Covered

| Category | Algorithms | Difficulty | Status |
|----------|-----------|-----------|--------|
| **Sorting** | 6 algorithms | ⭐⭐ | ⬜ |
| **Searching** | 4 algorithms | ⭐⭐ | ⬜ |
| **Recursion** | 5 problems | ⭐⭐⭐ | ⬜ |
| **Dynamic Programming** | 5 problems | ⭐⭐⭐⭐ | ⬜ |
| **Data Structures** | 9 implementations | ⭐⭐⭐ | ⬜ |
| **Graph Algorithms** | 7 algorithms | ⭐⭐⭐⭐ | ⬜ |

**Total: 36 Implementations**

---

## 📁 Directory Structure
```
algorithms/
├── sorting/
│   ├── bubble_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── README.md
├── searching/
│   ├── linear_search.py
│   ├── binary_search.py
│   └── README.md
├── recursion/
│   ├── factorial.py
│   ├── fibonacci.py
│   ├── tower_of_hanoi.py
│   └── README.md
├── dynamic_programming/
│   ├── knapsack.py
│   ├── longest_common_subsequence.py
│   └── README.md
├── data_structures/
│   ├── linked_list.py
│   ├── stack.py
│   ├── queue.py
│   ├── binary_tree.py
│   ├── hash_table.py
│   └── README.md
└── graph_algorithms/
    ├── bfs.py
    ├── dfs.py
    ├── dijkstra.py
    └── README.md
```

---

## 🎯 Learning Approach

### **1. Understand the Concept**
- Read about the algorithm/data structure
- Understand when and why to use it
- Study time and space complexity

### **2. Study Example Implementation**
- Review code in this repository
- Trace through execution step-by-step
- Understand edge cases

### **3. Implement from Scratch**
- Close reference materials
- Write implementation yourself
- Test with various inputs

### **4. Analyze Complexity**
- Calculate Big O notation
- Identify best/average/worst cases
- Compare with alternatives

---

## 📖 Algorithm Implementations

### **Sorting Algorithms**

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable |
|-----------|-------------|------------|--------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

### **Searching Algorithms**

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Requirements |
|-----------|-------------|------------|--------------|-------|--------------|
| Linear Search | O(1) | O(n) | O(n) | O(1) | None |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Sorted array |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) | Sorted array |
| Interpolation | O(1) | O(log log n) | O(n) | O(1) | Uniformly distributed |

---

## 💡 Study Tips

### **For Each Algorithm:**

**Before Coding:**
1. ✅ Understand the problem it solves
2. ✅ Study the approach (pseudocode)
3. ✅ Work through example by hand
4. ✅ Identify edge cases

**While Coding:**
1. ✅ Start with simple version
2. ✅ Add comments explaining logic
3. ✅ Test with small inputs
4. ✅ Handle edge cases

**After Coding:**
1. ✅ Test with various inputs
2. ✅ Analyze time complexity
3. ✅ Analyze space complexity
4. ✅ Optimize if possible
5. ✅ Compare with other solutions

---

## 🧪 Testing Your Implementations
```python
# Example test structure
def test_sorting_algorithm():
    # Test cases
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3])
    ]
    
    for input_arr, expected in test_cases:
        result = your_sort(input_arr.copy())
        assert result == expected, f"Failed on {input_arr}"
    
    print("All tests passed!")

test_sorting_algorithm()
```

---

## 📊 Complexity Analysis

### **Big O Notation**

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Fibonacci (naive) |
| O(n!) | Factorial | Permutations |

### **Common Patterns:**
- **Loops:** Usually O(n)
- **Nested loops:** Usually O(n²)
- **Divide and conquer:** Usually O(n log n)
- **Recursion:** Depends on tree depth

---

## 🎓 Learning Objectives

By completing this section, you will:

✅ Implement classic algorithms from scratch  
✅ Understand time and space complexity  
✅ Choose appropriate data structures  
✅ Analyze algorithm efficiency  
✅ Solve problems recursively  
✅ Apply dynamic programming  
✅ Work with graph algorithms  
✅ Pass technical interviews  

---

## 🏆 Recommended Order

### **Week 1: Sorting & Searching**
1. Bubble Sort → Selection Sort → Insertion Sort
2. Linear Search → Binary Search
3. Compare and analyze all sorting algorithms

### **Week 2: Data Structures**
1. Stack → Queue
2. Linked List (Singly → Doubly)
3. Binary Tree

### **Week 3: Recursion**
1. Factorial → Fibonacci
2. Tower of Hanoi
3. Practice thinking recursively

### **Week 4: Advanced Algorithms**
1. Merge Sort → Quick Sort
2. Hash Table
3. Graph traversal (BFS, DFS)

### **Week 5: Dynamic Programming**
1. Study memoization concept
2. Fibonacci (DP approach)
3. Knapsack problem

### **Week 6: Graph Algorithms**
1. Dijkstra's algorithm
2. Advanced graph problems
3. Review and practice

---

## 🔗 Additional Resources

**Visualization:**
- [VisuAlgo](https://visualgo.net/) - Algorithm visualizations
- [Algorithm Visualizer](https://algorithm-visualizer.org/)

**Practice:**
- [LeetCode](https://leetcode.com/) - Coding problems
- [HackerRank](https://www.hackerrank.com/domains/algorithms)
- [CodeSignal](https://codesignal.com/)

**Books:**
- "Introduction to Algorithms" (CLRS)
- "Algorithms" by Sedgewick & Wayne
- "Grokking Algorithms" by Aditya Bhargava

**Video:**
- [MIT OpenCourseWare - Algorithms](https://ocw.mit.edu/)
- [Abdul Bari's Algorithm Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)

---

## 🎯 Interview Preparation

### **Most Important for Interviews:**
1. ✅ Arrays and Strings
2. ✅ Hash Tables
3. ✅ Linked Lists
4. ✅ Trees and Graphs
5. ✅ Sorting and Searching
6. ✅ Dynamic Programming (advanced roles)

### **Practice Strategy:**
1. Master 1-2 problems per pattern
2. Time yourself (30-45 min per problem)
3. Explain your thought process out loud
4. Analyze complexity before coding
5. Test with edge cases

---

## 🏅 Milestones

- [ ] First sorting algorithm implemented
- [ ] All sorting algorithms completed
- [ ] Binary search mastered
- [ ] First data structure built from scratch
- [ ] Recursion concepts understood
- [ ] First graph algorithm implemented
- [ ] Dynamic programming basics mastered
- [ ] All 36 implementations completed
- [ ] **Algorithms section mastered!** 🎉

---

**Start with:** `sorting/README.md`

*"Algorithms + Data Structures = Programs" - Niklaus Wirth*