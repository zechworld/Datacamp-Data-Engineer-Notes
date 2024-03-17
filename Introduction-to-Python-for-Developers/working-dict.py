# Dictionaries - Ordered
# Key value pairs
products_dict = {
    "AG32": 10,
    "HT91": 20,
    "PL65": 30,
    "OS31": 15,
    "KB07": 25,
    "TR48": 35
}

# Accesing value
products_dict["AG32"] # 10

# Accesing all values
products_dict.values() # dict_values([10, 20, 30, 15, 25, 35])

# Accesing all keys
products_dict.keys() # dict_keys(['AG32', 'HT91', 'PL65', 'OS31', 'KB07', 'TR48'])

# Print the dictionary
print(products_dict)
# {'AG32': 10, 'HT91':20, 'PL65':30, 'OS31':15, 'KB07':25, 'TR48':35}

# Get all items (key-value pairs)
products_dict.items()
# dict_items([('AG32', 10), ('HT91', 20), ('PL65', 30), ('OS31', 15), ('KB07', 25), ('TR48', 35)])


# Adding a key-value pair
products_dict["UI56"] = 40

# Updating a value
products_dict["HT91"] = 12
