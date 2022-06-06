# def opendoll(doll):
#     if doll == 1:
#         print("all dolls are open.")
#     else:
#         print(f"doll no. {doll} is open. ")
#         opendoll(doll-1)
#
# opendoll(4)


# factorial programm

# def facto(num):
#     assert num>0 and int(num)==num,"only positive ints are allowed"
#     if num in [0,1]:
#         return 1
#     return num*facto(num-1)
# print(facto(5))



# def prime(x, y):
# 	prime_list = []
# 	for i in range(x, y):
# 		if i == 0 or i == 1:
# 			continue
# 		else:
# 			for j in range(2, int(i/2)+1):
# 				if i % j == 0:
# 					break
# 			else:
# 				prime_list.append(i)
# 	return prime_list
#
# starting_range = 1
# ending_range = 300
# lst = prime(starting_range, ending_range)
# if len(lst) == 0:
# 	print("There are no prime numbers in this range")
# else:
# 	print("The prime numbers in this range are: ", lst)


# def find_gcd(a,b):
#     gcd = 1
#     for i in range(1,a+1):
#         if a%i==0 and b%i==0:
#            gcd = i
#     return gcd
#
# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
#
# print('HCF or GCD of %d and %d is %d' %(first, second, find_gcd(first, second)))
#
# lcm = first * second / find_gcd(first, second)
# print('LCM of %d and %d is %d' %(first, second, lcm))




# def even_numbers(num):
#  if num<=0:
#    return
#  if num % 2 == 0:
#   even_numbers(num - 2)
#   print(num,end=" ")
#
#
# even_numbers(100)

import add
print(add.add(1,2))
print(add.add(8,5))