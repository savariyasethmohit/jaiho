import numpy as np
import pandas as pd
import numpy as ap

# 1.
# lst=int(input())
# print(lst)
# n=len(lst)
# try:
#     for i in range(n+1):
#         print(lst[i])
# except:
#     print("Now you Have to gone faa")




# 2.

# try:
#     x = int(input("Enter the string : "))
# except ValueError as ob:
#     print("Please enter a integer value")



# 3.
# import math as mt
#
# try:
#     num=int(input("Enter the number : "))
#     b=mt.sqrt(num)
# except ValueError as ob:
#     print("Don't give Negative value")
#
# num=int(input("Enter the number : "))
# b=mt.sqrt(num)
# print(b)


# 4.
#
# class InvalidMarks(Exception):
#     def __init__(self,msg="Please give next time correct marks."):
#         self.msg=msg
#
#     def __str__(self):
#         return self.msg
#
# sturecord={}
# for i in range(5):
#     id=int(input("Enter the student I'd : "))
#     sturecord.update({id:""})
# for i in sturecord.keys():
#     marks=int(input("Enter the Marks of Student : "))
#     if marks<=100 and marks>=0:
#         sturecord[i]=marks
#     else:
#         try:
#             raise InvalidMarks()
#         except InvalidMarks as ob:
#             sturecord[i]=int(input("Please give correct marks : "))
#             print(ob)
# print(sturecord)



# 5.
#
# class InvalidId(Exception):
#     def __init__(self,msg="Please give correct I'd"):
#         self.msg=msg
#
#     def __str__(self):
#         return self.msg
#
# dict={1:["Rasmalai",'100 Rs','1 hr','1 Kg'],2:["Spang",'30 Rs','2 hr','1 piece'],3:["kaju katali",'40 Rs','2 hr','250 gram']}
# n=int(input("Enter the Dish I'd : "))
# try:
#     if n in dict:
#         print(dict[n])
#     else:
#         raise InvalidId()
# except InvalidId as ob:
#     print("Please give correct I'd")














"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''
sr=pd.Series(data=[12,23,34,35,46],index=range(10,15))
print(sr[1])

sr=pd.Series(data=[12,23,34,35,40],index=(1,1,2,2,3))
print(sr[1])

sr=pd.Series(data=['KGF','RRR','POS','DDLJ','HNY'],index=('****','****','*****','**','*'))
print(sr[['****','*']])

sr=pd.Series(data={1:10,2:20,3:30,4:40,6:50},index=[1,2,4,5])
print(sr)

print(df[["placement","students"]])

fig,ax=plt.subplots(2)
ax[0].plot(df.year,df.placement,label="placement")
ax[1].plot(df.year,df.students,label="students")
ax[0].set_xlabel("year")
ax[0].set_ylabel("placement")
ax[1].set_xlabel("year")
ax[1].set_ylabel("students")
plt.suptitle("student record")
plt.legend()
plt.title("placement record")
plt.grid()
plt.tight_layout()
plt.show()



print(df)

df["stu&fac"]=df["students"]+df["faculty"]
#print(df.iloc[1])
df.loc[6]=[2021,400,40,400,440]
df.loc[7]=[2022,500,40,500,540]
print(df)



clg={"year":[2015,2016,2017,2018,2019,2020,2021],"students":[2000,3000,4000,3200,2100,800,400],
     "faculty":[150,170,200,150,100,30,10],"placement":[2000,2800,1000,400,100,40,400]}

df=pd.DataFrame(clg)
df["stu&fac"]=df["students"]+df["faculty"]
print(df)
#del(df["stu&fac"])
#print(df)
df.drop(5,inplace=True)
print(df)
df.drop("stu&fac",axis=1,inplace=True)
print(df)
print(df.iloc[3])
'''
"""


