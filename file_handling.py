from pyparsing import line


file=open("demo.txt","r")
t=file.read()
print(t)
file.close()


file=open("demo.txt","w")
u=file.write("welcome to python programming")
print(u)
file.close()


file=open("demo.txt","a")
v=file.write("\npython is a high level programming language")
print(v)
file.close()


file=open("demo.txt","r")
s=file.readline()
print(s)
file.close()

file=open("demo.txt","w")
i=file.writelines(["I am Jyotiraditya and I am going to himachal for a vacation.\n"])
print(i)
file.close()



file=open("demo.txt","r+")
j=file.write("i am jyotiraditya and i am going to himachal for a vacation.\n")
print(j)
k=file.read()
print(k)
file.close()



file=open("demo.txt","w+")
l=file.writelines(["i am jyotiraditya and i am going to manali for a vacation.\n"])
print(l)
file.close()


file=open("demo.txt","a+")
m=file.write("i am jyotiraditya and i love pattykulcha of amritsar.\n")
print(m)
n=file.read()
print(n)
file.close()

with open("demo.txt","r") as file:
    print(file.read())


with open("demo.txt","w") as file:
    file.write("i am jyotiraditya and i am going to manali for a vacation.\n")
print("file written successfully")

with open("demo.txt","w") as file:
     s=file.writelines(["i am jyotiraditya and i am going to manali for a vacation.\n"])
     print("file written successfully")


with open("demo.txt","a") as file:
    p=file.write("i am jyotiraditya and i love pattykulcha of amritsar.\n")
print("file appended successfully")



def check_lines():
    word=input("enter a word to check in the file: ")
    data=True
    with open("demo.txt","r") as file:
        for line in file:
            if word in line:
                print("the word is present in the file")
                data=False
                break
    if data:
        print("the word is not present in the file")
    else:
        print("the word is present in the file")

check_lines()


def check_for_lines():
    data=True
    word=input("enter a word to check in the file: ")
    line_no=1
    with open("demo.txt","r") as file:
        while data:
            line=file.readline()
            if word in line:
                print("the word is present in the file at line number",line_no)
                data=False
            line_no+=1

check_for_lines()


def check_for_lines():
    word=input("enter the word:")
    line_no=1
    data=True
    with open ("demo.txt","r") as f:
        while data:
            line=f.readline()
            if word in line:
                print("the word is present in the file at line number",line_no)
                data=False
                line_no+=1


check_for_lines()


with open("practice.txt","r") as file:
    s=file.read()
    print(s)


    num=""
    for i in range(len(s)):
        if s[i] == ",":
            print(int(num))
            num=""
        else:
            num+=s[i]
nums=s.split(",")
for val in nums:
    if int(val)%2==0:
        print(int(val),"is even")
        i+=1
        print(i)
    else:
        print(int(val),"is odd")
        
