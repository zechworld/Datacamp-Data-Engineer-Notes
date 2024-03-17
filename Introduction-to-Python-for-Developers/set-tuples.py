# Sets
# Contain unique data
# Unchangeable
# Ideal to identify and remove duplicates
# Quick to search

# Set = {}
# {} + : = Dictionary

# Create an attendee set
attendees_set = {"John Smith", "Alan Jones", "Roger Thompson", "John Smith", "Brandon Sharp", "Sam Washington"}

print(attendee_set) # {'Alan Jones', 'Brandon Sharp', 'John Smith', 'Roger Thompson', 'Sam Washington'} Altho there were two registries for John Smith, only one was shown

attendees_list = ["John Smith", "Alan Jones", "Roger Thompson", "John Smith", "Brandon Sharp", "Sam Washington"]

# Convert to a set
attendees_set = set(attendees_list) # casting the data type

# Sorting a set
sorted(attendees_set) # Returns a list sorted alphabetically

# Sets don't have indexes
# Sets are unordered


#----------------------------------
# Tuple
#
# Immutable - Cannot be changed
# No adding values
# No Removing values
# No changing values
# Ordered
# Subset with index

# Create a tuple
office_locations = ("New York", "London", "Leuven")

# Convert another data structure to a tuple
attendees = tuple(attendees_list)

# Access the second element
office_locations[1] # London

# List - [1, 2, 3] - Mutable - Allow Duplicates - Ordered - index subset
# Dict - {key:value} - Mutable - Allow Duplicates - Ordered - key subset
# Set - {1, 2, 3} - Mutable - No Duplicates - Unordered - No subset
# Tuple - (1, 2, 3) - Inmutable - Allow Duplicates - Ordered - index subset


