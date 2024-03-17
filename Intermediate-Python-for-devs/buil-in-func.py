# Functions we know

# Printing
print("Display this as an output")

# Check for data type
type(print) # builtin_function_or_method

# Looping through a range of numbers - range
for num in range(1, 5):
    print(num)

# Numeric functions
sales = [125.97, 84.32, 99.78, 154.21, 78.50, 83.67, 111.13]

# max
max(sales) # 154.21

# min
min(sales) # 78.5

# sum()
sum(sales) # 737.57999999999999999

# round
tota_sales = sum(sales)
round(total_sales, 2) # 737.58 The number specified is the number of decimals

# Nested functions
total_sales = round(sum(sales), 2)

# Length - Numeric
len(sales) # 7

# Use of length and sum to calculate the mean
sum(sales) / len(sales)

# Length - String
len("Introduction to Programming for Developers") # 42

# Length - Dictionary
len({"a": 1, "b": 2, "c":3}) # 3

# sorted
# Sort the sales list in ascending order
sorted(sales) 

# Sort a string alphabetically
sorted("George") # [ 'G', 'e', 'e', 'g', 'o', 'r']

# Help
help(function) # Get information about the function