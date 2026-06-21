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
