'''

## What is Recursion?

**Recursion** is a programming technique where a **function calls itself** to solve a problem.

**Simple meaning:**
A function repeats its work by calling itself until a stopping condition is reached.


## Why Use Recursion?

* Useful for problems that can be broken into **smaller similar problems**
* Makes code **short and clear** for mathematical problems
* Often used in **factorial, Fibonacci, tree, and list problems**



## Important Parts of Recursion

Every recursive function must have **two parts**:

### 1. Base Case

**Meaning:**
A condition that **stops the recursion**

**Why needed:**
Without it, the function will call itself forever and crash the program.

---

### 2. Recursive Case

**Meaning:**
The part where the function **calls itself** with a smaller or modified value.

---

## Example: Countdown
'''
def countdown(n):
    if n <= 0:          # Base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)   # Recursive case

countdown(5)
'''

**Explanation:**

* Prints numbers from 5 to 1
* Stops when `n` becomes 0

---

## Example: Factorial

**Factorial meaning:**
Factorial of `n` = `n × (n-1) × (n-2) ... × 1`

```python
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:                 # Recursive case
        return n * factorial(n - 1)

print(factorial(5))
```

---

## Fibonacci Sequence

**Meaning:**
Each number is the **sum of the previous two numbers**

Sequence:

```
0, 1, 1, 2, 3, 5, 8, ...
```

```python
def fibonacci(n):
    if n <= 1:           # Base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
```

---

## Recursion with Lists

### Sum of List Elements

```python
def sum_list(numbers):
    if len(numbers) == 0:    # Base case
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))
```

**Explanation:**

* Adds first element
* Calls function for remaining list

---

### Find Maximum Element in List

```python
def find_max(numbers):
    if len(numbers) == 1:    # Base case
        return numbers[0]
    else:
        max_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_rest else max_rest

print(find_max([3, 7, 2, 9, 1]))
```

---

## Recursion Depth Limit

**Meaning:**
Python limits how many times a function can call itself to avoid crashing.

Default limit is about **1000 calls**.

```python
import sys
print(sys.getrecursionlimit())
```

### Important Warning

Increasing recursion limit may:

* Use too much memory
* Crash the program

Use carefully.

---

## Advantages of Recursion

* Clean and readable code
* Best for mathematical and hierarchical problems

---

## Disadvantages of Recursion

* Slower than loops
* Uses more memory
* Risk of infinite recursion if base case is missing


'''