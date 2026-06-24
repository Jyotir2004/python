class student:
    name="jyotir"
    age=22
    love="music"
    skills="python"

S1=student()
print(S1.name)
print(S1.age)
print(S1.skills)
print(S1.love)

s2=student()
print(s2.name)
print(s2.age)



class car:
    brand="Mahindra"
    model="XL100"
    colour="blue"
    price="10 lakh"

c1=car()
print(c1.brand)
print(c1.colour)
c2=car()
print(c2.price)
print(c2.model)


class student:
    name="jyotir"

    def __init__(self):
        print("student added to the database")
       

s1=student()
print(s1)
print(s1.name)



class country:
    def __init__(self):
        print("students marksheet")



    def __init__(self,name,grade):
        self.n=name
        self.g=grade
        print("adding student")


p=country("jyotir","A+")
print(p.g)
print(p.n)
print(p)


p2=country("mohit","A")
print(p.g)
print(p.n)




class topper:
    name="Ramesh Sharma"
    college_name="odpd"

    def __init__(self,name,marks):
        self.n=name
        self.m=marks
        print("adding student to database")


s1=topper("alsj",90)
print(s1.name)


class jyotir:
    def __init__(self,name,age,marks):
        self.n=name
        self.a=age
        self.m=marks


    def music(self):
        print("arjit and atif are my fav singers")


    @staticmethod
    def artist():
        print("i love music")

    def get_marks(self):
        return self.m

j1=jyotir("jyotir","23","98")
print(j1.music())
print(jyotir.artist())
print(j1.get_marks())

    
class marks:
    def __init__(self,name,marks):
        self.n=name
        self.m =marks
    
    @staticmethod
    def hello():
        print("hello")

    def average(self):
        sum=0
        for val in self.m:
            sum+=val
            print("average",sum/3)

m1=marks("jyotir",marks=[90,89,67])
print(m1.average())
print(m1.hello())

        
#abstaction
class car:
    def __init__(self):
        self.acc=False
        self.b=False
        self.c=False

    def start(self):
        self.acc=True
        self.b=True
        self.c=True
        print("car started")

c2=car()
print(c2.start())
        

from abc import ABC, abstractmethod
class veichle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(veichle):
        def start(self):
            print("car start with key")

class bike(veichle):
    def start(self):
        print("bike strt with button")

c1=car()
print(c1.start())
b1=bike()
print(b1.start())


class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("dog bark")

class cat(animal):
    def sound(self):
        print("car meow")

d1=dog()
print(d1.sound())
c2=cat()
print(c2.sound())



#encapsulation
class Bankaccount:
    def __init__(self,name,balance):
        self.n=name
        self.b=balance

    def deposit(self,amount):
        if amount>0:
            self.b+=amount
            print("amount deposited")
            print("total balance",self.get_balance())

    def withdraw(self,amount):
        if amount<self.b:
            self.b-=amount
            print("amount withdwan from account")
            print("total amount",self.get_balance())

    def get_balance(self):
        return self.b
    
b1=Bankaccount("jyotir",balance=20000)
print(b1.deposit(5000))
print(b1.withdraw(10000))



# class student:
#     def __init__(self,name,grade):
#         self.n=name
#         self.g=grade

#     s1=student(name="jyotir",grade="A+")
#     print(s1.name())
#     print(s1.grade())



#mro
class grandfather:
    def grand_func(self):
        print("grand farher func")

class father:
    def grand_func(self):
        print("fathers func")

class uncle:
    def grand_func(self):
        print("uncles fuc")

class child(grandfather,father,uncle):
    def grand_func(self):
        pass

C1=child()
print(C1.grand_func())
print(child.__mro__)




class grandparent:
    def grand_func(self):
        print("grandparent function")

class parent:
    def parent_func(self):
        print("parent function")

class uncle:
    def uncle_func(self):
        print("uncle function")

class child(parent, uncle, grandparent):
    def child_func(self):
        super(uncle, self).grand_func()
        #pass

c=child()
c.grand_func()

print(child.mro())
print(child.__mro__)


#class method

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name


    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


s1 = Student("Jyotir")

print(s1.school)

Student.change_school("XYZ School")

print(s1.school)


class ramesh:
    colour="gold"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def dress(self):
        print("wears bold")

r1=ramesh("suresh",35)
print(r1.name)
# del r1
print(r1.name)
print(r1.colour)
# del (r1.colour)
print(r1.colour)

#private

class dhurander:
    def __init__(self,name,type):
        self.__name=name
        self.type=type
    
    def nationality(self):
        print(self.__name)

d1=dhurander("hamza","agent")
# print(d1.name)
print(d1.nationality())


class som:
    __gender="male"

    def __init__(self,name):
        self.name=name
 
    def show_gender(self):
        print(som.__gender)


s1=som("aman")
print(s1.show_gender())


class op:
    def __init__(self,name,type):
        self.name=name
        self.type=type


    def __yo(self):
        return "he is rockstar"
    
    def honey(self):
        print(self.__yo)

o1=op("rakesh","male")
print(o1.honey())




#Inheritance

#single inheritance
class car:
    def start(self):
        return "car started"

    def stop(self):
        return "car stopped"

class veichle(car):
    def __init__(self,name):
        self.name=name

