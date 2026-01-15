#print number less than n
'''n=int(input())
for i in range(1,n+1):
    print(i)'''

n=int(input("end"))
i=int(input("start"))
sum=0
while i<=n:
    print (i)
    sum+=i
    i+=1
print("sum", sum)