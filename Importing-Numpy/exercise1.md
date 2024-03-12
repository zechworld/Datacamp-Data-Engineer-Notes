# Exercise 1

1. Fill in the arguments of `np.loadtxt()` by passing file and a comma `','` for the delimiter.

2. Fill in the argument of `print()` to print the type of the object `digits`. Use the function `type()`.

```python
# Import package
import numpy as np
import matplotlib.pyplot as plt

file = 'digits.csv'

# 1.
digits = np.loadtxt(file, delimiter=',')
# 2.
print(type(digits))

im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

```
