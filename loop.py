#While Loop
count=0
while count<=10:
    print(count)
    count+=1

i=1
while i<=10:
    print(i)
    i+=1

i=0
while i<=100:
    print("jyotir",i)
    i+=1

i=1
while i<=20:
    print("sandeep",i)
    i+=1

i=20
while i>=1:
    print("jyotir",i)
    i-=1

i=100
while i>=0:
    print("sandeep",i)
    i-=1

a=[1,2,3,4,5,6,7,8,9,10]
x=5
i=0
while i<len(a):
    if i==x:
        print("element found at idx",i)
        i+=1
    else:
        print("finding")
        i+=1

a=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(a):
    print(a[i])
    i+=1

i=1
while i<=10:
    print(5*i)
    i+=1

i=3
while i<=30:
    print(i)
    i+=3

a=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(a):
    if a[i]%2==0:
        print(a[i],"is even")
        i+=1
    else:
        print(a[i],"is odd")
    i+=1

a=[1,2,3,4,5,6,7,8,9,10]
x=9
i=0
while i<len(a):
    if a[i]==x:
        print("element found at idx",i)
        break
    else:
        print("finding")
        i+=1

a=[1,2,3,4,5,6,7,8,9,10]
x=8
i=0
while i<len(a):
    if a[i]==x:
        i+=1
        continue
    print(a[i])
    i+=1

#for loop
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)

b=[12,23,34,45,56,67,78,89,90]
for i in b:
    print(i)

name="jyotiraditya"
for i in name:
    print(i)

name="sandeep"
for i in name:
    if i=="a":
        print("a found")

name="jyotiraditya"
for i in name:
    if i=="a":
        print("a found")
        break
    print(i)
else:
    print("a not found")

d=[9,8,7,6,5,4,3,2,1]
x=5
for i in d:
    if i==x:
        print("element found")
        break
    i+=1


for i in range(5):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)


n=int(input("enter a number"))
for i in range(1,11):
    print(n*i)

#pass statement
for i in range(5):
    pass
print("loop completed")


a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        pass
    else:
        print(i,"is odd")


n=5
sum=0
i=0
for i in range(1,n+1):
    sum+=i

print("sum of first",n,"natural numbers is",sum)


n=int(input("enter a number"))
sum=0
i=0
for i in range(1,n+1):
    sum+=i

print("sum of first",n,"natural numbers is",sum)


n=int(input("enter a number"))
i=0
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial of",n,"is",fact)

n=9
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial of",n,"is",fact)

n=7
sum=1
i=0
while i<=n:
    sum+=i
    i+=1
print("sum of first",n,"natural numbers is",sum)

n=9
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial of",n,"is",fact)