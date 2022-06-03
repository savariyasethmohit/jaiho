# import matplotlib as plt
#
# # Reference for adding title for each sub plots: https://gist.github.com/dyerrington/dac39db54161dafc9359995924413a12
# fig,ax = plt.subplots(2,2, figsize=(10,10))               # 'ax' has references to all the four axes
# plt.suptitle("Understanding the distribution of various factors", fontsize=20)
# sns.distplot(hr['Age'], ax = ax[0,0])  # Plot on 1st axes
# ax[0][0].set_title('Distribution of Age')
# sns.distplot(hr['TotalWorkingYears'], ax = ax[0,1])  # Plot on IInd axes
# ax[0][1].set_title('Distribution of Total Working Years')
# sns.distplot(hr['YearsAtCompany'], ax = ax[1,0])  # Plot on IIIrd axes
# ax[1][0].set_title('Distribution of Years at company')
# sns.distplot(hr['YearsInCurrentRole'], ax = ax[1,1])  # Plot on IV the axes
# ax[1][1].set_title('Distribution of Years in Current Role')
# plt.show()

# try:
#     print(100/0)
#     print("mohit")
#     # print("sharma")
# except ArithmeticError:
#     print("bye")
#     # print("go")
#     # print("back")
# # print("hello")
# except ZeroDivisionError:
#     print("no")
#
# try:
#     Risky code
# except:
#     Handling code
#     will act when any exception/run time error occur
# else:
#     normal code
#     will act when no exception occur it is opposite of except block
# finally:
#     clearing code
#     will act for sure , except occur or occur not


# # -----------------------------map------------
# def fun1(n):
#     return n*n
#
# list1 = [11,12,13,14]
#
# # map function (first argument is ur function name, second argument is ur sequence)
# p = list(map(fun1,list1))
# print(p)
#
# # --------------------------------lambda-------------
# list1 = [11,12,13,14]
# p=list(map(lambda a:a*a*a, list1))
# print(p)


# ----------------------------zip function-------------

# l1=["a",'b','c','d']
# l2=[1,2,3,4]
#
# res=list(zip(l1,l2))
# print(res)


# ------------------------filter function------------

# def checkupper(n):
#     if not n.isupper():
#         return True
#     else:
#         return False
#
#
# str1 = ["amm", "Boy", "tom", "Fox", "SON"]
#
# #  filter(function name, sequences)
# result = list(filter(checkupper, str1))
# print(result)
# ----------------------reduce function------------
from functools import reduce
#
# # reduce()  works differently than map() and filter()
# # reduce() returns a single  value
#
def add(x,y):
    return x+y

list1 = [1,2,3,4]

result = reduce(add,list1)

print(result)


# ----------------------------dec function------------------

# def dec(funarg):
#     def inner(name):
#         if name=="python":
#             print("it is a progrAMMing lang.")
#         else:
#             funarg(name)
#             # functinality work
#     return inner
# @ dec
# def narmalfunc(name):
#     print("hello",name)
#
#
# narmalfunc("sam")
# narmalfunc("jintu")
# narmalfunc("python")

# -----------------------generator function-----------------

# def genfun():
#     yield 'A'
#     yield 'B'
#     yield 'C'
# g = genfun()
# print(next(g)) # it will print the 0th index.
# print(next(g)) # it will print the 1st index
# print(next(g)) # it will print the 2nd index
# print(next(g)) # it will print the 3r index but it will give an error as 3rd element is not there

# n = int(input())
# arr = map(int, input().split(" "))
# print(sorted(list(set(arr)))[-2])

# n = int(input())
# lst=[]
# name = input()
# score = int(input())
# x=lst.append([[name,score]])
# print(x)
#
#
# Result =[]
# scorelist = []
#
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         Result+=[[name,score]]
#         scorelist+=[score]
#     b=sorted(list(set(scorelist)))[1]
#
#     for a,c in sorted(Result):
#         if c==b:
#             print(a)