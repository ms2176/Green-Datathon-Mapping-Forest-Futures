# Loading data
import pandas as pd

df = pd.read_csv('file.csv')

# Viewing data
df.head()  # First few rows
df.info()  # Dataset info
df.describe()  # Statistical summary

# Filtering
df[df['column'] > value] # type: ignore
df.query('column > value')

# Grouping and aggregation
df.groupby('column').mean()
df.groupby('column').agg({'col1': 'mean', 'col2': 'sum'})

# Sorting
df.sort_values('column', ascending=False)

# Basic plotting
df.plot(kind='bar')
df.plot(kind='scatter', x='column1', y='column2')

# Handling missing values
df.dropna()
df.fillna(value) # type: ignore

# Adding/modifying columns
df['new_column'] = df['column1'] + df['column2']