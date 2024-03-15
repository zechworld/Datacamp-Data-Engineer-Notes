# APIs and interacting with the world wide web
In this lecture we will explain what an API is and why are they important, followed by how to connect with them through an URL.

### What is an API? and, What is it importance?
Is a `set of protocols` and `routines` for `building and interacting` with software applications. In other words, its a small software that allows two different applications to communicate with each other. E.g: Twitter API, Uber API, Facebook, you name it. Using an API has now become a standard practice when interacting with applications.

## Connecting to an API with Python
We'll pull data from the `Open Movie DataBase` or OMDB API. Through the `requests` package we will assign the URL of interest, then we will package and send the request to the URL and catch the response in one line of code. From the `requests` package through the response object we have a method called `json` that helps us decode the JSON data into a dictionary.

```python
import requests

url = 'http://www.omdbapi.com/?t=hackers'

r = requests.get(url)

json_data = r.json()

for key, value in json_data.items():
	print(key + ':', value)


```
