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


