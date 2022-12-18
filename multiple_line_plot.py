import matplotlib.pyplot as plt
Month_num=[1,2,3,4,5,6,7,8,9,10,11,12]
Sales_unit_number_date=[2100,2120,2000,3000,3100,2200,2300,3000,2800,2000,1500,2100]
Sales_unit_number_date1=[5000,4900,4700,6000,4300,4400,4390,5000,5100,7500,6500,6500]
Sales_unit_number_date2=[8900,5900,8950,8500,8000,7900,8590,9000,6500,9000,12000,13500]
Sales_unit_number_date3=[1000,2000,3950,2000,1500,1550,1500,2800,1900,2040,2060,1500]
Sales_unit_number_date4=[1300,1000,1800,1700,1510,1450,1350,1500,1950,2100,2150,1500]
plt.xlabel("Month_number")
plt.ylabel("sale_unit_number_date")
plt.title("sale date")
plt.plot(Month_num,Sales_unit_number_date,label="face cream sale date",color="#0000A5",marker="o",linewidth=3)
plt.plot(Month_num,Sales_unit_number_date1,label="face wash sale date",color="green",linewidth=3,marker="o")
plt.plot(Month_num,Sales_unit_number_date2,label="Tooth past sale date",color="red",marker="o",linewidth=3)
plt.plot(Month_num,Sales_unit_number_date3,label="Tooth past sale date",color="#6A0DAD",marker="o",linewidth=3)
plt.plot(Month_num,Sales_unit_number_date4,label="Tooth past sale date",color="#835C3B",marker="o",linewidth=3)
plt.legend(loc="upper left")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])

plt.show()