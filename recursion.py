#recursion
def num(n):
    if n==0:
        return
    print(n)
    num(n-1)

num(5)

def show(n):
    if n==-1:
        return
    print(n)
    show(n-1)

show(9)


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(8))


def calc(n):
    if n==0:
        return 0
    print(n)
    return calc(n-1)+n

print(calc(5))


def op(list,idx):
    if idx==len(list):
        return
    print(list[idx])
    op(list,idx+1)

my_list=[10,20,30,40,50]
op(my_list,0)




def show(n):
    for i in range(n+1,0,-1):
        print(i)

show(5)



def recurse(n):
    if n==100:
        return
    print(n)
    recurse(n+1)


recurse(8)

def recurse(n):
    if n==200:
        return
    print(n)
    recurse(n+1)

recurse(150)


def loop(n):
    for i in range(8,100):
        print(i)

loop(8)


def while_loop(n):
    while n<200:
        print(n)
        n+=1

while_loop(150)
