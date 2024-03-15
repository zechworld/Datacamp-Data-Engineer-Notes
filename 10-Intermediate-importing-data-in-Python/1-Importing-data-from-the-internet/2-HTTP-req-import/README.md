# HTTP request to import files from the web

## URL
Lets grasp some basic knowledge of the internet. We used the URL when we used the function `urlretrieve`, but, What is a URL? URL stands for `Universal Resource Locator` and all it does is to be a reference point to a web resource. Most of the URL are destined for web addresses, but others can point directly into a `FTP (File Transfer Protocol)` and a database access. In this lecture we will focus on URLs that point to web addresses or website locations.

URL structure consist in two parts:

- Protocol identifier - HTTP, HTTPS
- Resource Name - Name of the page
- Combining this two we get the web address

## HTTP
This stands for `HyperText Transfer Protocol` and it's the foundation of data communication in the WWW (The `HTTPS`is the same protocol but with a layer of security). Using this protocol generates a request to the server we are sending that request, this comes with a certain `HTTP verb` attached to it:

### HTTP Verbs
- GET: Retrieve information, can be a in loads or single
- POST: Write new information
- UPDATE: Updates information
- DELETE: Deletes information
- PUT: Updates information

So far, using the function `urlretrieve` we were making a GET request through HTTP. We can go further, extracting html from a page, lets say Wikipedia home page:

```python
from urllib.request import urlopen, Request

# Allocate URL into url
url = "https://www.wikipedia.org"

# Package the GET request
request = Request(url)

# Send and catch the response
response = urlopen(request)

# Read the response
html = response.read()

# Close connection
response.close()
```

Lets do the same but using another package, the `requests` package. This package makes the use of request a bit more easy. With one single function called `requests.get` we can send the request and catch the response, we later apply the method `text` to the response to get the HTML as text:

```python
import requests

url = "https://www.wikipedia.org/"

r = requests.get(url)
text = r.text
```
	
