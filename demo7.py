import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.set_option("display.max_rows",200)
pd.set_option("display.max_columns",200)
pd.set_option("display.max_colwidth",30)
pd.set_option("display.width",2000)
# emp= pd.read_csv("Employee.csv")
"""
Ems = pd.ExcelFile("EMS.xlsx",engine="openpyxl")
emp=pd.read_excel(Ems,"Sheet1")
emp.drop_duplicates(inplace=True)
print(emp[emp.duplicated()])

print(emp)
"""

"""Ems = pd.ExcelFile("EMS.xlsx",engine="openpyxl")
dept=pd.read_excel(Ems,"Sheet2")
# # print(pd.isnull(dept))                         # it give the null value department true --> null  and    false --> data value
dept.dropna(inplace=True)                      # it deletes the value of null values data in main copy
print(dept)
# dept.fillna("no emps",inplace=True)              # it replace the null values to no emps.
# print(dept)"""


# Ems = pd.ExcelFile("EMS.xlsx",engine="openpyxl")
# emp=pd.read_excel(Ems,"Sheet1")
# dept=pd.read_excel(Ems,"Sheet2")
# print(emp["Department_Id"].unique())
# print(emp.columns)
# res=emp[['Employee_Id', 'Name', 'Salary','Department_Id']]
# res.sort_values(by=["Department_Id","Salary"],ascending=[True,False],inplace=True)              # it gives the ascending of department id or it give the descending of salary of same deoartment id .
# print(res.T)

# print(emp[emp["Department_Id"].isin([10,20,30])])
# print(emp[emp["Salary"]>7500])

# res=(emp[emp["Department_Id"]==60])[["Employee_Id","Name","Salary","Department_Id"]]
# res2=(emp[emp["Department_Id"]==40])[["Employee_Id","Name","Salary","Department_Id"]]
# # print(res,res2,sep="\n")
# res3=pd.concat([res,res2],axis=1)
# print(res3)

# rs=pd.merge(left=emp,right=dept,on="Department_Id",how="left")
# print(rs[["Name","Department_Name"]])
#
# res=emp.groupby("Department_Id")
# print(emp.groupby("Department_Id")["Salary"].max())
# print(emp.groupby("Department_Id")["Salary"].count())
# print(res.groups)


# emp=pd.read_csv("Employee.csv")
# print(emp.groupby(["did","jobid"])["salary"].sum())
# res=emp.groupby("did").aggregate({"salary":[sum,max,min,np.mean,np.count_nonzero]})
# print(res)

# res=emp.groupby(["did","jobid"]).aggregate({"salary":[sum,max,min,np.mean,np.count_nonzero]})
# print(res)

emp=pd.read_csv("nba.csv")
res=emp.groupby("Name")["College"].max().count()
print(res)