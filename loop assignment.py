# num = 50
# for i in range (1, num):
#     if(i % 2 == 0):
#         print("{0}".format(i))
#

"""Using while loop starting from 1 to 345, print the number that is divisible by 3, 5 or both."""

# start = 1
# end = 345
# while(start<=end):
#     if(start%5==0 or start%3==0):
#       print(start)
#     start += 1
"""3. Run a for loop starting from 0 to 99, print only the numbers that are range between 51 to 67 [Both
inclusive]."""

# start = 0
# end = 99
# for i in range(start,end):
#     if(i>50 and i<68):
#         print(i)
#         i += 1

"""1. Write a python program to find sum of all odd numbers between 1 to n."""
# num = int(input("Enter the number : "))
# for i in range(1,num+1):
#     if(i % 2 != 0):
#         n = int(f"{i}")
#         num += 1
#         sum = n*(n-1)//2
#         print(sum)

# n = input("Enter Number to calculate sum")
# n = int (n)
# sum = 0
# for num in range(0, n+1, 1):
#     if (num % 2 != 0):
#         sum = sum + num
# print("SUM of first ", n, "numbers is: ", sum)

"""2. Write a python program to print multiplication table of any number."""

# n = int(input("Enter the number for table : "))
# for i in range (1,11):
#     a = n*i
#     print(f"{n} * {i} = {a}")


"""3. Write a python program to count number of digits in a number."""
# num = input("Enter any digit : ")
# i = input("enter digit which you can count : ")
# a = num.count(f"{i}")
# print(a)
"""4. Write a python program to find sum of first and last digit of a number."""
# num = int(input("Enter any three digit : "))
# last = num%10
# while(num>=10):
#     num = num//10
# first = num
# sum = last + first
# print(sum)

"""5. Write a python program to enter a number and print its reverse."""
# # num = input("Enter a number : ")
# Num = int(input("Please Enter any Number: "))
# Reverse = 0
# while(Num > 0):
#     Reminder = Num %10
#     Reverse = (Reverse *10) + Reminder
#     Num = Num //10
# print("Reverse of entered number is = %d" %Reverse)






