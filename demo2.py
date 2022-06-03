"""
import matplotlib.pyplot as plt

year=[2015,2016,2017,2018,2019,2020,2021]
tata=[1500,3400,4100,4700,5000,4300,3200]
maruti=[3000,4200,5200,4800,7000,6200,6000]
mercedeez=[5000,4400,3000,2100,1800,1000,800]
audi=[1000,1800,1200,1800,1700,1200,1500]

def common():
    plt.xlabel("Years")
    plt.ylabel("Units Sold")
    plt.grid(linestyle="--", color="cyan")
    plt.legend()
plt.title("Car sale records of last 7 years")
plt.subplot(1,4,1)
plt.plot(year,tata,label="TATA",linewidth=3,linestyle="-",marker="o",markersize="8",markerfacecolor="black")
common()
plt.subplot(1,4,2)
plt.plot(year,maruti,label="Maruti",linewidth=3,linestyle="--",marker="*",markersize="8")
common()
plt.subplot(1,4,3)
plt.plot(year,mercedeez,label="Mercedeez",linewidth=3,linestyle="-.",marker="d",markersize="8")
common()
plt.subplot(1,4,4)
plt.plot(year,audi,label="Audi",linewidth=3,linestyle=":",marker="^",markersize="8")
common()

plt.show()

"""

import matplotlib.pyplot as plt

year=[2015,2016,2017,2018,2019,2020,2021]
tata=[1500,3400,4100,4700,5000,4300,3200]
maruti=[3000,4200,5200,4800,7000,6200,6000]
mercedeez=[5000,4400,3000,2100,1800,1000,800]
audi=[1000,1800,1200,1800,1700,1200,1500]

def common():
    plt.xlabel("Years")
    plt.ylabel("Units Sold")
    plt.grid(linestyle="--", color="cyan")
    plt.legend()
plt.title("Car sale records of last 7 years")
plt.subplot(2,2,1)
plt.plot(year,tata,label="TATA",linewidth=3,linestyle="-",marker="o",markersize="8",markerfacecolor="black")
common()
plt.subplot(2,2,2)
plt.plot(year,maruti,label="Maruti",linewidth=3,linestyle="--",marker="*",markersize="8")
common()
plt.subplot(2,2,3)
plt.plot(year,mercedeez,label="Mercedeez",linewidth=3,linestyle="-.",marker="d",markersize="8")
common()
plt.subplot(2,2,4)
plt.plot(year,audi,label="Audi",linewidth=3,linestyle=":",marker="^",markersize="8")
common()

plt.show()

import matplotlib.pyplot as plt
import numpy as np
# month=[1,2,3,4,5,6,7,8,9,10,11,12]
# profit=[210000,180000,240000,239000,220000,210000,200000,300000,350000,230000,420000,300000]
# plt.plot(month,profit,label="Profit data per month",linestyle="--",marker="o",color="red",linewidth=3,markerfacecolor="black")
# plt.xlabel("Month")
# plt.ylabel("Sold units number")
# plt.title("Company Profit Per Month")
# plt.legend(loc='lower right')
# plt.show()


# month=[1,2,3,4,5,6,7,8,9,10,11,12]
# creame1=[1500,3400,4100,4700,5000,4300,3200,7895,4562,3698,7896,4589]
# creame2=[3000,4200,5200,4800,7000,6200,6000,4560,7821,3654,1256,6542]
# creame3=[5000,4400,3000,2100,1800,1000,1800,1450,4502,4560,6582,7852]
# creame4=[1000,1800,1200,1800,1700,1200,1500,1850,1950,2000,1900,1950]
# creame5=[9000,7000,6000,6500,4500,10000,7500,8450,7540,6120,7899,6548]
#
# plt.plot(month,creame1,marker="o",label='face cream sales data')
# plt.plot(month,creame2,marker="o",label='face cream sales data')
# plt.plot(month,creame3,marker="o",label='face cream sales data')
# plt.plot(month,creame4,marker="o",label='face cream sales data')
# plt.plot(month,creame5,marker="o",label='face cream sales data')
#
# plt.xlabel("Month")
# plt.ylabel("Sales Unit in number")
# plt.title("Sales Data")
# plt.legend(loc='upper left')
# plt.show()


# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# toothpaste=[5350,5250,4550,5900,4530,4900,4800,5800,6100,8400,7300,7400]
#
# plt.plot(month,toothpaste,marker="o",label='Tooth Paste sales data',linestyle=" ")
#
# plt.xlabel("Month")
# plt.ylabel("Sales Unit in number")
# plt.title("Tooth Paste Sales Data")
# plt.grid(linestyle=':',)
# plt.legend(loc='upper left')
# plt.show()

# month = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# facecream=[2500,2650,2100,3400,3700,2800,2950,3800,3600,2000,2400,2900]
# facewash=np.array([1500,1200,1300,1100,1750,1550,1100,1400,1800,1900,2100,1800])
#
# plt.bar(month,facecream,label='face cream sales data',width=.1)
# plt.bar(month+.1,facewash,label='face wash sales data',width=.1)
#
# plt.xlabel("Month")
# plt.ylabel("Sales Unit in number")
# plt.title("Facewash and Facecreame Sales Data")
# plt.grid(linestyle='--')
# plt.legend(loc='upper left')
# plt.show()


# month = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# bathingsoap = [9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]
# plt.bar(month,bathingsoap)
# plt.xlabel("Month")
# plt.ylabel("Sales Unit in number")
# plt.title("Bathingsoap Sales Data")
# plt.grid(linestyle='--')
# plt.show()


total_units=np.array([21100,18330,22470,22270,20960,20140,29550,36140,23400,26670,41280,30020])
things=np.array(['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer'])

plt.pie(total_units, labels=things, autopct="%.2f%%")
plt.legend()
plt.show()