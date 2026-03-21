#List
from filecmp import cmp


l=[1,23,34,56,87,12]
print(l)
print(type(l))

#indexing/slicing
print(l)
print(l[2])
print(l[1:6])
print(l[-1])
print(l[-4])
print(l[0:6:2])
print(l[-4:-1:2])

#list mutating
l=[1,23,34,56,87,12]
l[3]=60
print(l)
l[2]=50
print(l)
l[0:4]=[23,56,78,90]
print(l)
l[-1]=100
print(l)
l[-3:-1]=[72,20]
print(l)

l=[1,23,34,56,87,12]
del l[3]
print(l)

#List cocatenation
l1=[1,23,34]
l2=[56,87,12]
print(l1+l2)

l4=[1,23,34]
l5=[56,87,12]
l6=l4+l5
print(l6)


#list methods
#append()
l=[1,23,34,56,87,12]
l.append(100)
print(l)

#extend()
l=[1,23,34,56,87,12]
l2=[100,200,300]
l.extend(l2)
print(l)

#sort()
l=[1,23,34,56,87,12]
l.sort()
print(l)

#reverse()
l=[1,23,34,56,87,12]
l.reverse()
print(l)

#descending order
l=[1,23,34,56,87,12]
l.sort(reverse=True)
print(l)

#insert()
l=[1,23,34,56,87,12]
l.insert(2,48)
print(l)

#remove()
l=[1,23,34,56,87,12]
l.remove(23)
print(l)

#pop()
l=[1,23,34,56,87,12]
l.pop()
print(l)

l=[1,23,34,56,87,12]
l.pop(3)
print(l)

#count()
l=[1,23,34,56,87,12]
count = l.count(23)
print(count)
print(l.count(56))

#copy()
l=[1,23,34,56,87,12]
l2=l.copy()
print(l2)

#clear()
l=[1,23,34,56,87,12]
l.clear()
print(l)

#index()
l=[1,23,34,56,87,12]
l.index(12)
print(l.index(12))

#list comprehension
l=[1,23,34,56,87,12]
a=[x for x in l if x%2==0]
print(a)

l=[1,23,34,56,87,12]
a=[x**2 for x in l]
print(a)

l=[1,23,34,56,87,12]
a=[x for x in l if x%2!=0]
print(a)

l=[1,23,34,56,87,12]
a=[x**3 for x in l]
print(a)

l="Jyotiraditya Khatua"
a=[x for x in l if x!=""]
print(a)
b="".join(a)
print(b)

#list with lambda function
a=[1,23,34,56,8]
p=list(map(lambda x:x**2, a))
print(p)

a=[1,23,34,56,8]
o=list(filter(lambda x:x%2==0,a))
print(o)

c=[1,23,34,56,8]
q=list(map(lambda x:x**3,c))
print(q)

d=[1,23,34,56,8]
s=sorted(d,key= lambda x: x)
print(s)

n=[1,23,34,56,8]
z=sorted(n, key= lambda x: x)
print(z)

#nested list
l=[3,9,6,7]
b=[1,8]
l.append(b)
print(l)


#loops in list
w=[1,23,34,56,87,12]
for i in w:
    print(i)

name=["J","y","o","t","i","r","a","d","i","t","y","a"]
for i in name:
    print(i)

w=[1,23,34,56,87,12]
i=0
while i<(len(w)):
    print(w[i])
    i+=1




#TUPLE
a=(1,23,34,56,87,12)
print(a)
print(type(a))

#indexing/slicing
print(a[2])
print(a[1:5])
print(a[-1])
print(a[-4])
print(a[0:4:1])
print(a[-5:-1:1])
print(a[-5:-1:2])

#tuple concatenation
a=(1,23,34)
b=(56,87,12)
print(a+b)


c=(1,23,34)
d=(56,87,12)
m=c+d
print(m)

#tuple methods
#count()
t=(1,23,34,56,87,12)
print(t.count(34))
print(t.count(56))

w=(1,23,34,56,87,12)
print(w.count(1))

#index()
k=(1,23,34,56,87,12)
print(k.index(23))
print(k.index(56))

#pcking or unpacking()
x=(1,23,34)
p,q,r=x
print(x)

tup1 = (10,20,30)
a,b,c=tup1
print(a)
print(b)
print(tup1)

tup1=(10,20,30)
a,*b=tup1
print("a",a,"b",b)

tup1 = (10,20,30)
x, *y = tup1
print ("x: ", x, "y: ", y)

q=(1,23,34,56,87,12)
a,b,c,*d=q
print("a",a,"b",b,"c",c,"d",d)

#named tuple
from collections import namedtuple
a=namedtuple("a",["name","age","city"])
p1=a("Jyotiraditya",22,"Kolkata")
print(p1.name)
print(p1.age)

from collections import namedtuple
c=namedtuple("c",["name","age","city"])
o=c("Jyotiraditya",22,"Kolkata")
print(o.name)
print(o.age)
print(o.city)


#loops in tuple
b=(1,23,34,56,87,12)
for i in b:
    print(i)

m=(1,23,34,56,87,12)
i=0
while i<(len(m)):
    print(m[i])
    i+=1

#tuple with lambda function
a=(1,23,34,56,8)    
f=tuple(map(lambda x:x**2, a))
print(tuple(f))    

b=(1,23,34,56,8)
g=tuple(filter(lambda x:x%2==0,b))
print(tuple(g))

m=(1,23,34,56,8)
h=sorted(m,key=lambda x:x)
print(tuple(h))

#Questions
#1. Write a Python program to create a list of sequence of 3 movies
movies=[]
a=input("enter the movie1=")
b=input("enter the movie2=")
c=input("enter the movie3=")
movies.append(a)
movies.append(b)
movies.append(c)
print(movies)

#2. Write a Python program to create a list of palindrome words and numbers from a given list of words and numbers.
a=[1,2,2,2,1]
o=a.copy()
o.reverse()
if o==a:
    print("palindrome")
else:
    print("not palindrome")

a=["a","b","b","a"]
x=a.copy()
x.reverse()
if x==a:
    print("palindrome")
else:
    print("not palindrome")


a=["C","D","A","A","B","B","A"]
f=tuple(a)
print(f)
print(f.count("A"))
m=list(f)
m.sort()
print(m)


