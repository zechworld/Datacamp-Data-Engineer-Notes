# Scraping the web in Python

We just saw how to scrap HTML data with two libraries `urllib` and `requests`.Generally, HTML is a mix of `structured` and `unstructured` data. To turn the HTML data useful we need to parse it and extract that structured data. 

In this lecture we'll use the package `BeautifulSoup`. Sometimes, the HTML of a page is not correctly formatted, using wrong tags and creating what it's called a `tag soup`. This `package` helps formatting the `tag soup` into a more `beautiful soup` from which we can extract information with ease.

Lets see an example in action. For this we'll use `requests` again to send request and recieve the reponse, then we'll use method `BeautifulSoup()`.

```python
from bs4 import BeautifulSoup
import requests

url = "https://www.crummy.com/software/BeautifulSoup"

r = requests.get(url)

html_doc = r.text
soup = BeautifulSoup(html_doc)
```
Then we can `prettify` the soup Object and print it. What we will get from this the HTML properly written and indented.

```python 
print(soup.prettify())
```

Other methods we can apply to the `soupified HTML` is `soup.title` to get the title tag, and `soup.get_text()` to get the text tag. Other method is `find_all()`, this method helps us extract all occurrences of a certain tag, for example, if we use the `<a>` tag we can get all the URLs used in the HTML.

```python
for link in soup.find_all('a'):
	print(link.get('href'))
		# List of URLS in the HTML soupified
```
