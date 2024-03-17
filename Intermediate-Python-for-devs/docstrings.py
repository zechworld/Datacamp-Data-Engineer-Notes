# Docstrings 

# String that explain what a specific function does

# Can be access by help() function
# Can be access with: func.__doc__ (two sets of __ is refer to dunder)

# Are build with """ """ (Triple quotation marks). Can be one line or multiline

# Adding docstrings to our function
def average(values):
    """
    Find the mean in a sequence of values and round to two decimal places.

    Args:
        values (list): A list of numeric values.

    Returns:
        rounded_average (float): The mean of values, rounded to two decimal places.
    """

    """ One line docstring"""
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

