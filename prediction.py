import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data
df = pd.read_csv('Forest_Area.csv')

# Select a country (e.g., Albania)
country = 'Albania'
country_data = df[df['Country and Area'] == country]

# Prepare the data
years = [1990, 2000, 2010, 2020]
forest_areas = country_data[['Forest Area, 1990', 'Forest Area, 2000', 'Forest Area, 2010', 'Forest Area, 2020']].values.flatten()

# Visualize the data
plt.figure(figsize=(12, 7))
plt.scatter(years, forest_areas, color='blue', label='Actual data')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Forest Area (sq km)')
plt.title(f'Forest Area in {country} Over Time')

# Add text annotations for actual data
for i, txt in enumerate(forest_areas):
    plt.annotate(f'{txt:.2f}', (years[i], forest_areas[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Show the plot with actual data
plt.legend()
plt.grid(True)

# Pause to explain the scatter plot
plt.show()

# Now, let's add the linear regression
X = np.array(years).reshape(-1, 1)
y = forest_areas

model = LinearRegression()
model.fit(X, y)

# Make a prediction for 2030
prediction_2030 = model.predict([[2030]])

# Visualize the data, regression line, and prediction
plt.figure(figsize=(12, 7))
plt.scatter(years, forest_areas, color='blue', label='Actual data')
plt.plot(years, model.predict(X), color='red', label='Linear regression')
plt.scatter([2030], prediction_2030, color='green', label='2030 prediction')

plt.title(f'Forest Area Prediction for {country}')
plt.xlabel('Year')
plt.ylabel('Forest Area (sq km)')
plt.legend()

# Add text annotations
for i, txt in enumerate(forest_areas):
    plt.annotate(f'{txt:.2f}', (years[i], forest_areas[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(f'{prediction_2030[0]:.2f}', (2030, prediction_2030), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.show()

print(f"Predicted forest area for {country} in 2030: {prediction_2030[0]:.2f} sq km")
print(f"Slope (change per year): {model.coef_[0]:.2f} sq km/year")
print(f"Intercept: {model.intercept_:.2f} sq km")