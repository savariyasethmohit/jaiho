# st = "The quick brown fox jumps over the lazy dog"
# print("a in string st : ")
# print(st.count('a'))
# print("e in string st : ")
# print(st.count('e'))
# print("i in string st : ")
# print(st.count('i'))
# print("o in string st : ")
# print(st.count('o'))
# print("u in string st : ")
# print(st.count('u'))

# st = "The quick brown fox jumps over the lazy dog"
# for st in range ():
#     print(st.bit_count())

# string = "The quick brown fox jumps over the lazy dog"
# vowels = 0
# consonants = 0
# for i in string:
#     if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
#         vowels+=1
# print("Vowels :",vowels)

# str1 = "Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks."
# str2 = "length is even"
# str3 = "length is odd"
# x = len(str1)
# if(x % 2 == 0):
#     print(str1+str2)
# else:
#     print(str1+str3)

# num1 = 10
# num2 = 14
# num3 = 12

# uncomment following lines to take three numbers from user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# larg = num1>=num2 and num1 >= num3 if (largest = num1)
# # if (num1 >= num2) and (num1 >= num3):
# #    largest = num1
# # elif (num2 >= num1) and (num2 >= num3):
# #    largest = num2
# # else:
# #    largest = num3
#
# print("The largest number is", larg)

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# gretest = num1 if num1>num2 else num2
# gretest = num3 if num3>gretest else gretest
# print("Greatest Number is ",gretest)
# num = int(input("Enter the number : "))
# factorial = 1
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1, num + 1):
#        factorial = factorial*i
#    print("The factorial of", num, "is", factorial)

"""4. Write a python program to check whether a number is Prime number or not."""
# num = int(input("Enter the number to check the number is prime or not : "))
# if (num//num==1 and num//1==num):
#    print("YES,", num ,"is prime number ")
# # elif(num%2==1 and num%2==0):
# #    print("NO,", num,"is not prime number")
# else:
#    print("NO,", num,"is not prime number")

# number = int(input("Enter The Number : "))
# if number > 1:
#     for i in range(2, int(number/2)+1):
#         if (number//number==1 and number//1==number and number%2==1 and number%2==0):
#             print(number, "is a Prime Number")
#             break
#         else:
#             print(number,"is not a Prime number")
#             break
# else:
#     print(number,"is not a Prime number")

# number = int(input("Enter the number to check the number is prime or not : "))
# if number > 1:
#     for i in range(2,int(number/2)+1):
#         if (number % i == 0):
#             print(number, "is not a Prime Number")
#             break
#     else:
#         print(number,"is a Prime number")
# # If the number is less than 1 it can't be Prime
# else:
#     print(number,"is not a Prime number")
# import collections
# str1 = 'thequickbrownfoxjumpsoverthelazydog'
# d = collections.defaultdict(int)
# for c in str1:
#     d[c] += 1
# for c in sorted(d, key=d.get, reverse=True):
#   if d[c] > 1:
#       print('%s %d' % (c, d[c]))

st = "32.054,23"
st1 = st[2:3]
st2 = st[6:7]
print(f"{st[0:2]}{st2}{st[3:6]}{st1}{st[7:9]}")



