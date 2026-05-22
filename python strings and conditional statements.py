#Strings
a="I am Jyotiraditya Khatua"
print(type(a))

a=("jyotir","Ayushman","Kunal")
b=("Mohit","Srijan","Aman")
print(a+b)

a="1"
print(type(a))

#Join Function
a=["J","Y","O","T","I","R","A","D","I","T","Y","A"]
print((" ").join(a))

#Indexing/Slicing
a="Jyotiraditya Khatua"
print(a[0])
print(a[1])
print(a[7])
print(a[-3])

a="Jyotiraditya Khatua"
print(a[0:6:1])
print(a[6:12:1])
print(a[-7::1])
print(a[-1])
print(a[-13:-7:1])


#String Methods
#Startswith()
a="Jyotiraditya Khatua"
print(a.startswith("a"))
print(a.startswith("J"))

#endswith()
a="Jyotiraditya Khatua"
print(a.endswith("a"))
print(a.endswith("J"))

#capitalize()
a="jyotiraditya Khatua"
print(a.capitalize())

#replace()
a="Jyotiraditya Khatua"
print(a.replace("Jyotiraditya","Mohit"))

a="Jyotiraditya Khatua"
print(a.replace("a","o"))

#find()
a="Jyotiraditya Khatua"
print(a.find("a"))
a="Jyotiraditya Khatua"
print(a.find("J"))

#Count()
a="Jyotiraditya Khatua"
print(a.count("a"))
print(a.count("i"))

#lower()
a="Jyotiraditya Khatua"
print(a.lower())

#upper()
a="Jyotiraditya Khatua"
print(a.upper())

#Center
a="Jyotiraditya Khatua"
print(a.center(50))

#lstrip()
a="Jyotiraditya Khatua"
print(a.lstrip("J"))
a="Jyotiraditya Khatua"
print(a.lstrip("Jy"))

#rstrip()
a="Jyotiraditya Khatua"
print(a.rstrip("a"))
print(a.rstrip("ua"))

#split()
a="Jyotiraditya Khatua"
print(a.split())

#join()
a=["J","Y","O","T","I","R","A","D","I","T","Y","A"]
print(("").join(a))



#CONDITIONAL STATEMENTS
#If
#Else

age=21
if age>18:
    print("can vote")
else:
    print("can not vote")

light=input("enter the colour of light=")

if light =="green":
    print("go")

elif light =="red":
    print("stop")

else:
    print("ready")

age=11
if age<=10:
    print("free ticket for travel")
else:
    print("no free tickets")

age=25
if age<=12 :
   print("child")
elif age<=20:
    print("teen")
elif age<=30:
    print("young")
elif age<=35:
    print("young adult")
else:
    print("adult")

marks=int(input("enter the marks="))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade C")
elif marks>=60 and marks<70:
    print("Grade D")
elif marks>=45 and marks<60:
    print("grade E")
elif marks<45:
    print("fail")
else:
    print("invalid input")

num=1
if num>=5:
    print("greater")
else:
    print("smaller")

a=int(input("enter the number="))
if a%7==0:
    print("divisible")
else:
    print("not divisible")

b=int(input("enter the number="))
if b%2==0:
    print("even")
else:
    print("odd")

num1=int(input("enter the number1="))
num2=int(input("enter the number2="))
num3=int(input("enter the number3="))
num4=int(input("enter the number4="))

if num1>num2 and num1>num3 and num1>num4:
    print("num1 is greatest")
elif num2>num3 and num2>num1 and num2>4:
    print("num2 is greatest")
elif num3>num1 and num3>num2 and num3>num4:
    print("num3 is greatest")
else:
    print("num4 is greatest")

a=int(input("enter the number of year="))
if a%4==0 and a%100!=0 or a%400==0:
    print("leap year")
else:
    print("non leap year")

side1=int(input("enter the side1="))
side2=int(input("enter the side2= "))
side3=int(input("enter the side3="))
if side1==side2 and side1==side3:
    print("equiliteral triangle")
elif side1!=side2 or side2==side3 or side3==side1:
    print("isosceles triangle")
else:
    print("scelene triangle")


num1=int(input("enter the number1="))
operator=input("enter the operator=")
num2=int(input("enter the number2="))

if "+":
    print("result=",num1+num2)
elif  "-":
    print("result=",num1-num2)
elif "*":
    print("result=",num1*num2)
elif "/":
    if num2==0:
      print("not divisible")
    else:
        print("divisible")
else:
    print("invalid input")


z=int(input("enter the number="))
if z%5==0:
    print("multiple of 5")
else:
    print("not multiple of 7")


