# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary
# all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.


# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
'''

'''
thisset = {"apple", "banana", "cherry", True, 1, 2} #True and 1 is considered the same value
print(thisset)
'''

'''
thisset = {"apple", "banana", "cherry", False, True, 0} False and 0 is considered the same value:
print(thisset)
print(len(thisset))# length'''

'''
myset = {"apple", "banana", "cherry"}
print(type(myset))'''

'''

thisset = {"apple", "banana", "cherry"}
 for x in thisset:
   print(x)

print("banana" not in thisset)'''


# Add an item to a set, using the add() method:
'''
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
'''

# Add elements from tropical into thisset:

'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)'''


# Add elements of a list to at set
'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
'''


# Remove "banana" by using the remove() method:

'''
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)'''


# Remove "banana" by using the discard() method:
'''
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
'''

# Remove a random item by using the pop() method:

'''
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
'''

# The clear() method empties the set
'''
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)'''

# The del keyword will delete the set completely
'''
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

print(thisset)
          ^^^^^^^
NameError: name 'thisset' is not defined'''


'''
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.

'''

# Join set1 and set2 into a new set:
'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)'''

# Use | to join two sets

'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)'''

# Join multiple sets with the union() method:

'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)'''


# Join a set with a tuple
'''
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)'''

# The update() method inserts the items in set2 into set1

'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
'''

# Join set1 and set2, but keep only the duplicates:
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
'''

# Keep the items that exist in both set1, and set2:

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)'''

# Keep all items from set1 that are not in set2:

'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)'''

# Use '-' to join two sets
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
'''
# Use the difference_update() method to keep only the items from the first set that are not present in the other set:
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)'''

# Keep the items that are not present in both sets
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)'''

# Use ^ to join two sets:
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
'''

# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)'''

# Create a frozenset 
'''
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))'''

