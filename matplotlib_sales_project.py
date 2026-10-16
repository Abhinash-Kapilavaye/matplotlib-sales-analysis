import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
laptop_sales = [50000, 60000, 55000, 80000]
mouse_sales = [10000, 15000, 20000, 25000]

laptop_profit = [8000, 10000, 9000, 15000]
mouse_profit = [2000, 3000, 4000, 5000]


# Chart 1: Monthly sales comparison

plt.figure(figsize=(8,5))
plt.plot(months,laptop_sales,marker="o",color="orange",label="Laptop")
plt.plot(months,mouse_sales,marker="s",color="blue",label="Mouse")

plt.title("Monthly wise Sales")
plt.xlabel("Months")
plt.ylabel("Sales (₹)")
plt.legend()
plt.grid(True)
plt.savefig("outputs/monthly_sales.png")
plt.tight_layout()
plt.show()
plt.close()

# Chart 2: Monthly profit comparison

plt.figure(figsize=(8, 5))

plt.plot(months, laptop_profit, marker="o", label="Laptop")
plt.plot(months, mouse_profit, marker="s", label="Mouse")

plt.title("Monthly Profit by Product")
plt.xlabel("Month")
plt.ylabel("Profit (₹)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("outputs/monthly_profit.png")
plt.show()
plt.close()