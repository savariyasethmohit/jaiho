
#  -------------------- Making our Exception Handeling---------------------
#  apna khud ka error banana


# class InvalidAge(Exception):
#     def __init__(self,msg="Error"):
#         self.msg=msg
#
#     def __str__(self):
#         return self.msg
#
# age=int(input("Enter your age "))
# if 18<=age<=45:
#     print("plse submit ur pv")
# else:
#     raise InvalidAge()


# except ValueError as ob:
#     print(ob)
# except ZeroDivisionError as ob:
#     print(ob)

#
# # --------------  Assertion Error (statement error)---------------
#
# def checkage(age):
#     assert age>=18,"age must be greater than 17 "
#     print("u r alwd ")
#
# checkage(int(input("Enter Your Age ")))