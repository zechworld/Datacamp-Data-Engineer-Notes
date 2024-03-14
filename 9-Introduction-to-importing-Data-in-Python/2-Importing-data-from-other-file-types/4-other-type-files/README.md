# Other file types
We also can import files from other types of extensions such as spreadsheets from Excel, or files from MATLAB, SAS and Stata. Also, HDF5 files which is a prevalent form for storing large datasets. Finally, we can include the so called `pickled files`.

The latter is a file native to Python. As we go deeper into importing data into Python, we will encounter some issues when we want to save datatypes into flat files (like the case of dictionaries and list). The answer to this is to `Pickle` them, or serialize them into a sequence of btyes, or bytestreams.

This course is about importing files, so, we won't be transforming files into pickled files, but we will importing already pickled files. To do this we'll use the `with` Context and specify it's `read-only` and `binary`:

```python
import pickle
with open('pickled_fruit.pkl', 'rb') as file:
	data = pickle.load(file)
print(data)
```

Also, we can import excel spreadsheets using pandas because it generates a dataframe natively. For this we need to use the function `pd.ExcelFile` so we can assign an Excel file to a variable data. First, we need to know how many sheets does the file has (normally the Excel spreadsheets have a number of sheets), and then with this we can load the data into a dataframe using the function `data.parse()` that will accept one argument to refer to a sheet, this can be achieved in two ways:

1. By sheet name, as a string
2. By sheet index, as a float

### E.g:

```python
import pandas as pd

file = 'urbanpop.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)

"""
Sheets parsed into data variable

['1960-1966', '1967-1974', '1975-2011']
"""

#If we want to select a particular sheet we use
df1 = data.parse('1960-1966')
df2 = data.parse(0)

```

