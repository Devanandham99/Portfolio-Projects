import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import plotly.express as px

table=pd.read_csv("SocialMediaData.csv", encoding="latin1")
#File read successful

table.isnull().sum
table=table.dropna()
print(table.head())
#Checking for null values and dropping null values

impressions=table["Impressions"].sum()
home = table["From Home"].sum()
hashtags = table["From Hashtags"].sum()
Search = table["From Search"].sum()
other = table["From Other"].sum()

labels = ['From Home','From Hashtags','From Search','Other']
values = [home, hashtags, Search, other]
product_i=table.groupby('Product')['Impressions'].sum().reset_index()
print(product_i)
fig=px.pie(product_i, values='Impressions', names='Product', title='Product performance in social media', hole=0)
fig.show()  
#pie Chart to visualize overall performance of products online

fig = px.pie(table, values=values, names=labels, title='Impressions on Instagram Posts From Various Sources', hole=0)
fig.show()
#Pie Chart to visualize overall performance from various aspects of social media

fig = px.scatter(table, x="Impressions", y="Likes", size="Likes", trendline="ols", title = "Relationship Between Likes and Impressions")
fig.show()
#Analyzing relationship between likes and impressions

fig = px.scatter(data_frame = table, x="Impressions", y="Shares", size="Shares", trendline="ols", title = "Shares vs impressions")
fig.show()
#Analyzing relationship between Shares and impressions

fig = px.scatter(data_frame = table, x="Profile Visits", y="Follows", size="Follows", trendline="ols", title = "Profile Views vs Follower Gains")
fig.show()
#Relationship between profile visits and followers improvement

plt.title("Distribution of Impressions From Home")
sea.histplot(table["From Home"], kde=True)
plt.xlabel("Home Page")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
sea.histplot(table['From Hashtags'], kde=True)
plt.show()
#Plotting graph to check if our posts appear through the various hashtags

plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Search")
sea.histplot(table['From Search'], kde=True)
plt.show()
#plotting graph to check if our posts appear in the Search page
