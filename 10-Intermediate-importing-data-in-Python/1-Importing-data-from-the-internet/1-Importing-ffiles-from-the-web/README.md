# Importing flat files from the web

We already saw how to import a large quantity of files to Python, but there is a much more broader source of information that we need to know how to extract and import data from, the `Web`.

Say you want to `retrieve information` from a web page, for this you normally would go and download files for your research manually. This approach is okay if you're making a small research for personal use, but it poses a few `problems` if we want to `scalate` to a bigger project. First, there's no written code so, if someone (another Data Scientist) wanted to reproduce your workflow it would neccesarily have to go outside Python to download those files, hence `reproducibility problems`.

Another problem we encounter has to do with `scalability`. Say we have to download a file once, then a hundred times, then a thousand times, the proportion of time taken to download those files would proportionally increase with the number of downloads.

To tackle this problem we'll learn to use `Python` to scrap the web and import data from it, saving them locally and loading that data into `Pandas DataFrame`. We'll learn how to make `HTTP Request` with `GET`, for this we'll get familiar with the `urllib` package.

## The urllib package
This package provides a high-level interface for fetching data across the `World Wide Web (WWW)`. The function `urlopen` is similar to the buil-in function `open` that accepts `URL (Universal Resource Locators)` instead of filenames.

## How to automate file download in Python
First we're going to import the function `urlretrieve` from the `request` subpackage of `urllib`. Second, we'll assign the URL to a variable. Finally, we'll use the `urlretrieve` function to import the data from the web and write it into a `csv file`.

```python
from urllib.request import urlretrieve
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url, 'winequality-white.csv')
```
