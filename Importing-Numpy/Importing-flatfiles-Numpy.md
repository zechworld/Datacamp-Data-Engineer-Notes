# Importing Flat files using NumPy

## Why NumPy?
The arrays that this package has built-in are the standard when you want to deal with storing numerical data. This package gives us a very efficient, fast and clean way to manipulate numeric data. 

### Importing
We will be using the functions `loadtxt` and `genfromtxt`. First we need to import NumPy as np *(good practice)*. Then we can load the file name into a variable and use the function `np.loadtxt` along with its two arguments: *filename* and *delimiter (The default delimiter is white spaces, so if we want to use a different delimiter we have to use this argument explicitly)* 

```python
import numpy as np
filename = 'MNIST.txt'
data = np.loadtxt(filename, delimiter=',')
data

```
Most of the time the files that we need to import will have different datatypes in different columns. We could have `str`, `int` or `floats`. The function we were using `np.loadtxt` won't work properly, but we can use another function called `np.genfromtext()` which can handle multiple structures. 

This function will create a `structure array` for the different types. Numpy have to contain elements that have the same type, and structured arrays allow to generate a 1D array that contains multiple format inside.

Also, there's the function `np.recfromcsv()` that has its `dtype` as None by default. 

```python
# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv()

# Print out the first three entries of da
print(d[:3])

```
