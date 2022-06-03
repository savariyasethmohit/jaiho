import matplotlib.pyplot as plt
import numpy as np
"""
year=[2015,2016,2017,2018,2019,2020,2021]
tata=[1500,3400,4100,4700,5000,4300,3200]
maruti=[3000,4200,5200,4800,7000,6200,6000]
mercedeez=[5000,4400,3000,2100,1800,1000,800]
audi=[1000,1800,1200,1800,1700,1200,1500]

plt.bar(year,tata,label="TATA",color="yellow",edgecolor="red",linewidth="3")
plt.bar(year,maruti,label="MARUTI",color="blue",edgecolor="yellow",linewidth="2",alpha=.5,width=.6)

plt.xlabel("Years")
plt.ylabel("Units Sold")
plt.grid(linestyle="--", color="cyan")
plt.legend()

plt.show()"""

"""import matplotlib.pyplot as plt
import numpy as np

year=np.array([2015,2016,2017,2018,2019,2020,2021])
tata=[1500,3400,4100,4700,5000,4300,3200]
maruti=[3000,4200,5200,4800,7000,6200,6000]
mercedeez=[5000,4400,3000,2100,1800,1000,800]
audi=[1000,1800,1200,1800,1700,1200,1500]

plt.bar(year,tata,label="TATA",color="yellow",edgecolor="red",linewidth="3",width=.1)
plt.bar(year+.1,maruti,label="MARUTI",color="blue",edgecolor="yellow",linewidth="2",alpha=.5,width=.1)
plt.bar(year+.2,mercedeez,label="MERCEDEEZ",color="green",edgecolor="orange",linewidth="2",alpha=.5,width=.1)
plt.bar(year+.3,audi,label="AUDI",color="red",edgecolor="blue",linewidth="2",alpha=.5,width=.1)
plt.xlabel("Years")
plt.ylabel("Units Sold")
plt.grid(linestyle="--", color="cyan")
plt.legend()

plt.show()

year=np.array([2015,2016,2017,2018,2019,2020,2021])
tata=np.array([1500,3400,4100,4700,5000,4300,3200])
maruti=np.array([3000,4200,5200,4800,7000,6200,6000])
mercedeez=np.array([5000,4400,3000,2100,1800,1000,800])
audi=np.array([1000,1800,1200,1800,1700,1200,1500])

plt.bar(year,tata,label="TATA",color="yellow",edgecolor="red",linewidth="3",width=.5)
plt.bar(year,maruti,label="MARUTI",color="blue",edgecolor="yellow",linewidth="2",alpha=.5,width=.5,bottom=tata)
plt.bar(year,mercedeez,label="MERCEDEEZ",color="green",edgecolor="orange",linewidth="2",alpha=.5,width=.5,bottom=tata+maruti)
plt.bar(year,audi,label="AUDI",color="red",edgecolor="blue",linewidth="2",alpha=.5,width=.5,bottom=tata+maruti+mercedeez)
plt.xlabel("Years")
plt.ylabel("Units Sold")
plt.grid(linestyle="--", color="cyan")
plt.legend()

plt.show()

year=np.array([2015,2016,2017,2018,2019,2020,2021])
tata=np.array([1500,3400,4100,4700,5000,4300,3200])
maruti=np.array([3000,4200,5200,4800,7000,6200,6000])
mercedeez=np.array([5000,4400,3000,2100,1800,1000,800])
audi=np.array([1000,1800,1200,1800,1700,1200,1500])

plt.subplot(2,1,1)
plt.barh(year,tata,label="TATA",color="yellow",edgecolor="red",linewidth="3",height=.5)
plt.barh(year,maruti,label="MARUTI",color="blue",edgecolor="yellow",linewidth="2",alpha=.5,height=.5,left=tata)
plt.barh(year,mercedeez,label="MERCEDEEZ",color="green",edgecolor="orange",linewidth="2",alpha=.5,height=.5,left=tata+maruti)
plt.barh(year,audi,label="AUDI",color="red",edgecolor="blue",linewidth="2",alpha=.5,height=.5,left=tata+maruti+mercedeez)
plt.xlabel("Years")
plt.ylabel("Units Sold")
plt.grid(linestyle="--", color="cyan")
plt.legend()

plt.subplot(2,1,2)
plt.bar(year,tata,label="TATA",color="yellow",edgecolor="red",linewidth="3",width=.1)
plt.bar(year+.1,maruti,label="MARUTI",color="blue",edgecolor="yellow",linewidth="2",alpha=.5,width=.1)
plt.bar(year+.2,mercedeez,label="MERCEDEEZ",color="green",edgecolor="orange",linewidth="2",alpha=.5,width=.1)
plt.bar(year+.3,audi,label="AUDI",color="red",edgecolor="blue",linewidth="2",alpha=.5,width=.1
        )
plt.xlabel("Years")
plt.ylabel("Units Sold")
plt.grid(linestyle="--", color="cyan")
plt.legend()

plt.show()

"""

"""

import matplotlib.pyplot as plt
#ds
month_number=[1,2,3,4,5,6,7,8,9,10,11,12]
facecream=[2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
toothpaste=[5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
bathingsoap=[9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]
shampoo=[1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]
moisturizer=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
total_units=[21100,18330,22470,22270,20960,20140,29550,36140,23400,26670,41280,30020]
total_profit=[211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]

"""



