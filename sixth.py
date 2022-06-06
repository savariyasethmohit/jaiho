"""a = 1000000
# a = "name"
# a = 120.5
# b = a
b = 1000000
print(b)
print(id(a))
print(id(b))"""

"""a = "name"
print(eval(a))
print(int(0b101))
print(int("0b101", 2))                # int(string/value,base) it give binary becase we provide base 2(for binary)
"""
print(eval("'mohit'"))
a = eval(input("Enter 1st number "))
b = eval(input("Enter 2nd number "))
c = a / b
print(c)

var1 = int(input())
var2 = int(input())
var3 = var1 + var2
var4 = var3 - var2
var5 = var4 * var4
print(var3, var4, var5)
print(type(var5))
