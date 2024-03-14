# Importing MATLAB files

MATLAB is short for `Matrix Laboratory`. Is a numerical computing environment standard used for engineering and science. This software saves files with the extension `.mat`. So, How can we import this files?

We need to use the `ScyPy` library. This package has in-built functions to work with `.mat` files:

- `scipy.loadmat()`: Read `.mat` files 
- `savemat()`: Write `.mat` files

The MATLAB files deal with loads of variables, its workspace contain strings, floats, vectors, arrays, among many other objects. Hence, we should expect different groupings of these datatypes.Lets do a quick import of a MATLAB file and inspect what type of object we have in return:

```python
#Importing the package
import scipy.io

# Loading the file's path
filename = 'workspace.mat'

# Importing .mat file 
mat = scipy.io.loadmat(filename)

# Inpect the type of mat
print(type(mat))

# <class 'dict'>
```

We see that the `.mat` file gets converted into a dictionary in Python. The way MATLAB relates to a Python dictionary is really easy to grasp:

- Keys = MATLAB variable names
- Values = Objects assigned to that variable

Lets suppose that our previous example, the variable mat that contains the data imported from MATLAB has a variable `x`. Lets explore the type of that variable:

```python
print(type(mat['x']))
# <class 'numpy.ndarray'>
```
We get back a NumPy array, which means that a `MATLAB array x` corresponds to a `MATLAB array`.

