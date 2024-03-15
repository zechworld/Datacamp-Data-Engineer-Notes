# Introduction to APIs and JSONs
Now we will focus in learning how to interact with `APIs (Application Programming Interface)`. APIs are a set of protocols and routines for building and interacting with sofware applications. In the next exercises we will be working with the OMDb API and Twitter API.

The standard form for transferring data through APIs is through `JSON file format`. JSON is an acronym for `JavaScript Object Notation` and it's a form of gathering data for `real-time server-to-browser` communication. This files are Human readable, they work with `name-value pairs` separated by commas which remind us to the `dictionary key-value pairs`. 

Lets load a JSON file into our Python environment. For this we'll use the package `json`, then we'll make a context manager to load the contents of the JSON file.

```python
import json

with open('snake.json', 'r') as json_file:
	json_data = json.load(json_file)

print(type(json_data))
	# <Class dict>
```
We can also print the key value pairs of the dictionary:

```python
for key, value in json_data.items():
	print(key + ':', value)
```

