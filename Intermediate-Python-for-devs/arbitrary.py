# Arbitrary arguments

# The way we've constructed our function means that it only accept a data structure like list, set. If we try to provide another type of data structure we'll get an error.

# Docstrings help clarify "How to use a function", arbitrary arguments helps us fix this problem, accepting any number of arguments

# The conventional naming for arbitrary arguments is *args. 

# Syntax:
def average(*args):

# Using a * means that Python combines all the arguments into a single iterable (tuple)

# We can pass also multiple arguments without the need of combine them into a single variable using *

average(*[15, 29], *[4, 13], *[11, 8]) # 13.33

# We also use arbitrary keyword arguments using the syntax: **kwargs
def average(**kwargs):
    average_value = sum(kwargs.values()) / len(kwargs.values())
    rounded_average = round(average_value, 2)
    return rounded_average

# If we now pass keyword arguments
average(a=15, b=29, c=4, d=13, e=11, f=8) # 13.33

average(**{"a": 15, "b": 29, "c":4, "d":13, "e":11, "f":8}) # 13.33

# Calling average with three kwargs
average(**{"a": 15, "b": 29}, **{"c":4, "d":13}, **{"e":11, "f":8}) # 13.33


# Using arbitrary positional arguments
def average_positional(*args):
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

# Use arbitrary keyword arguments
def average_arbitrary(**kwargs):
    average_value = sum(kwargs.values()) / len(kwargs.values())
    rounded_average = round(average_value, 2)
    return rounded_average

