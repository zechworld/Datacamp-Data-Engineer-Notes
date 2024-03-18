# Data range constraints

This contraints are important to consider when delimiting the acceptable range of the data you're working on. For example, having a movie dataset, and it has been stablished that a rating from `1 to 5`' but in checking the data and building a histogram with `matplotlib` we encounter that there are some movies with an average rating of 6.

```python
import matplotlib.pyplot as plt

plt.hist(movies['avg_rating'])
plt.title('Average rating of movies (1-5)')
```

Another example could be a `suscription dates` dataset. We could have suscriptions that start in the future, hence is wrong data. We could use the `datetime` package and use the `date.today()` to get today's date. and filter the dataset by a date higher than today's date.

```python
# Import date time
import datetime as dt

today_date = dt.date.today()
user_signups[user_signups['subscription_date'] > dt.date.today()]
```

We have different ways to deal with this problem. A simple way to solve this is dropping the data, but, this way is recommended only when a small portion of the dataset is affected, otherwise important and essential information could be lost.

The best way to tackle this is to understand the dataset. In our case, perhaps is better to set a custom minimum and maximum to the colum. Or we could also set the data to `missing`, or assign a `custom value` for any values that go beyond certain range.

---
Lets go back to the movies example. We are going to isolate the movies with ratings higher than 5, if this values affect a small st of our data, we can drop them. We can do the latter in two different ways:

1. Create a new `DataFrame` with values lower or equal than 5
2. Drop values using drop.


```python
# Drop values using filtering
movies = movies[movies['avg_rating'] <= 5]

# Drop values using .drop()
movies.drop(movies[movies['avg_rating'] > 5].index, inplace = True)
```
The drop method takes as argument the `row indices of movies` for which the avg_rating is `higher than 5`. The argument `inplace` is set to `true`so the data is dropped in place and we don't have to create a new column. We can finally test if this worked using the `assert` function.

```python
assert movies['avg_rating'].max() <=5
```

Depending on the assumptions we make on our data, perhaps is better to create a `hard limit` for the rating values, like every value that goes beyond our maximum (5) we force the value to 5. We can do this using the `.loc` method that returns all cell that `fit a custom row`.

This function accepts as first argument the row column label, in our case `avg_rating`. Finally, we can `assert` if the change was done succesfuly.

```python 
# Convert avg_rating > 5 to 5
movies.loc[movies['avg_rating'] > 5, 'avg_rating'] = 5

# Assert statement
assert movies['avg_rating'].max() <= 5
```

Moving to the example with subscriptions happening in the future. The First step we'll do is check the data types of the columns:

```python
import datetime as  dt
import pandas as pd

# Output data types
user_signups.dtypes
```
|||
|--|--|
|subscription_date|object|
|user_name|object|
|Country|object|
|dtype: object|

As we can see, the `subscription_date`'s type is `object` and it should be `date`. For this we'll apply the `Pandas` function `to_datetime` that takes as argument the column we want to convert into and then use the function from the `datetime` package `dt.date`.


