# Exercise 1
Here, you'll take advantage of the power of `pandas` to write the results of your SQL query to a DataFrame in one swift line of Python code!

You'll first import `pandas` and create the SQLite `'Chinook.sqlite'` engine. Then you'll query the database to select all records from the `Album` table.

Recall that to select all records from the Orders table in the Northwind database, Hugo executed the following command:
```python
df = pd.read_sql_query("SELECT * FROM Orders", engine)
```

```python
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine("sqlite:///Chinook.sqlite")

# Execute query and store records in DataFrame: df
df1 = pd.read_sql_query("SELECT * FROM Album", engine)

# Print head of DataFrame
print(df1.head())

# Open engine in context manager and store query result in df2
with engine.connect() as con:
	rs = engine.execute("SELECT * FROM Album")
	df2 = pd.DataFrame(rs.fetchall())
	df2.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))

# True
```




# Exercise 2

Here, you'll become more familiar with the pandas function `read_sql_query()` by using it to execute a more complex query: a `SELECT` statement followed by both a `WHERE` clause `AND` an `ORDER BY` clause.

You'll build a DataFrame that contains the rows of the `Employee` table for which the `EmployeeId` is greater than or equal to 6 and you'll order these entries by `BirthDate`.

```python
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine("sqlite:///Chinook.sqlite")

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate", engine)

# Print head of DataFrame
print(df.head())
```

