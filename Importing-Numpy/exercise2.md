# Exercise 2
Using `np.loadtxt()` arguments to succesfully import a csv file. The arguments to use are:

1. delimiter: Changes the default delimiter (white space). We can use ',' for comma-delimited, and '\t' for tab-delimited.

2. skiprows: Specify how many rows you want to be skipped. Bare in mind this doesn't mean indices, so it **doesn't start with index 0**.

3. usecols: Takes a list of indices of the columns wish to be kept.

### Instructions
Complete the arguments of np.loadtxt(): the file you're importing is tab-delimited, you want to skip the first row and you only want to import the first and third columns.

```python
# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=0, usecols=[0,2])

# Print data
print(data)

```

### Correction
The issue here is that you set `skiprows=0`, which means you are not skipping any rows. However, the first row in your data file contains column labels like 'label', which cannot be converted to a float. This is causing the error.

```python
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])
```

 
