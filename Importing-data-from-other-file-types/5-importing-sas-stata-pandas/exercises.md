# Exercise 1
In this exercise, you'll learn how to import any given sheet of your loaded .xlsx file as a DataFrame. You'll be able to do so by specifying either the sheet's name or its index. 

```python
import pandas as pd
import matplotlib.pyplot as plt
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
w'ith SAS7BDAT('sales.sas7bdat') as file:
	df_sas = files.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of data

```

# Exercise 2
Here, you'll gain expertise in importing Stata files as DataFrames using the pd.read_stata() function from pandas. The last exercise's file, 'disarea.dta', is still in your working directory.

```python
# Import Pandas
import pandas as pd

# Lload Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

```


