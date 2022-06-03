import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# sr=pd.Series(data=['KGF','RRR','POS','DDLJ','HNY'],index=['*****','****','***','****','**'])
# print(sr[['*****','**']])

# sr=pd.Series(data={1:10,2:20,3:30,4:40,6:50},index=[1,2,4,5,6])
# print(sr)

clp={"year":[2015,2016,2017,2018,2019,2020,2021],"students":[2000,3000,4000,3200,2100,000,400],"faculty":[150,170,200,150,100,30,10],"placement":[2000,2000,100,400,100,40,400]}
df=pd.DataFrame(clp)
# print(df)
# print(df["year"])
# print(df["year"].max())
# print(df[["year","placement","students"]])

# plt.plot(df.year,df.placement,label="placement")
# plt.xlabel("Years")
# plt.ylabel("placements")
# plt.grid()
# plt.title("placements records of last 7 years")
# plt.legend()
# plt.show()a

df["stu&fac"]=df["students"]+df["faculty"]
# print(df.iloc[1])

df.loc[6]=[2021,400,40,400,40]
# df.loc[7]=[2022,500,40,500,540]

#del(df["stu&fac"])
# res=df.drop(5)      # it changes the new data frames
df.drop(5,inplace=True)
print(df)

print(df.iloc[3])

df.drop("stu&fac",axis=1,inplace=True)
print(df)