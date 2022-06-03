# try:
#     file=open("errorlog.txt","a")
#     num1 = int(input("entr 1 num "))
#     num2 = int(input("entr 2 num "))
#     st=f"{num1}//{num2}={num3}"
#     file.write(st)
#     file.close()
#
# except ZeroDivisionError as ob:
#     file.write(str(ob)+"\n")
#     file.close()
# except Exception as ob:
#     file.write(str(ob)+"\n")
# finally:
#     file.close()

# import builtins
# print(dir(builtins))

# try:
#     age=int(input("enter your age "))
#     if 18<=age<=45:
#         print("plse submit ur pv")
#     else:
#         raise ZeroDivisionError("invalid age")
# except ValueError as ob:
#     print(ob)
# except ZeroDivisionError as ob:
#     print(ob)

#
