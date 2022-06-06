# print([n for n in range(1, 8) if(n%2==1)])
# lst = [1,3,8,9]
# print(["true" if(n%3==0) else "false" for n in lst])

# print([n for n in range(2, 10) if(n%n==1 and n%1==n)])


# a = []
# n = int(input("enter the number of elements you want to store in list"))
# for x in range(n):
#     b = eval(input("enter comma seperated values to create a tuple"))
#     a.append(b)
#     print("tuple before remove\n", a)
# for y in a:
#     print(len(y))
#     if len(y) == 3:
#         a.remove(y)
# print(a)


# lst = [[1, 2], [3, 4], [5, 6]]
# lst1 = [1, 2, 3]
# res = {lst1[i]: lst[i] for i in range(len(lst1))}
# print(str(res))




# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
# res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
# print ("Resultant dictionary is : " + str(res))



# Python program to sort the list
# alphabetically in a dictionary
# dict ={
# 	"L1":[87, 34, 56, 12],
# 	"L2":[23, 00, 30, 10],
# 	"L3":[1, 6, 2, 9],
# 	"L4":[40, 34, 21, 67]
# }
#
# print("\nBefore Sorting: ")
# for x in dict.items():
# 	print(x)
#
# print("\nAfter Sorting: ")
#
# for i, j in dict.items():
# 	sorted_dict ={i:sorted(j)}
# 	print(sorted_dict)
#
# test_dict = {"Gfg" : 5, "is" : 5, "Best" : 5}
# print("The original dictionary is : " + str(test_dict))
# res = True
# test_val = list(test_dict.values())[0]
# for ele in test_dict:
# 	if test_dict[ele] != test_val:
# 		res = False
# 		break
# print("Are all values similar in dictionary : " + str(res))

# def CountFrequency(lst):
# 	freq = {}
# 	for item in lst:
# 		if (item in freq):
# 			freq[item] += 1
# 		else:
# 			freq[item] = 1
# 	for key, value in freq.items():
# 		print ("% d : % d"%(key, value))
# if __name__ == "__main__":
# 	lst =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# 	CountFrequency(lst)
