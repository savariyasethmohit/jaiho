import matplotlib.pyplot as plt
import numpy as np

year=np.array([2015,2016,2017,2018,2019,2020,2021])
tata=np.array([1500,3400,4100,4700,5000,4300,3200])
lst=[0.5,0,0,0,0,0,0]
plt.pie(tata,labels=year,autopct="%.2f%%",explode=lst,shadow=True)
plt.show()

