# Defining a custom function
sales = [125.97, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]

# What if modules and packages don't have the functionality needed?

# Example to calculate the mean / average

# Sales variable
sales = [125.97, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]

# Calculating average sales
average_sales = sum(sales) / len(sales)

# Rounding the results
rounded_average_sales = round(average_sales, 2)
print(rounded_average_sales)

# ---- 

# If we need to repeat this code, to help readability of your code
# we can create your own function.

def average(values):
    # Calculate the average
    average_value = sum(values) / len(values)

    # Return the rounded results
    return round(average_value, 2)

# Now we can use this function in our code and pass the result into a variable

sales2 = [125.97, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]

avg_sales2 = average(sales2)


