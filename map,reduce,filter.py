'''built-in functions:

* **map()**
* **filter()**
* **reduce()**

These functions work on **iterables** (list, tuple, etc.) and help process data **without using loops**.

---

## 1. map() Function

### Purpose

Applies a function to **each element** of an iterable and returns the result.

### Syntax

```python
map(function, iterable)
```

### How it works

* Takes one element at a time
* Applies the function
* Returns a **map object** (convert to list to see output)

### Example
'''
'''
def double(n):#better complexity
    return n * 2

n = [5, 6, 7, 8]
res = map(double, n)
print(list(res))
#print(tuple(res))
n = [5, 6, 7, 8] # bad complexity
l2=[]
for i in n:
    i=i*2
    l2.append(i)
print(l2)
'''
'''

### Output

```
[10, 12, 14, 16]
```

**Use map() when you want to modify every element**

---

## 2. reduce() Function

### Purpose

Reduces the entire iterable into **one single value**.

### Module Required

```python
from functools import reduce
```

### Syntax

```python
reduce(function, iterable)
```

### How it works

* Takes first two elements
* Applies the function
* Uses the result with the next element
* Continues until one value remains

### Example


from functools import reduce

n = [1, 2, 3, 4]
prod = reduce(lambda x, y: x * y, n)
print(prod)

### Output

```
24
```

**Use reduce() when you want a single result (sum, product, max, etc.)**

---

## 3. filter() Function

### Purpose

Selects elements from an iterable **based on a condition**.

### Syntax

```python
filter(function, iterable)
```

### How it works

* Function returns **True or False**
* Only True values are kept

### Example

def is_even(n):
    return n % 2 == 0

n = [1,2,3,4,5,6,7,8,9,10]
res = filter(is_even, n)
print(list(res))


### Output

```
[2, 4, 6, 8, 10]
```

**Use filter() when you want to remove unwanted values**

---

## 4. Combined Use of map(), filter(), reduce()

### Example 1: Sum of squares of even numbers

```python
from functools import reduce

n = [1, 2, 3, 4, 5, 6]

res = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, n))
)

print(res)
```

### Output

```
56
```

### Steps

1. filter → [2, 4, 6]
2. map → [4, 16, 36]
3. reduce → 56

---

### Example 2: Product of positive numbers

```python
from functools import reduce

n = [-3, -1, 2, 4, -2, 5]

res = reduce(
    lambda x, y: x * y,
    filter(lambda x: x > 0, n)
)

print(res)
```

### Output

```
40
```

---

### Example 3: Sum of lengths of words containing vowels

```python
from functools import reduce

w = ["sky", "apple", "tree", "gym", "orange"]

res = reduce(
    lambda a, b: a + b,
    map(len, filter(lambda w: any(v in w for v in 'aeiou'), w))
)

print(res)
```

### Output

```
15
```

---

## Quick Comparison Table

| Function | Works On       | Returns           | Use When      |
| -------- | -------------- | ----------------- | ------------- |
| map()    | Each element   | Modified iterable | Change values |
| filter() | Each element   | Filtered iterable | Select values |
| reduce() | Whole iterable | Single value      | Final result  |

---

## One-Line Summary (Important for Exams)

* **map()** → transforms data
* **filter()** → selects data
* **reduce()** → combines data

'''