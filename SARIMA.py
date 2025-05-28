import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/DevanandamRSV/Python/Filelocation/filename.csv")
print(df.head())
df['Date']=pd.to_datetime(df['Date'])

df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month

grouped = df.groupby(pd.Grouper(key='Date', freq='ME'))['Sales'].sum().reset_index()
grouped['Month_Year']=grouped['Date'].dt.strftime('%b %Y')

print(grouped.head())

plt.figure(figsize=(15,15))
plt.plot(grouped['Month_Year'], grouped['Sales'], marker='o', linestyle='-', color='b', label="Sales")

# Customize the plot
plt.title("Sales Trend Over Time (2020-2024)", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Total Sales", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(ticks=range(len(grouped['Month_Year'])), labels=grouped['Month_Year'], rotation=45)
plt.legend(fontsize=12)

plt.show()
