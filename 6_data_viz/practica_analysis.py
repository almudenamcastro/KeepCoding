import pandas as pd

#read the data
df = pd.read_csv("6_data_viz/datasets/airbnb-listings Madrid.csv", sep=";")

# add a column with all the prices added (night price, cleaning fee and security deposit)

# we add up all the prices. 
# In this case, it makes sense to replace null values with 0 
# (if a host is not charging a deposit, for instance, that is equivalent to a free deposit)

# df['Cleaning Fee'] = df['Cleaning Fee'].fillna(0)
# df['Security Deposit'] = df['Security Deposit'].fillna(0)
# df['Total Price'] = df['Price'] + df['Cleaning Fee'].fillna(0) + df['Security Deposit'].fillna(0)
df['Total Price'] = df['Price'] + df['Cleaning Fee'] + df['Security Deposit']


# group df by property type and sort by total price. 
df_means3 = df.groupby('Property Type')['Price', 'Cleaning Fee', 'Security Deposit', 'Total Price'].mean()
df_means3['Total Price 2'] = df_means3['Price'] + df_means3[ 'Cleaning Fee'].fillna(0) + df_means3['Security Deposit'].fillna(0)

df_means3.sort_values('Total Price 2', ascending=False)

# save smaller data set with only the avg data grouped by neighbourhood and property type. 
df_means = df.groupby(['Neighbourhood', 'Property Type'])['Price', 'Cleaning Fee', 'Security Deposit', 'Total Price'].mean()
df_means.reset_index(inplace=True)

# hoy many offers are there. 
df_means['count'] = df.groupby(['Neighbourhood', 'Property Type'])['ID'].count().reset_index()['ID']

# Total Price 2 is the sum of the average prices
df_means['Total Price 2'] = df_means['Price'] + df_means[ 'Cleaning Fee'].fillna(0) + df_means['Security Deposit'].fillna(0)

# print values for aluche sorted by Total Price
df_means[df_means['Neighbourhood']=='Aluche'].sort_values('Total Price', ascending=False)


# if I used Neighbourhood Cleansed instead of Neighbourhood to do the groupings. 
df_means2 = df.groupby(['Neighbourhood Cleansed', 'Property Type'])['Price', 'Cleaning Fee', 'Security Deposit', 'Total Price'].mean()
df_means2.reset_index(inplace=True)
df_means2['Total Price 2'] = df_means2['Price'] + df_means2[ 'Cleaning Fee'] + df_means2['Security Deposit']
df_means2[df_means2['Neighbourhood Cleansed']=='Aluche'].sort_values('Total Price', ascending=False)


# save the avg total price by property type in aluche. 
aluche = df[df['Neighbourhood']=='Aluche'].groupby('Property Type')['Total Price', 'Price'].mean().sort_values('Price', ascending=False)
aluche = aluche.reset_index()

## matplotlib para representar aluche en un barplot
import matplotlib.pyplot as plt

aluche.plot(kind='bar', x='Property Type', y='Total Price', ax=plt.gca())
#aluche.plot(kind='bar', x='Property Type', y='Price', color='red',  ax=plt.gca())
plt.show()

aluche.head()