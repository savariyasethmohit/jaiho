# lst = list("mohit")
# print(lst)
# lst = [[12]]
# print(lst, type(lst))
# lst = [101, "mohit",1000000000,"noida", (12+4j)]
# print(lst)
# for val in lst:
#     print(val,type(val))

# lst = [12, 23, 45, 46, 67,]
# # print(lst[0], lst[-1], lst[-3:], lst[:3], lst[::2], lst[::2], id(lst), sep="\n")
# # print(lst, id(lst))
# # lst[1] = 1000
# # print(lst, id(lst))
# lst2 = lst
# print(lst, lst2)
# lst2[1] = 1000
# print(lst, lst2)
#
# str1 = 'hello'
# str2 = str1
# print(str1, str2)
# str2 += ' world'
# print(str1, str2)

# lst = [12, 23, 45, 46, 67, ]
# lst.remove(23)
# print(lst)
# lst.clear()
# print(lst)

# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(lst[-1][1])
# for row in lst:
#     for col in row:
#         print(col, end="  ")
# print(lst)
#
# for i in range(3):
#     for j in range(3):
#         lst[i][j] = lst[i][j]+10
#
# print(lst)

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# res = lst1+lst2
# print(res)
# print(lst1)

# lst = [[1, 2, 3], 12, 23, [2, 3, 4], 12]
# for i in lst:
#     if type(i) == list:
#         for j in i:
#             print(j+10)
#     else:
#             print(i+10)


# count = int(input("Enter limit : "))
# lst = []
#
# for i in range(count):
#     val = eval(input("Enter value : "))
#     lst.append(val)
#
# print(lst)

# # list of list
# count = int(input("Enter limit : "))
# lst = []
#
# for i in range(count):
#     clst = []
#     val = eval(input("Enter value : "))
#     for j in range(val):
#         clst.append(int(input("enter num : ")))
#     lst.append(clst)
# print(lst)


# lst1 = [1, [100]]
# lst2 = lst1.copy()
# print(lst1, lst2)
#
# lst2[0] = 20
# print(lst1, lst2)
#
# lst1[1].append(200)
# print(lst1, lst2)
"""
use of deep copy
import copy
lst1 = [1, [100]]
lst2 = copy.deepcopy(lst1)
print(lst1, lst2)
lst1[1].append(200)
print(lst1, lst2)"""


