# input a word and traverse through each letter

'''
a=input("")
for i in a:
    print (i)
'''

# list traverse
'''a=[2,3,7,5,3]
for i in (a):
    print (i)'''


# range(start,stop,step)


# even no in list
'''a=[2,3,7,5,3]
for i in (a):
    if i%2==0:
          print (i)'''

'''for i in '123':
    print(i,"hello")'''

#print table
'''
num=int(input())
for i in range(1,11):
    print(num,"*",i, "=", num*i)'''


#factorial== 5!--> 5*4*3*2*1
'''num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(fact)'''


#print number less than n
'''n=int(input())
for i in range(1,n+1):
    print(i)'''

#prime check
'''
num=int(input())
flag=False
for i in range(2,num):
    if (num%i==0):
        flag=False
    else:
        flag=True

if flag==True:
        print("not prime")
else:
        print("prime")'''

#print all even no upto n
'''num=int(input())
for i in range(num):
    if i%2==0:
        print(i)'''


#fabonacci
i=int(input())
x=0
y=1
z=1
print("fabonacci :")
print(x,y,end=" ")
while(z<=i):
    print(z, end=" ")
    x=y
    y=z
    z=y+x
