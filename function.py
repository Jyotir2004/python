#function
def sum(a,b):
    add=a+b
    print("the sum is",add)
    return add

sum(2,6)
sum(10,20)

def minus(a,b):
    print("the difference is",a-b)
    return a-b

minus(10,5)
minus(20,10)

def multiply(a,b):
    product=a*b
    print("the product is",product)
    return product

multiply(5,6)
multiply(10,20)

def division(a,b):
    divide=a/b
    print("the division is",divide)
    return divide

division(10,5)
division(20,10)

def modulus(a,b):
    print("the modulus is",a%b)
    return a%b

modulus(10,3)
modulus(20,7)

def power(a,b):
    square=a**b
    print("the power is",square)
    return square

power(2,3)
power(5,2)

def floor_division(a,b):
    print("the floor division is",a//b)
    return a//b

floor_division(10,3)
floor_division(20,7)

def average(a,b,c):
    avg=(a+b+c)/3
    print("the average is",avg)
    return avg

average(10,20,30)
average(5,10,15)

def product(a,b=8):
    result=a*b
    print("the product is",result)
    return result

product(5)

def maximum(a,b):
    if a>b:
        print("the maximum is",a)
        return a
    else:
        print("the maximum is",b)
        return b
    
maximum(10,20)

def minimum(a,b=7):
    if a<b:
        print("the minimum is",a)
        return a
    else:
        print("the minimum is",b)
        return b

minimum(20)

def equal(b,a=10):
    if a==b:
        print("the numbers are equal")
        return True
    else:
        print("the numbers are not equal")
        return False
equal(10)
equal(5)


def  addition(b,a=10):
    add=a+b
    print("the addition is",add)
    return add

addition(5)

def greet():
    print("hello, welcome to python programming")
    return "greeted"

greet()


def hello():
    print("hello, how are you?")
    return "greeted"

hello()

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def lambai(list):
    print(len(list))
    return len(list)

lambai(list1)
lambai(list2)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("the factorial is",fact)
    return fact

factorial(5)
factorial(10)

def currency_calc(usd_val):
    inr_val=usd_val*88
    print("the value in INR is",inr_val,"usd_val",usd_val)
    return inr_val,usd_val

currency_calc(100)
currency_calc(50)

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b

fibonacci(10)


def area_of_square(side):
    area=side*side
    print("the area of the square is",area)
    return area

area_of_square(5)


def area_of_rect(length,breadh):
    area=length*breadh
    print("the area of the rectangle is",area)
    return area

area_of_rect(5,10)


def  circumference_of_circle(radius):
    circumference=2*3.14*radius
    print("the circumference of the circle is",circumference)
    return circumference

circumference_of_circle(5)


def category(n):
    if n<12 and n>0:
        print("teen")
    if n<=20 and n>12:
        print("young")
    if n<=30 and n>20:
        print("young adult")
    if n<=50 and n>30:
        print("adult")
    if n>50:
        print("senior")
    
category(10)


def is_even(n):
    if n%2==0:
        print(n,"is even")
        return True
    
    else:
        print(n,"is odd")
        return False
    
is_even(10)
is_even(7)

def is_prime(n):
    if n%n==0:
        print(n,"is prime")
        return True
    
    else:
        print(n,"is not prime")
        return False
    
is_prime(7)


def is_palindrome(s):
    if s.copy()==s.reverse():
        print("the list is palindrome")
        return True
    

    else:
        print("the list is not palindrome")
        return False
    
is_palindrome([1,2,3,2,1])


def say_good_morning():
    print("good morning")
    return "greeted"

say_good_morning()

def sum(n):
    add=0
    for i in range(1,n+1):
        add+=i
    print("the sum is",add)
    return add

sum(5)

def  reverse_number(n):
    if list(str(n)).copy()==list(str(n)).reverse():
        print("this is actual number")
    else:
        print("this is not actual number")

reverse_number([12321])


def find():
    print("i am jyotir")
    return "found"

find()