#Dictionary

A={
"a":1,
"b":2,
"c":3,
"d":4
}

print(A)

dicct={
"name":"John",
"age":30,
"city":"New York",
"country":"USA",
"credit _score":[700,750,800],
"married":True
}

print(dicct)
print(dicct["name"])
print(dicct["age"])
print(dicct["city"])


student={
"name":"Alice",
"age":25,
"city":"Los Angeles",
"courses":["Math","Science","History"],
"grade":("A","B","A-"),
"graduated":False
}
print(student)
print(student["name"])
print(student["age"])
print(student["city"])
print(student["courses"])
print(student["grade"])
print(student["graduated"])

#nested dictionary
ram={
"name":"Ram",
"age":30,
"city":"Boston",
"skills":["Python","Java","C++"],
"experience":5,
"employed":True,
"subjects":("Math","Science","History"),
"children":{
"boy":"Rohan",
"girl":"Riya",
"age":5,
"class":1
}
}
print(ram)
print(ram["name"])
print(ram["age"])
print(ram["city"])
print(ram["skills"])
print(ram["experience"])
print(ram["employed"])
print(ram["subjects"])
print(ram["children"] ["age"])
print(ram["children"] ["class"])
ram["age"]=31
print(ram["age"])
ram["city"]="Delhi"
print(ram["city"])
print(ram.get("name"))
print(ram.get("age"))
ram.setdefault("country","India")
print(ram)
ram["jyotir"]="friend"
print(ram)

#dictionary methods
#keys()
print(ram.keys())

#values()
print(ram.values())

#items()
print(ram.items())

#update()
ram.update({"age":32})

#copy()
ram_copy=ram.copy()
print(ram_copy)

#clear()
ram_copy.clear()
print(ram_copy)

#pop()
age=ram.pop("age")
print(age)

#popitem()
last_item=ram.popitem()
print(last_item)

#fromkeys()
keys=["name","age","city"]
default_value="unknown"
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)

#setdefault()
ram.setdefault("country","India")
print(ram)

#get()
print(ram.get("name"))

#dict comprehension
student={
"name":"Alice",
"age":25,
"city":"Los Angeles",
"courses":["Math","Science","History"],
"grade":("A","B","A-"),
"graduated":False
}
new_student={key:value for key,value in student.items() if key!="age"}
print(new_student)
x={key:value for key,value in student.items() if key=="name"}
print(x)

#lambda function with dictionary
square=lambda x:x**2
print(square(5))

student={
"name":"Alice",
"age":25,
"city":"Los Angeles",
"courses":["Math","Science","History"],
"grade":("A","B","A-"),
"graduated":False
}
square_age=lambda x:x**2
print(square_age(student["age"]))

#lOOP with dictionary
student={
"name":"Alice",
"age":25,
"city":"Los Angeles"
}
for key in student:
    print(key, student[key])
for key,value in student.items():
    print(key,value)
for value in student.values():
    print(value)


student={
"name":"Alice",
"age":25,
"city":"Los Angeles",
"courses":["Math","Science","History"],
"grade":("A","B","A-"),
"graduated":False
}
print(type(student))

#SET
s={1,2,3,4,5}
print(s)

a={1,"hello",3.14,True}
print(a)

b=set([1,2,3,4,5])
print(b)

a={1,"hello",3.14,True,(1,2,3)}
print(a)

#set operatiions
#addition()
s1={1,2,3}
s2={4,5,6}
s1.add(9)
print(s1)

#remove()
s1.remove(2)
print(s1)

#discard()
s1.discard(3)
print(s1)

#pop()
s1.pop()
print(s1)

#clear()
s1.clear()
print(s1)

#copy()
s1_copy=s1.copy()
print(s1_copy)

#difference()
s1={1,2,3,4}
s2={3,4,5,6}
diff=s1.difference(s2)
print(diff)

#sysmmetric_difference()
s1={1,2,3,4}
s2={3,4,5,6}
sym_diff=s1.symmetric_difference(s2)
print(sym_diff)

#update()
s1={1,2,3}
s2={4,5,6}
s1.update(s2)
print(s1)

#union()
s1={1,2,3}
s2={3,4,5}
union_set=s1.union(s2)
print(union_set)

#intersection()
s1={1,2,3,4}
s2={3,4,5,6}
intersection_set=s1.intersection(s2)
print(intersection_set)

#set comprehension
b1={5,10,15,20,25}
squared_set={x**2 for x in b1 if x%2==0}
print(squared_set)

b1={5,10,15,20,25}
squared_set={x**2 for x in b1}
print(squared_set)

#lambda function with set
c={1,2,3,4,5}
sq_set=lambda x:x**2
squared_set=set(map(sq_set,c))
print(squared_set)

d={1,2,3,4,5}

even_numbers=set(filter(lambda x:x%2==0,d))
print(even_numbers)

#loop with set
e={1,2,3,4,5}
for num in e:
    print(num)

f={1,2,3,4,5}
for num in f:
    print(num**2)

#Questions
#wap to store word meanings in a dictionary and print the meaning of a word entered by the user.
word_meanings={
    "apple": "a round fruit with red or green skin",
    "banana": "a long yellow fruit with a soft sweet flesh",
    "cat": "a small domesticated carnivorous mammal"
}
word = input("Enter a word: ")
print(word_meanings.get(word, "Word not found"))


#wap given a list of subjects 
subjects={"Math","Science","Math","History","Science"}

unique_subjects=set(subjects)
print(unique_subjects)

#wap to add marks of three subjects in a dictionary and print the total marks.
marks={}
a=int(input("Enter marks for subject 1 "))
b=int(input("Enter marks for subject 2 "))
c=int(input("Enter marks for subject 3 "))
marks["subject1"]=a
marks["subject2"]=b
marks["subject3"]=c

print(marks)
print("Total marks:", sum(marks.values()))

#wap to store 9 and 9.0 in a set
numbers={9,"9.0"}
print(numbers)

numbers={"number":9,"float":9.0}
print(numbers)
