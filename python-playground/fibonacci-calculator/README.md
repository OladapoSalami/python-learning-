# 🔢 Nth Fibonacci Calculator

An efficient Python implementation to calculate the n-th number in the Fibonacci sequence using **Dynamic Programming**.

### 🧠 The Approach: Iterative vs. Recursive
While the Fibonacci sequence is often taught using recursion, this project uses an **iterative approach** to optimize performance:
1. **Time Complexity:** $O(n)$ — It only calculates each number once, making it significantly faster than the $O(2^n)$ recursive version.
2. **Space Complexity:** $O(n)$ — Results are stored in a list (memoization) to build the sequence.
3. **Memory Safety:** It avoids "Recursion Depth Errors" which occur in Python when calculating very large Fibonacci numbers.



### 🛠️ Features
* **Dynamic Programming:** Utilizes a list named `sequence` as a cache to build each new number based on the two preceding values.
* **Input Validation:** Designed to handle positive integers, including base cases for $0$ and $1$.
* **Iterative Logic:** Explicitly avoids recursion to ensure maximum efficiency and compatibility.

### 📝 Mathematical Logic
The algorithm follows the standard Fibonacci recurrence relation:
$$F_n = F_{n-1} + F_{n-2}$$

**Example Walkthrough for `fibonacci(5)`:**
* Initial Sequence: `[0, 1]`
* Step 1: $0 + 1 = 1$ → `[0, 1, 1]`
* Step 2: $1 + 1 = 2$ → `[0, 1, 1, 2]`
* Step 3: $1 + 2 = 3$ → `[0, 1, 1, 2, 3]`
* Step 4: $2 + 3 = 5$ → `[0, 1, 1, 2, 3, 5]`
* **Return Value:** $5$

### 💻 Skills Demonstrated
* Algorithm Design
* Dynamic Programming (Memoization)
* Computational Efficiency
* Python List Manipulation
