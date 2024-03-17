# While Loops

# The flow of a while loop is similar to an If statement, only that it will run until the condition is false.

# Useful for continuous tasks

# Syntax
while condition:
    action


# Example

# Stock limit
stock = 10

# Number of purchases
num_purchases = 0

# While num_purchases < stock limit
while num_purchases < stock:
    # Increment num_purchases
    num_purchases += 1
    # Print remaining stock
    print(stock - num_purchases)

# Output: 9 8 7 6 5 4 3 2 1 0 Loop exited

# Take in consideration that a condition must be present inside the While loop, otherwise the loop will continue executing and using resources from  the system.

# To break a While loop on code, you can use the break keyword. If the code is already running then the process should be terminated using command+c or ctrl+c

