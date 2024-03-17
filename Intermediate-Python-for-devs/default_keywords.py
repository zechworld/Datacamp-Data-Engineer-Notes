# Arguments are values or data structure provided to the function to 
# Work properly

# Positional arguments -> Provide arguments in order, separating them by commas. 

# keyword arguments -> require the user to define that argument's value
# using the keyword provided.

# The values of this arguments can be None, if
# None is used, it means that that argument can be empty.

# Round function accepts two arguments, number and ndigits (None). We dont need

# to specify those values if we maintain the position they have in the 
# function.

round(number=3.141592, ndigits=2)

# Same

round(3.141592, 2)


# Let's remember the function for average we created
def average(values):
    # Calculate the average
    average_value = sum(values) / len(values)

    # Return the rounded results
    return round(average_value, 2)

# We'll adapt this function to have arguments with standard values.
# If we defined a certain type during definition, it will have that value
# as default. In the average case, we'll make the rounded argument to be
# default to False

def average_modified(values, rounded=False)
    # Round average to two decimal places if rounded is True
    if rounded == True:
        average_value = sum(values) / len(values)
        rounded_average = round(average_value, 2)
        return rounded_average

    # Otherwise, don't round
    else:
        average_value = sum(values) / len(values)
        return average_value


