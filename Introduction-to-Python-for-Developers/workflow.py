# in keyword

# in = check if a value is in a variable / data structure

products_dict = {
    "AG32": 10, "HT91": 20,
    "PL65": 30, "OS31": 15,
    "KB07": 25, "TR48": 35
}

# Check if "OS31" is a key in products_dict
if "OS31" in products_dict.keys():
    print(True)
else:
    print(False)


# Not keyword

# not = check if a condition is not met

# Check if "OS31" is not a key in products_dict
if "OS31" not in products_dict.keys():
    print(False)
else:
    print(True)
