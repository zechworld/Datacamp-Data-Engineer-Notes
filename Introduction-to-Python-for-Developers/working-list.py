# Variables of product prices
price_one = 10
price_two = 20
price_three = 30
price_four = 15
price_five = 25
price_six = 35

# List = store multiple values in a single variable
# Can store multiple data types

prices = [10, 20, 30, 15, 25, 35]

prices = [price_one, price_two, price_three, price_four, price_five, price_six]

# Check data  type
string_type = "string"
int_type = 10
list_type = [1,2,3]

type(string_type) # <class string>
type(int_type) # <class int>
type(list_type) # <class 'list'>

# Finding elements in a list
# List are ordered and 0 index
practice_list = ["tree", "pear", "apple", "apricot"] #tree 0  pear 1 apple 2 apricot 3
practice_list[2] = "apple"
practice_list[0] = "tree"

#Findin last element
# Count all items and substract 1: the list has 4 elements
practice_list[3] = "apricot"

# Python shortcut, counting with negative index (This don't start with 0)
practice_list[-1] = "apricot"
practice_list[-2] = "apple"

# List slicing
# [starting_element : last_element + 1] - the first element is inclusive, last_element is not
practice_list = ["tree", "pear", "apple", "apricot", "grape", "melon"]
practice_list[1:3] = ["pear", "apple"]
practice_list[2:6] = ["apple", "apricot", "grape", "melon"]


# Accessing multiple elements
group_slicing = [1, 2, 3, 4, 5, 6]

# Access all elements from the third element
group_slicing[2:] # [3, 4, 5, 6]

# Get the first four elements
group_slicing[:4] # [1, 2, 3, 4]

# Alternating access
prices = [10, 20, 30, 15, 25, 35]
prices[::2]
# The number specified is the interval
# Grabs every second element - First, third, fifth
# [10, 30, 25]

prices [1::3]
# Starts from the second element and gets every third value
# [20, 25]



