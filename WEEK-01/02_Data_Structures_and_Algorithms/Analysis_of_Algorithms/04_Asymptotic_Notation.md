# Asymptotic Notation

## Introduction

Asymptotic Notation is a mathematical method used to describe how an algorithm performs as the input size increases. It helps compare algorithms based on their growth rate rather than actual execution time.

## Big O (O)

Big O Notation represents the **worst-case** performance of an algorithm. It indicates the maximum time or space an algorithm may require.

**Examples:**

- Linear Search → **O(n)**
- Binary Search → **O(log n)**

---

## Big Omega (Ω)

Big Omega represents the **best-case** performance of an algorithm. It shows the minimum amount of work required under ideal conditions.

**Example:**

- Linear Search → **Ω(1)**

---

## Big Theta (Θ)

Big Theta represents the **average-case** or **tight bound** of an algorithm. It describes the expected performance when the input size grows.

**Example:**

- Linear Search → **Θ(n)**

---

## Complexity Comparison

| Complexity | Growth Rate |
|------------|-------------|
| **O(1)** | Constant |
| **O(log n)** | Logarithmic |
| **O(n)** | Linear |
| **O(n log n)** | Linearithmic |
| **O(n²)** | Quadratic |

## Conclusion

Understanding asymptotic notation helps developers evaluate and compare algorithms, making it easier to choose efficient solutions for different computational problems.