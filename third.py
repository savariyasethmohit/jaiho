"""
 Tuples :-
tuple is different from list because in tuple small brackets are use,
tuple value can not change it is immutable
 """
# tp = (1, 2, 3)      # tuple syntax = {name =(value , value2 ,value3 ,....)}
# print(tp)           # printing a tuple.

#  Swapping the values :--
# tamp = a
# a = b
# b = tamp
# a = 2
# b = 3
# a, b = b, a
# print(a, b)
# List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 4, 2, 2]
# print(List.count(2))

# lst = [1, 2, 3, 4]
# tup = tuple(lst)
# print(tup,type(tup))
# tup = (12, 12, 12, 34, 56, 78, 90)
# print(tup,type(tup))
# print(tup.count(12))
# print(tup.index(12))

# tup = (12, 34.45, "mohit", [12, 23, 34])
# print(tup[0], tup[-1], tup[::-1], sep="\n")
# tup[-1].append(1000)
# print(tup)


# res = 1, 2, 3, 4, 5, 6
# print(res,type(res))
# *x, y = res
# print(x, y, sep=" ")

# num1 = 0
# num2 = 2
# print(num1, num2, end="\n")
# for i in range(8):
#     num3 = num1 + num2
#     print(num3, end="\n")
#     num1 = num2
#     num2 = num3

# num1 = 0
# num2 = 1
# print(num1, num2, end="\n")
# for i in range(8):
#     num1, num2 =num2, num1+num2
#     print(num1, num2, end="\n")