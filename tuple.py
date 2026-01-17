'''
t = (10, 20, 30, 40, 50)
print(t[0])   # 10
print(t[2])   # 30
print(t[4])   # 50
print(t[-1])  # 50
print(t[-2])  # 40
print(t[-5])  # 10



t = (5, 10, 15)
for i in range(len(t)):
    print(t[i])



t = (1, 2, (3, 4, 5))

print(t[2])      # (3, 4, 5)
print(t[2][1])   # 4


'''
#input elements in tuple 
'''
t=tuple()
n=int(input("no of elements: "))
for i in range(n):
    a=input("enter the elements ")
    t+=(a,)
print(t)
'''


#linear search
'''
t = (10, 25, 30, 45, 50, 60)

key = int(input("Enter element to search: "))

found = False

for i in range(len(t)):
    if t[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")'''

# swap 2 tuples
'''
t1 = tuple(input("Enter elements of first tuple: ").split())
t2 = tuple(input("Enter elements of second tuple: ").split())

print("Before swapping:")
print("Tuple 1:", t1)
print("Tuple 2:", t2)

t1, t2 = t2, t1   # swapping

print("After swapping:")
print("Tuple 1:", t1)
print("Tuple 2:", t2)'''

