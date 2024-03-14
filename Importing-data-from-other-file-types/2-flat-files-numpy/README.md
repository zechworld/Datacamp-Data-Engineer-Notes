# Using pandas to import flat files as DataFrames

Using DataFrames is a much more accurate way to import data structures from a flat file. For that we can use `read_csv()` and `read_table()` functions:

### E.g:

```python
# Import pandas as pd
import panda as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

```

We can also transform this `DataFrame` into NumPy arrays very easily like this example:

```python
# Assign the filename: file
file = 'digits.csv'

# Read the first 5 rows of the file into a Dataframe: data
data = pd.read_csv(file, header=None, nrows=5)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

```

Pandas is also great dealing with issues when we import data like missing values and empty lines. In this case we'll use the function `pd.read_csv()` with the arguments 
- `sep: Sets a delimiter`
- `comment: Takes the character that comments occur after like #`
- `na_values: Takes a list of strings to recognize as NaN`

###E.g:

```python
# Assign filename: file
file = 'titanic_corrupt.csv'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())
```


