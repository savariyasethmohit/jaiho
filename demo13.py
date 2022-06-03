# class school():
#     def schooladdress(self, address):
#         self.address = address
#         print("Parent address", self.address)
#
#
# class student():
#     def studentdetail(self, name, roll):
#         self.name = name
#         self.roll = roll
#
#     def displaystudent(self):
#         print("student details : ")
#         print(self.name)
#         print("school address : ", self.address)
#
#
# # Hierarchial inheritant.
#
# class teacher():
#     def getdatateacher(self, teachername):
#         self.teachername = teachername
#
#     def displayteacher(self):
#         print("Teacher name :", self.teachername)
#         print("Teacher address :", self.teacheraddress)
#
#
# # Multilevel inheritant.
#
# class test(student):
#     def getdatatest(self, tmarks, name, roll):
#         self.tmarks = tmarks
#         self.name = name
#         self.roll = roll
#         print("Student Name :", self.name)
#         print("Student roll :", self.roll)
#         print("Student Marks :", self.tmarks)
#
#
# schooladdress = input("Enter school address :")
# roll = int(input("Enter roll number :"))
# name = input("Enter name of the student :")
# teachername = input("Enter name of the teacher :")
# studentmarks = int(input("Enter the marks :"))
#
# t1 = teacher()
# t1.schooladdress(schooladdress)
# t1.getdatateacher(teachername)
# t1.displayteacher()
# s1 = student()
# s1.studentdetail(name, roll)
# s1.schooladdress(schooladdress)
# s1.displaystudent()
#
# t1 = test()
# t1.getdatatest(studentmarks, name, roll)

# polymorphism

# class vehicle():
#     def __init__(self,number=0):
#         self.number=number
#     def __add__(self, other,iii):
#         return ((self.number+other.number+iii.number))
# v1=vehicle(10)
# v2=vehicle(20,33)
# #v3=vehicle(30)
# print(v1+v2)




# Q 1. understand differrenrt types of argument in python


# class abc:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self, other):
#         return (self.a+other.a,self.b+other.b)
#
# a1=abc(2,4)
# a2=abc(5,5)
# print(a1+a2)

# Q 2. simple variable length argument return result in which data type
# Q 3. keyword variable length argument return result in which data type


# class parent():
#     def getdata(self,a,b):
#         pass
#     def get2(self,c):
#         pass
#
# class child():
#     def getdata(self, a, b):
#         pass
# ob1=child()
# ob1.getdata(10,12)
# ob1.get2(2)
# ob2=parent()
# ob2.getdata(33,44)

# class parent():
#     def __init__(self,number):
#         self.number=number
#     def display(self):
#         print("Self.numberofchildclass:",self.number)
#
# class child(parent):
#     def __init__(self,number,address):
#         self.number=number
#         self.address=address
#     def display(self):
#         print("self.numberofchildclass:",self.number)
#         print("self.numberofchildclass:",self.address)
# ob1=parent(10)
# ob2=child(16,'abd')

#
# thickness = int(input("Enter thickness:"))
#
# for j in range(1, 10, 2):
#     print(('H' * j).center(10))
#
# for i in range(6):
#     print(('H' * thickness).center(10), ('H' * thickness).center(30), sep='')
#
# rep = 'H' * thickness * 5
# for i in range(3):
#     print(rep.center(30))
#
# for i in range(6):
#     print(('H' * thickness).center(10),('H' * thickness).center(30),sep='')
#
# for j in range(9, 0, -2):
#     print(('H' * j).center(10).rjust(30))


