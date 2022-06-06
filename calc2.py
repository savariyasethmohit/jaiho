# import calc
#
# print(calc.add(7,8))


# lst = []
# def test(num,lst):
#     lst.append(num)
#
# test(12,lst)
# test(13,lst)
# print(lst)

"""mainlst = ["james","king","neene","black"]

print([len(name) for name in mainlst])

def lenname():
    lst=[]
    for i in mainlst:
        lst.append(len(i))
    return lst
print(lenname())

print(list(map(len,mainlst)))


for i in map(len,mainlst):
    print(i)


for i in map(float,["12.3","34.5","44.6","99"]):
    print(i,type(i))

print("12 34 56".split(" "))

num1,num2,num3=map(int,input("Enter three numbers").split(" "))
print(num1,num2,num3)


lst = [12,13,14,15,16,11,18]
print([i for i in lst if i%2==0])
for i in filter(lambda num:num%2==0,lst):
    print(i)

for i in (filter(lambda num:num%2==0,lst)):
    print(i,end=" ")"""

"""def fibo(lim):
    num1,num2=0,1
    for i in range(lim):
        yield num1
        num1,num2=num2,num1+num2

for i in filter(lambda num:num%2==0,fibo(10)):
    print(i)"""


# def fibo(lim):
#     num1,num2=0,1
#     while True:
#         yield num1
#         num1,num2=num2,num1+num2
#
# for i in filter(lambda num:num%2==0,fibo(10)):
#     print(i)


# for i in map(sum,[[1,3],[4,2,-5]]):
#     print(i)
#

import numpy

import random

# print(random.random())
#
# print(random.randint(1,10))

st = random.getstate()
print(random.random())
print(random.random())
print(random.random())
print(random.random())
random.setstate(st)
print(random.random())
print(random.random())
print(random.choice(["james","anna","neene","king"]))
print(random.choices(["james","anna","neene","king"],weights=[10,2,4,3],k=10))