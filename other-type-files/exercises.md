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
