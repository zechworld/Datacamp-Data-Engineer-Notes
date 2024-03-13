# Exercise 1

In this exercise, you'll import the pickle package, open a previously pickled data structure from a file and load it.

```python
# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
	d = pickle.load(file)

# Print d
print(d)  # { 'June': '69.4', 'Aug': '85', 'Airline': '8', 'Mar': '84.4'}

# Print datatype of d
print(type(d)) # <class 'dict'>

```

# Exercise 2

You'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace Research Institute Oslo's (PRIO) dataset. This data contains age-adjusted mortality rates due to war in various countries over several years.

```python
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

# ['2002', '2004']
```

# Exercise 3
In this exercise, you'll learn how to import any given sheet of your loaded .xlsx file as a DataFrame. You'll be able to do so by specifying either the sheet's name or its index.

```python
# Loading spreadsheet into xls
xls = pd.ExcelFile('battledeath.xlsx')

# Load a sheet inot a Dataframe by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet inot a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())
```

# Exercise 4
Here you'll parse your spreadsheet and use additional arguments to skip rows, rename columns and select only prticular columns.

```python
# Parse the first sheet by index, skip the first row of data and name the columns 'Country' and 'AAM due to War (2002)' using the argument names
df1 = xls.parse(0, skiprows=[0], names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the second sheet by index. Parse only the first column with usecols, skip the the first row and rename the column 'Country'
df2 = xls.parse('2004', usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

```
