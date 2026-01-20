'''Here are **GitHub-style, clean & exam-friendly notes** on **Python Lambda Functions**, written in **Markdown** so you can directly paste them into your **README.md / notes repo** 📘✨

---

#  Python Lambda Functions

##  What is a Lambda Function?

A **lambda function** is a **small anonymous function** in Python.


{
An anonymous function is a function without a name.
In Python, lambda functions are anonymous functions because:
They are not defined using def
They do not have a function name
}



* It has **no name**
* Can take **any number of arguments**
* Can have **only one expression**
* The expression is **automatically returned**

---

##  Syntax

```python
lambda arguments : expression
```

---

##  Basic Examples

### ➤ Add 10 to a number

```python
x = lambda a: a + 10
print(x(5))   # Output: 15
```

### ➤ Multiply two numbers

```python
x = lambda a, b: a * b
print(x(5, 6))   # Output: 30
```

### ➤ Add three numbers

```python
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))   # Output: 13
```

---

##  Why Use Lambda Functions?

Lambda functions are useful when:

* You need a **short function**
* You need a function **temporarily**
* You don’t want to define a full function using `def`

They are mostly used **inside other functions** or with **built-in functions**.

---

##  Lambda Inside Another Function

### ➤ Function returning a lambda

```python
def myfunc(n):
    return lambda a: a * n
```

### ➤ Double a number

```python
mydoubler = myfunc(2)
print(mydoubler(11))   # Output: 22
```

### ➤ Triple a number

```python
mytripler = myfunc(3)
print(mytripler(11))   # Output: 33
```

### ➤ Using both together

```python
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))   # 22
print(mytripler(11))   # 33
```

---

## Lambda with Built-in Functions

Lambda functions are commonly used with:

* `map()`
* `filter()`
* `sorted()`

---

##  Lambda with `map()`

**map()** applies a function to **each element** of an iterable.

### ➤ Double all numbers in a list

```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
```

**Output**

```
[2, 4, 6, 8, 10]
```

---

## 🔹 Lambda with `filter()`

**filter()** selects elements for which the function returns **True**.

### ➤ Filter odd numbers

```python
numbers = [1,2,3,4,5,6,7,8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
```

**Output**

```
[1, 3, 5, 7]
```

---

## 🔹 Lambda with `sorted()`

**sorted()** uses lambda as a **key** for custom sorting.

### ➤ Sort tuples by second value

```python
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
```

**Output**

```
[('Tobias', 22), ('Emil', 25), ('Linus', 28)]
```

### ➤ Sort strings by length

```python
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
```

**Output**

```
['pie', 'apple', 'banana', 'cherry']
```

---

## ⚠️ Limitations of Lambda Functions
 Only **one expression**
 Cannot contain statements like `if`, `for`, `while` (normal way)
 Less readable for complex logic
'''