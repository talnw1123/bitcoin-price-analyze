from tkinter import *
from tkinter.ttk import *
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BitCoin.csv") 
df.fillna(0 , inplace=True)
df = df.sort_values(by = "Date", ignore_index=True)
df["Date"] = pd.to_datetime(df["Date"])

price = []
total = []
year = [] 
sum = 0

for i in df.index:
    if df["Date"].loc[i].year not in price :
        year.append(df["Date"][i].year)

year = list(dict.fromkeys(year))
year.sort()
print(year)

for k in range(len(year)):
    sum = 0 
    for l in df.index:
        if df["Date"].loc[l].year == year[k]:
            sum = sum + df["btc_market_price"][l]
            total.append(sum)
    price.append(min(total))
    total.clear()      
print(price)

plt.figure(facecolor="gray")
plt.title("Bitcoin Price")
x = year
y = price
plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()