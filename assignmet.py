# def even(num):
#  if num < 0:
#   return
#  if num>0:
#   even(num-2)
#   print(num, end=",")
#
# even(100)

# def odd(num):
#  if num<=0:
#   return
#  if num%2==0:
#   print(num-1,end=",")
#   odd(num-2)
#
# odd(100)

# def T(n) :
#  if n <= 2 :
#   fval = 1
#   return fval
#  else :
#   fval = T(n - 5) + 1.3
#   return fval
# print("Answer of first part :{:.2f}".format(T(510)) )
# print("Answer of second part :{:.2f}".format(T(219)))
# print("Answer of third part :{:.2f}".format(T(782)))

#
# def rev(n, temp):
#  if (n == 0):
#   return temp
#  temp = (temp * 10) + (n % 10)
#  return rev(n // 10, temp)
# n = int(input("Enter the num : "))
# temp = rev(n, 0)
# if (temp == n):
#  print("yes")
# else:
#  print("no")

import numpy as np
# lst=[[64392,31655],[32579,0],[49248,462],[0,0]]
# arr=np.array(lst)
# print(arr,type(arr))
#
# print(f"""
# array shape is:{arr.shape}
# array length is:{arr.itemsize}
# array dimension are:{arr.ndim}
# """)

lst1 = []
arr = np.array(lst1)
n = 90
for i in range(10):
    n += 10
    lst1.append(n)
print(lst1)
B = np.reshape(arr,(5,2))
