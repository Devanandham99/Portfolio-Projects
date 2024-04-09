import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

table=pd.read_csv("Marketing.csv")
#Getting the Table
table['name']=table['make']+' '+table['model']+' '+table['trim']
table=table.dropna()
table['state']=table['state'].str.strip()
table['state']=table['state'].replace("ab", "Alabama")
table['state']=table['state'].replace('az', 'Arizona')
table['state']=table['state'].replace('al', 'Alaska ')
table['state']=table['state'].replace('ca', 'California')
table['state']=table['state'].replace('co', 'Colorodo')
table['state']=table['state'].replace('fl', 'Florida')
table['state']=table['state'].replace('ga', 'Georgia')
table['state']=table['state'].replace('hi', 'Hawaii')
table['state']=table['state'].replace('il', 'Illinois')
table['state']=table['state'].replace('in', 'Indiana')
table['state']=table['state'].replace('la', 'Loiusiana')
table['state']=table['state'].replace('ma', 'Massachusetts')
table['state']=table['state'].replace('md', 'Maryland')
table['state']=table['state'].replace('mi', 'Michigan')
table['state']=table['state'].replace('mo', 'Montana')
table['state']=table['state'].replace('mn', 'Minnesota')
table['state']=table['state'].replace('ms', 'Missippi')
table['state']=table['state'].replace('nc', 'North Carolina')
table['state']=table['state'].replace('ne', 'Nebraska')
table['state']=table['state'].replace('nj', 'New Jersey')
table['state']=table['state'].replace('nm', 'New Mexico')
table['state']=table['state'].replace('ma', 'Massachusetts')
table['state']=table['state'].replace('ns', 'New Hampshire')
table['state']=table['state'].replace('nv', 'Nevada')
table['state']=table['state'].replace('ny', 'New York')
table['state']=table['state'].replace('oh', 'Ohio')
table['state']=table['state'].replace('ok', 'Oklahama')
table['state']=table['state'].replace('on', 'North Dakota')
table['state']=table['state'].replace('or', 'Oregon')
table['state']=table['state'].replace('pa', 'Pennsylvania')
table['state']=table['state'].replace('pr', 'Puerto Rico')
table['state']=table['state'].replace('qc', 'South Dakota')
table['state']=table['state'].replace('sc', 'South Carolina')
table['state']=table['state'].replace('tn', 'Tennesse')
table['state']=table['state'].replace('tx', 'Texas')
table['state']=table['state'].replace('ut', 'Utah')
table['state']=table['state'].replace('va', 'Virginia')
table['state']=table['state'].replace('wa', 'Washington')
table['state']=table['state'].replace('wi', 'Wisconsin')
#Data Manipulation
print(table.head())

#Data wrangling and data cleaning for manipulation

brandsales=table['make'].value_counts().reset_index()
brandsales.columns=['Brand', 'Sales Value']
print(brandsales)
#Car sales based on brand

fig=px.pie(brandsales, values=brandsales['Sales Value'], names=brandsales['Brand'], title="Sales brand wise", hole=0)
fig.update_traces(textinfo='none')
fig.show()
#Pie chart for brand based sales

areasales=table['state'].value_counts().reset_index()
areasales.columns=['State', 'Overall Sales']
print(areasales)
fig=px.bar(areasales, x=areasales['State'], y='Overall Sales')
fig.show()
#pie chart for area based sales

table['month']=table['saledate'].str[4:7]
table['year']=table['saledate'].str[11:15]
table['year_month']=table['month']+' '+table['year']
#separating the saledate column into month and year

timesale=table['year_month'].value_counts().reset_index()
timesale.columns=['Month', 'Sales Value']
print(timesale)
plt.figure(figsize=(20,10))
plt.plot(timesale['Month'], timesale['Sales Value'], marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')

# Display the chart
plt.show()