import matplotlib.pyplot as plt
munth_number=[1,2,3,4,5,6,7,8,9,10,11,12]
number_unit_sold=[5200,5100,4500,5900,4550,4850,4750,5900,6100,8500,7300,7400]
plt.title("Tooth past sales date")
plt.xlabel("Munth Number")
plt.ylabel("Number of Unit Sold")
plt.scatter(munth_number,number_unit_sold,label="Tooth past sale date")
plt.legend(loc="upper left")
plt.grid(True,linewidth=1,linestyle="--")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
#plt.yticks([5300,5050,4500,5800,4500,4800,5800,6200,6200,8500,9500,10000])
plt.show()