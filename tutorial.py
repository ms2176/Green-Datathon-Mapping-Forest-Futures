# Basic Data Manipulation Tutorial using Python and Pandas

# 1. Loading the data
import pandas as pd
df = pd.read_csv('Forest_Area.csv')

# 2. Exploring the dataset
print(df.head())
print(df.info())

# 3. Basic filtering
# Example: Countries with forest area > 1,000,000 ha in 2020
large_forest_countries = df[df['2020'] > 1000000]

# 4. Grouping and aggregation
# Example: Average forest area by continent in 2020
avg_forest_by_continent = df.groupby('Continent')['2020'].mean()

# 5. Simple visualization
import matplotlib.pyplot as plt

# Example: Bar plot of top 10 countries by forest area in 2020
top_10 = df.nlargest(10, '2020')
plt.figure(figsize=(12,6))
plt.bar(top_10['Country'], top_10['2020'])
plt.title('Top 10 Countries by Forest Area in 2020')
plt.xlabel('Country')
plt.ylabel('Forest Area (1000 ha)')
plt.xticks(rotation=45)
plt.show()