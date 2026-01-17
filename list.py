'''lst = [10, 20, 30, 40]

print(lst[0])   # 10
print(lst[2])   # 30
print(lst[-1])  # 40
print(lst[-2])  # 30
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(1, 6)))       # [1, 2, 3, 4, 5]
print(list(range(1, 10, 2)))   # [1, 3, 5, 7, 9]

'''

'''#sum of element
lst = [10, 20, 30, 40]
total = 0

for i in lst:
    total += i

print("Sum =", total)'''


# find common elements in the list.
''''
l=[2,3,6,9,10,11,12,65]
l1=[26,43,76,89,70,10,12,65]
for i in l:
    for j in l1:
        if i==j:
            print(i)
'''

# find second largest element in the list
'''
l=[]
n=int(input("element number"))
i=0
for i in range(n):
    num=int(input("element"))
    l.append(num)
print(l)
l.sort(reverse=True)
print(l)
print(l[1])'''

# write a program to delete all the odd numbers in list
'''l=[2,8,12,45,-6,-34,-23,-70,34,56,65]
l2=[]
for i in l:
    if i>0:
        l2.append(i)
print(l2)'''


#count the occurrences
'''l=[10,20,30,40,16,10,15]
num=int(input("enter the element"))
count=0
for i in l:
    if num==i:
        count+=1
print(count)'''


#wap to count number of string where length is 2 or more and the first and last character are same from a given list of string
'''
strings = ['abc', 'xyz', 'aba', '1221', 'aa', 'a']
count = 0
for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1
print("Count =", count)
'''
#wap tht accepts the number from user and print the frequency of the  number in the lst given  as under  given as under if number  is not in lst it should print number not available

'''lst = [1, 2, 3, 4, 2, 5, 2, 6, 3]
num = int(input("Enter a number: "))
count = 0
for i in lst:
    if i == num:
        count += 1
if count > 0:
    print("Frequency of", num, "=", count)
else:
    print("Number not available")'''

# find the unique element from list

'''

l=[2,3,6,9,10,11,12,65]
l1=[26,43,76,89,70,10,12,65]
for i in l:
    if i not in l1:
        print(i, end=" ")

for j in l1:
    if j not in l:
        print(j, end=" ")'''

# element first-half element of list second half elements assuming list having even number
'''
l=[10,20,30,40,50,60,70]
print(l)
x=int(len(l)/2)
for i in range(x):
    l[i],l[x+i]=l[x+i],l[i]
print(l)'''

