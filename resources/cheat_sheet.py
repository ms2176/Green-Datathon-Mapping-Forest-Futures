# Loading data
import pandas as pd

df = pd.read_csv('file.csv')

# Viewing data
df.head()  # First few rows
df.describe()  # Statistical summary

# Filtering
df[df['column'] > value]  # Filter rows where 'column' is greater than a value

# Grouping and aggregation
df.groupby('column').mean()  # Group by 'column' and calculate mean

# Sorting
df.sort_values('column', ascending=False)  # Sort by 'column' in descending order

# Basic plotting (requires matplotlib)
df.plot(kind='bar')  # Bar plot
df.plot(kind='scatter', x='column1', y='column2')  # Scatter plot

# Handling missing values
df.dropna()  # Drop rows with any missing values
df.fillna(value)  # Replace missing values with a specific value

# Adding/modifying columns
df['new_column'] = df['column1'] + df['column2']  # Add a new column as a sum of two others

# Reading and Writing to Different Formats
df.to_excel('filename.xlsx', index=False)  # Write to Excel
df = pd.read_excel('filename.xlsx')  # Read from Excel

# Selecting Columns and Rows
df.loc[:, 'column1':'column3']  # Select columns by name range
df.iloc[0:5]  # Select first 5 rows

# Renaming Columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)  # Rename a column