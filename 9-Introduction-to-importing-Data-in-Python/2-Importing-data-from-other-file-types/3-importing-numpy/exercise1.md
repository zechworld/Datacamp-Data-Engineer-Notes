# Exercise 1

1. Fill in the arguments of `np.loadtxt()` by passing file and a comma `','` for the delimiter.

2. Fill in the argument of `print()` to print the type of the object `digits`. Use the function `type()`.

```python
# Import package: Here we are importing numpy and Matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Assign the filename to variable file
file = 'digits.csv'

# Filling the arguments: passing the file and use a comma as delimiter
digits = np.loadtxt(file, delimiter=',')

# Printing the type of digits
print(type(digits))

# Plotting the results
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

```
