# number = [10, 2, 89, 7, 64, 78]
# number.sort()
# print("the second largest no. is ", number[-2])


# dupList = [1, 2, 3, 2, 4, 8, 9, 1, 7, 6, 4, 5]
# print("List Items = ", dupList)
#
# uniqSet = set(dupList)
# uniqList = list(uniqSet)
#
# print("List Items after removing Duplicates = ", uniqList)

# lst = [3, 34, 4, 5, 3, 8, 3]
# print("list items are = ", lst)
# uniqset = set(lst)
# uniqlist = list(lst)
#
# print("List Items after removing Duplicates = ", uniqList)

# [output iteration condition]
# names = ["mohit", "sharma", "uday", "satyaprakash"]
# print([name.upper() if(len(name))>=5 else name for name in names])

""" Write a program to remove all the duplicate elements from list."""

# list1 = [10, 20, 10, 20, 30, 40, 30, 50]
# list2 = [50, 30, 70, 80, 90, 10, 60, 45]
# for n in list1:
# 	if n in list2:
# 		print(n)

# print("Original list")
# print("list1: ", list1)


# list = ['mohit', 'xyz', 'satyaprakash', 'amma', 'mom']
# count = 0
# for x in list:
#     if len(x) >= 2 and x[0] == x[-1]:
#         count += 1
# print(count)

# num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# print(max(num, key=sum))

# a = [1, 2, 3, 4, 5]
# # a[::2] = 10, 20, 30, 40, 50, 60
# print(a[3:0:-1])

# a=[10, 23, 56, [78]]
# b=list(a)
# a[3][0]=95
# a[1]=34
# print(b)
# import random
#
# fruit = ['apple', 'banana', 'papaya', 'cherry']
# random.shuffle(fruit)

# data = [[1, 2], [3, 4], [5, 6], [7, 8]]
# res = data[0][0]
# for row in data:
#     for element in row:
#         if res<element: res=element
# print(res)

# arr = [[1, 2, 3, 4],[4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop())

# a=[[]]*3
# a[1].append(7)
# print(a)

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1,6):
#     arr[i - 1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end=" ")


# fruit_list1 = ['apple', 'banana', 'papaya', 'cherry']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
#
# fruit_list2[0] = 'guava'
# fruit_list3[1] = 'kiwi'
#
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'guava':
#         sum += 1
#     if ls[1] == 'kiwi':
#         sum += 20
#
# print(sum)

# a = [1,2,3,4,5,6,7,8,9]
# print(a[::2])




# init_tuple_a = 1, 2
# init_tuple_b = (3, 4)
# [print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

# init_tuple = [(0, 1), (1, 2), (2, 3)]
# result = sum(n for _, n in init_tuple)
# print(result)


# l = [1, 2, 3]
# init_tuple = ('python',) * (len(l) - l[::-1][0])
# print(init_tuple)


# init_tuple = ('python') * 3
# print(type(init_tuple))

init_tuple = (1,) * 3
init_tuple[0] = 2
print(init_tuple)

# init_tuple = ((1, 2),) * 7
# print(len(init_tuple[3:8]))