v1=veichle("toyota")
print(v1.start())
print(v1.stop())

class vijay:
    @staticmethod
    def position():
        print("CM")

    def oppsition(self):
        print("rahul gandhi")

class modi(vijay):
    def pm(self):
        print("modi is pm")



m1=modi()
print(m1.position())
print(m1.oppsition())

#multilevel inheritance

class op:
    def emote(self):
        return "played op"
    def player(self):
        return "DJ Alok"
    
class dynamo(op):
    def play(self):
        return "play pubg"
class format(dynamo):
    @staticmethod
    def top_knotch():
        return "head shot"
    
class whole(format):
    def __init__(self,type):
        self.type=type

w1=whole("pubg")
print(w1.play())
print(w1.top_knotch())


class car:
    def start(self):
        return "car started"

    def stop(self):
        return "car stopped"

class veichle(car):
    def __init__(self,name):
        self.name=name
class two_wheeler(veichle):
    def __init__(self,type):
        self.type=type

t1=two_wheeler("disel")

print(t1.start())
print(t1.stop())

#Multiple inheritance

class A:
    def letter(self):
        print("i am the first letter")

    def start(self):
        print("aman")

class B:
    @staticmethod
    def pagal():
        return "main pagal hu"
    
    def akshr(self):
        return "i am second letter"
    
class C:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def guy(self):
        return self.name
    
class D(A,B,C):
    def all_three(self):
        return "yes all three"
    def none(self):
        return self.age
    
d=D("sodj","jdwo")
print(d.pagal())
print(d.akshr())


#hierchial inheritance

class animal:
    def livingz(self):
        return "lop"
    
class cat(animal):
    def ion(self):
        return "zjaix"
    
class dog(animal):
    def neo(self):
        return "PKZAO"
    
d=dog()
print(d.livingz())
print(d.neo())


#hybrid inheritance
class moon:
    def color(self):
        return "white"
    
class planet(moon):
    def big(self):
        return "planets are big"
    

class oxsi(moon):
    def horn(self):
        return "blow horn"
    
class posy(planet,oxsi):
    def hurray(self):
        return "got you"
    
p=posy()
print(p.horn())
print(p.big())
print(p.color())



#super method()

class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        return "start the car"
    
    @staticmethod
    def stop():
        return "stop the car"
    

class Toyota(car):
    def __init__(self,name,type):

       self.name=name
       super().__init__(type)


T=Toyota("priyus","Disel")
print(T.stop())


class person:
    name="anonymus"
    @classmethod
    def changename(cls,name):
        cls.name=name


p1=person()

p1.changename("OP")
print(p1.name)


class school:
    school_name="APS"

    def __init__(self,name):
        self.name=name


    @classmethod
    def change_school_name(cls,new_name):
        cls.school_name=new_name

s1=school("AKTU")
s1.change_school_name("AKTU")
print(s1.name)


#@property

class student:
    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem

        @property
        def percentage(self):
            return str((self.phy+self.math+self.phy)/3)+ "%"
        
s1=student(90,89,87)
# print(s1.percentage())

# s1.phy=88
# print(s1.percentage())


#polymorphismc
class cricket:
    def player(self):
        return "rohit sharma"
    
class football:
    def player(self):
        return "ronaldo"
    
class Basketball:
    def player(self):
        return "micheal Jorden"
    
op=[cricket(),football(),Basketball()]


for i in op:
    print(i.player())
 

class dog:
    def make_sound(self):
        return "bark"
    
class cat:
    def make_sound(self):
        return "meow"
    
class jyotir:
    def make_sound(self):
        return "talk"
    
def create_sound(living_being):
    living_being.make_sound()

create_sound(dog())
create_sound(cat())


class A:
    def a(self):
        return "i am A"
    
class B(A):
    def b(self):
        return "i am B"
    
a1=A()
print(a1.a())
b1=B()
print(b1.b())



#getter and setter
class iron:
    def __init__(self,age):
        self.__age=age


    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            return self.__age
        else:
            return "invalid age"
        
i=iron(78)
print(i.get_age())
print(i.set_age(78))
print(i.get_age())


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show_number(self):
        print (self.real,"i+",self.img,"j")

    def __add__(self,num2):
        new_real=self.real+num2.real
        new_img=self.img+num2.img
        return Complex(new_real,new_img)

num1=Complex(1,3)
print(num1.show_number())

num2=Complex(8,9)
print(num2.show_number())

class circle:
    def __init__(self,radious):
        self.radious=radious

    def area(self):
        return (22/7*self.radious)**2
    
    def perimeter(self):
        return (2*22/7*self.radious)
    
c1=circle(78)
print(c1.area())
print(c1.perimeter())


class Employee:
    def __init__(self,role,dept,salary):
        self.r=role
        self.d=dept
        self.s=salary


    def show_details(self):
        print("role",self.r)
        print("dept",self.d)
        print("salary",self.s)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age

        super().__init__("Engineer","IT",7500000000000000000)

Engg=Engineer("Virat",22)
print(Engg.show_details())



class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price


    def __gt__(self,order2):
        return self.price>Order2.price
    

Order1=Order("chips",56)
Order2=Order("kurkure",65)
print(Order1>Order2)