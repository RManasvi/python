'''a="independence day"
print(len(a))
print(a[3])
print(a[6])
print(a[7])
print(a[9])
print(a[10])
print(a[-10])
print(a[15])
print(a[-15])
print(a[-2])
print(a[:-2:7])
print(a[::-1])
print(a[:9])
print(a[5:])
'''

# count the occurances
'''
s=input("")
ch=input("")
count=0
for i in s:
    if i==ch:
        count+=1
print(count)
'''

#reverse the sting
'''
s=input("")
print(s[::-1])
'''



#opetations in string

# concatenation
'''
a = "Hello"
b = "World"
print(a + " " + b)

'''
#repetition
'''
s = "Hi "
print(s * 3)
'''
#membership
'''
s = "Python"
print("P" in s)
print("z" not in s)
'''
#comparision
'''print("apple" == "apple")
print("Apple" > "apple")
'''
#slicing
'''
s = "Python"
print(s[0:4])   # From index 0 to 3
print(s[2:])    # From index 2 to end
print(s[:5])    # From start to index 4
print(s[::-1])  # Reverse string

'''
#  String Methods 

'''


##  Case Conversion Methods

| Method         | Description                           | Example                 | Output        |
| -------------- | ------------------------------------- | ----------------------- | ------------- |
| `upper()`      | Converts to uppercase                 | `"python".upper()`      | `PYTHON`      |
| `lower()`      | Converts to lowercase                 | `"PYTHON".lower()`      | `python`      |
| `title()`      | Capitalizes first letter of each word | `"hello world".title()` | `Hello World` |
| `capitalize()` | Capitalizes first character           | `"python".capitalize()` | `Python`      |
| `swapcase()`   | Swaps upper & lower case              | `"PyThOn".swapcase()`   | `pYtHoN`      |



##  Searching & Counting Methods

| Method         | Description                       | Example                     | Output |
| -------------- | --------------------------------- | --------------------------- | ------ |
| `find()`       | Returns index, `-1` if not found  | `"python".find('o')`        | `4`    |
| `index()`      | Returns index, error if not found | `"python".index('p')`       | `0`    |
| `count()`      | Counts occurrences                | `"hello".count('l')`        | `2`    |
| `startswith()` | Checks starting substring         | `"python".startswith('py')` | `True` |
| `endswith()`   | Checks ending substring           | `"python".endswith('on')`   | `True` |



##  Checking Type of Characters

| Method      | Description        | Example              | Output |
| ----------- | ------------------ | -------------------- | ------ |
| `isalpha()` | Only alphabets     | `"abc".isalpha()`    | `True` |
| `isdigit()` | Only digits        | `"123".isdigit()`    | `True` |
| `isalnum()` | Alphabets + digits | `"abc123".isalnum()` | `True` |
| `isspace()` | Only spaces        | `"   ".isspace()`    | `True` |
| `islower()` | All lowercase      | `"python".islower()` | `True` |
| `isupper()` | All uppercase      | `"PYTHON".isupper()` | `True` |



##  Split & Join Methods

| Method    | Description             | Example                           | Output                  |
| --------- | ----------------------- | --------------------------------- | ----------------------- |
| `split()` | Splits string into list | `"I love Python".split()`         | `['I','love','Python']` |
| `join()`  | Joins list into string  | `" ".join(['I','love','Python'])` | `I love Python`         |



##  Replace & Whitespace Methods

| Method      | Description               | Example                    | Output  |
| ----------- | ------------------------- | -------------------------- | ------- |
| `replace()` | Replaces substring        | `"hello".replace('h','H')` | `Hello` |
| `strip()`   | Removes spaces both sides | `"  hi  ".strip()`         | `hi`    |
| `lstrip()`  | Removes left spaces       | `"  hi".lstrip()`          | `hi`    |
| `rstrip()`  | Removes right spaces      | `"hi  ".rstrip()`          | `hi`    |



##  Other Useful Methods

| Method        | Description                           | Example                   | Output          |
| ------------- | ------------------------------------- | ------------------------- | --------------- |
| `len()`       | Returns length of string *(function)* | `len("python")`           | `6`             |
| `center()`    | Centers string                        | `"hi".center(6,'*')`      | `**hi**`        |
| `zfill()`     | Fills with zeros                      | `"42".zfill(5)`           | `00042`         |
| `partition()` | Splits string into 3 parts            | `"a=b".partition('=')`    | `('a','=','b')` |
| `istitle()`   | Checks title case                     | `"Hello World".istitle()` | `True`          |





* Strings are **immutable**
* `len()` is a **function**, not a string method
* `find()` → returns `-1`
* `index()` → gives **error** if not found
* `split()` returns **list**
* `join()` works on **iterable only**
* `startswith()` / `endswith()` return **Boolean**



'''


# check if string is palndrome
'''s=input("")
s1=s[::-1]
if s==s1:
    print("palindrome")
else:
    print("not palindrome")'''

# count the number of vowel
'''
s=input("")
vowel=0
cons=0
for i in s:
    if i.lower() in ('a','e','i','o','u'):
        vowel+=1
    else:
        cons+=1
print("vowel",vowel)
print("consonent",cons)'''

#count the number of words
'''
line=input("")
l=line.split()
count=0
for i in l:
    count+=1
print(count)
'''

# print every 2nd letter as capital
'''
s = input("Enter string: ")
result = ""
for i in range(len(s)):
    if i % 2 == 1:
        result += s[i].upper()
    else:
        result += s[i].lower()
print(result)
'''

# Read Longest String in a Line

'''

line = input("Enter a line: ")
words = line.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest string:", longest)'''

# Remove Vowels from a String
'''s = input("Enter string: ")
result = ""
for ch in s:
    if ch.lower() not in "aeiou":
        result += ch
print("String without vowels:", result)'''
