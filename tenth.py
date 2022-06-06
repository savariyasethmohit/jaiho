# print([i*2 for i in range(20) if i%2==0])
# print([j for i in range(1, 11) for j in range(i) ])
# print([i for i in range(10)])

# d =dict(r="red", g="green", b="blue")
# print(d)
# d = dict([(1, 10),(2, 30),(3, 30)])
# print(d)

# d = {"r":"red","g":"green","b":"blue"}
# d["c"]="cyan"                            # insert the dictionery data
# print(d, id(d))
# del[d["c"]]
# print(d, id(d))
# d["b"] = "black"
# print(d, id(d))

# d = {1:"red", 2:[12, 23], 3:12.5,4:(12, 13), 5:True, 6:"red"}
# print(d)
# d = {}
# d.setdefault("r","red")
# print(d)
# # d.setdefault("d","dark")
# # print(d)
# d["r"]="green"

# print({i:i**3 for i in range (1,11)})
# d = {int(input("Enter key")):input("enter value")}
# print(d)

# st = "mississippi"
# st1 = "abcdefghijklmnopqrstuvwxyz"
# for ch in set(st):
#     if ch in st1:
#         print("char is in the str")
# print(st)

# lst = ["james","neena","ana","paul"]
# for i in range(lst):
#     if(len(i)<=4):
#         lst.append(i)
# print(lst)

# q = ["name","age","address"]
# a = ["mohit","16","goverdhan"]
# d = {}
# for i in zip(q,a):
#     d[i[0]]=i[1]
#     print(d)

import os

os.system("cls")
print("hello")
os.system("pause")