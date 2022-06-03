import matplotlib.pyplot as plt

"""year=[2015,2016,2017,2018,2019,2020,2021]
tata=[1500,3400,4100,4700,5000,4300,3200]
maruti=[3000,4200,5200,4800,7000,6200,6000]
mercedeez=[5000,4400,3000,2100,1800,1000,800]
audi=[1000,1800,1200,1800,1700,1200,1500]
plt.plot(year,tata,label="TATA",linewidth=3,linestyle="-",marker="o",markersize="8",markerfacecolor="black")  # intersection of x and y axix is shown by marker
plt.plot(year,maruti,label="Maruti",linewidth=3,linestyle="--",marker="*",markersize="8")
plt.plot(year,mercedeez,label="Mercedeez",linewidth=3,linestyle="-.",marker="d",markersize="8")
plt.plot(year,audi,label="Audi",linewidth=3,linestyle=":",marker="^",markersize="8")

plt.title("Car sale records of last 7 years")
plt.xlabel("Years")
plt.ylabel("Units Sold")
plt.grid(linestyle="--",color="cyan")
plt.legend() # Differentiate both the graphs

plt.show()"""

year=[2015,2016,2017,2018,2019,2020,2021]
# year2=[2004,2001,2002,2003,2004,2005,2006]
data=[[2000,2500,3000,2366,4000,3500,4200],
     [1500,1785,2000,2987,3400,2967,3897],
     [1000,1589,2789,1895,2654,3546,4562]]
plt.plot(year,data[0],label="TATA",linewidth=3,linestyle=":",marker="o",markersize="8",markerfacecolor="red")
plt.plot(year,data[1],label="FORD",linewidth=3,linestyle="-.",marker="^",markersize="8",markerfacecolor="yellow")
plt.plot(year,data[2],label="MARUTI",linewidth=3,linestyle="--",marker="*",markersize="8",markerfacecolor="blue")

plt.title("Car sale records of last 7 years")
plt.xlabel("Years")
plt.ylabel("Units Sold")
plt.grid(linestyle="-.",color="red")
plt.legend()
# plt.text(2017,3000,"data")
for i in data:
    for y, u in zip(year,i):
        plt.text(y,u,f"{u}")

plt.show()

# GLA#sj9eva