# class student():
#     '''
#     student class
#     '''
#     variable1 =10
#     def getdata(self,rollno,name):
#         self.rollno = rollno
#         self.name = name
#         print("self.variable1",self.variable1+1)
#
#         print("print inside getdata function:",stud1.name)
#         print("print inside getdata function:",self.name)
#
#     def display(self):
#         print("Display the data of the student")
#         print("Roll :",self.rollno,"name:",self.name)
#

#  delete object

# stud1 = student()
# print("stud1.variable1:",stud1.variable1)
# stud1.getdata(1,"Avinash")
# stud1.display()
#
# stud2 = student()
# stud1.getdata(2,"Ravi")
# stud1.display()
#
# stud3 = student()
# stud1.getdata(3,"Python_student")
# stud1.display()

# class student(object):
#     "common base class to all students."
#     def __init__(self,rollno,name,course):
#         self.rollno=rollno
#         self.name=name
#         self.course=course
#     def displaystudent(self):
#         print("Roll no : ",self.rollno)
#         print("Name : ",self.name)
#         print("Course : ",self.course)
#
# stud1=student(10,"jack","ms")
# stud1.displaystudent()
#
# print("Student.__doc__:",student.__doc__)
# print("student.__name__:",student.__name__)
# print("student.__module__:",student.__module__)
# print("student.__base__:",student.__base__)
# print("student.__dict__:",student.__dict__)


#  Single inheritance

# class student(object):
#     def getdata(self,roll,name):
#         self.roll=roll
#         self.name=name
#     def displaystudent(self):
#         print("")
#         print("Parent roll : ",self.roll)
#         print("Parent name : ",self.name)
#
# # single inheritance derive class.
#
# class Test(student):
#     def getmarks(self,marks):
#         self.marks=marks
#     def displaymarks(self):
#         print("Child class method calling .")
#         print("Roll no.",self.roll)
#         print("Name :",self.name)
#         print("Total marks : ",self.marks)
#
# r=int(input("Enter roll no. : "))
# n=input("Enter name : ")
# m=int(input("Enter marks : "))
#
# # creatring object.
# # object name=classname
#
# t1=Test()
# t1.getdata(r,n)
# t1.getmarks(m)
# t1.displaystudent()
# t1.displaymarks()


#  Multilevel inheritance

# class school():
#     def getschooldetail(self,schname):
#         self.schname=schname
#
#
# class student(school):
#     def getstudentdetail(self,sname):
#         self.sname=sname
#
# class test(student):
#     def getanddisplay(self,marks):
#         self.marks=marks
#         print(self.schname)
#         print(self.sname)
#         print(self.marks)
#
# t1=test()
# t1.getschooldetail('dav')
# t1.getstudentdetail('sam')
# t1.getanddisplay(200)

# Multiple inheritence
# class school():
#     def getschooldetail(self,schname):
#         self.schname=schname
#
#
# class student():
#     def getstudentdetail(self,sname):
#         self.sname=sname
#
# class test(student,school):
#     def getanddisplay(self,marks):
#         self.marks=marks
#         print(self.schname)
#         print(self.sname)
#         print(self.marks)
#
# t1=test()
# t1.getschooldetail('dav')
# t1.getstudentdetail('sam')
# t1.getanddisplay(200)

#   herarical inheritance
# class school():
#     def getschooldetail(self,schname):
#         self.schname=schname
#
# class student(school):
#     def getstudentdetail(self,sname):
#         self.sname=sname
#         print("School name : ",self.schname)
#         print("Student Name : ",self.sname)
#
# class teacher(school):
#     def getanddisplay(self,tname):
#         self.tname=tname
#         print(self.schname)
#         print(self.tname)
#
#
# t1=teacher()
#
# t1.getschooldetail("dav school")
# t1.getanddisplay("science teacher")
#
# s1=student()
# s1.getschooldetail("dav school")
# s1.getstudentdetail("class2 teacher")



"""# create a simple constructor program in python


class mohit():
    def __init__(self,name,rollno="NA"):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("Name : ",self.name)
        print("Roll no. :",self.rollno)
t1=mohit("Mohit",16)
t1.display()
t2=mohit("Luvkush",13)
t2.display()
t3=mohit("Luvkush",)
t3.display()"""


# HYBRID INHERUTANCE IS A COMBINATION OF TWO OR MORE TYPE OF INHERITANCE

class school:
    def test1(self,name):
        self.name=name
        print("School Name :",self.name)
class student(school):
    def studentdetail(self,sname,roolno):
        self.sname=sname
        self.rollno=roolno

    def displaystudent(self):
        print("school name :",self.name)
        print("student Detail :")
        print("Student Name :",self.sname)
        print("Student Roll no :",self.rollno)
class teacher(school):
    def datateacher(self,tname):
        self.tname=tname

    def displayteacher(self):
        print("School Name",self.name)
        print("Teacher Name",self.tname)

class test(student):
    def getdatatest(self,tmarks,name,roll):
        self.tmarks = tmarks
        self.name = name
        self.roll = roll
        print("student name:",self.name)
        print("student roll:",self.roll)
        print("student marks:",self.tmarks)

test1=input("Enter School Name:")
roll=int(input("Enter Roll no.:"))
name=input("Enter Student Name: ")
tname=input("Enter t Name :")
studentmarks=int(input("Enter the marks : "))

t1=teacher()
t1.school(test1)