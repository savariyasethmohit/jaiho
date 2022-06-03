import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import win32file

pd.set_option("display.max_rows",200)
pd.set_option("display.max_columns",11)
pd.set_option("display.max_colwidth",30)
pd.set_option("display.width",1000)
emp= pd.read_csv("Employee.csv")
# print(employees[["fname","salary"]])
"""print(emp.info())
print(emp.dtypes)
print(emp.columns)
print(emp.values)
print(len(emp))
print(list(emp.index))
print(emp.shape)

print(emp.head(2))
print(emp.tail(2))
print(emp.iloc[::2, :3])
print(f"""
# {emp['salary'].max()}
# {emp['salary'].min()}
# {emp['salary'].mean()}
# {emp['salary'].sum()}
# {emp['salary'].count()}
""")

print(emp['salary'].describe())
print(emp.describe())
res=emp[['eid','fname','salary','did']]
print(res)
res=(emp[emp['did']==60])[['eid','fname','salary','did']]               # it gives the same did value 
print(res)

res=(emp[(emp['did']==60) & (emp['salary']>5000)])[['eid','fname','salary','did']]               # it gives the same did value and give 5000 above salary data
print(res)

# Use of xlrd python module inbuiltly

Ems = pd.ExcelFile("EMS.xlsx",)
emp=pd.read_excel(Ems,"Sheet1")
dept=pd.read_excel(Ems,"Sheet2")
loc=pd.read_excel(Ems,"Sheet3")
salgrad=pd.read_excel(Ems,"Sheet4")
print(salgrad)
"""

"""# create duplicate file 
Ems = pd.ExcelFile("EMS.xlsx",engine='openpyxl')
emp=pd.read_excel(Ems,"Sheet1")

df=emp[emp["Department_Id"] == 60]
df.to_csv("dept60.csv",index= False)
print(df)"""

Ems = pd.ExcelFile("EMS.xlsx",engine='openpyxl')
emp=pd.read_excel(Ems,"Sheet1").rename(columns={"Employee_Id":"eid","Hire_Date":"Hd","Manager_Id":"Mid","Department_Id":"Did"})
print(emp)






