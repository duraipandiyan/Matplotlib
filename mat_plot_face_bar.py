import matplotlib.pyplot as plt
month_number=[1,2,3,4,5,6,7,8,9,10,11,12]
month_number1=[1.3,2.3,3.3,4.3,5.3,6.33,7.3,8.3,9.3,10.3,11.3,12.3]

number_unit_sold=[2500,2600,2200,3500,3600,2700,2950,3600,3550,2000,2400,2900]
number_unit_sold1=[1500,1300,1300,1100,1700,1550,1100,1400,1700,1450,2050,1300]
plt.title("Face wash and face Cream  date")
plt.xlabel("Month Number")
plt.ylabel("Number of Unit Number")
plt.bar(month_number,number_unit_sold,label="face  Cream sale date",width=0.3,color="blue")
plt.bar(month_number1,number_unit_sold1,label="face wash sale date",color="orange",width=0.3)
plt.legend(loc="upper left")
plt.grid(True,linewidth=1,linestyle="--")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
#plt.yticks([5300,5050,4500,5800,4500,4800,5800,6200,6200,8500,9500,10000])
plt.show()