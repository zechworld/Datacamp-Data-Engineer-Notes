# Exercise 1
Now, it's time for liftoff! In this exercise, you'll perform the Hello World of SQL queries, SELECT, in order to retrieve all columns of the table Album in the Chinook database. Recall that the query SELECT * selects all columns.

```python
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
```




# Exercise 2
Congratulations on executing your first SQL query! Now you're going to figure out how to customize your query in order to:

- Select specified columns from a table;
- Select a specified number of rows;
- Import column names from the database table.

```python
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
	rs = engine.execute("")
	df = pd.DataFrame(rs.fetchmany(3))
	df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))
	#3

# Print the head of the DataFrame df
print(df.head())
	# Table
```





# Exercise 3
You can now execute a basic SQL query to select records from any table in your database and you can also perform simple query customizations to select particular columns and numbers of rows.

There are a couple more standard SQL query chops that will aid you in your journey to becoming an SQL ninja.

Let's say, for example that you wanted to get all records from the `Customer` table of the Chinook database for which the Country is `'Canada'`. You can do this very easily in SQL using a `SELECT` statement followed by a `WHERE`

```python
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
	rs = con.execute("SELECT * FROM Employee WHERE EmployeeId >= 6")
	df = pd.DataFrame(rs.fetchall())
	df.columns = rs.keys()

# Print the head of the df
print(df.head())
```




# Exercise 4
You can also order your SQL query results. For example, if you wanted to get all records from the Customer table of the Chinook database and order them in increasing order by the column SupportRepId, you could do so with the following query

```python
# Create the engine: engine
engine = create_engine("sqlite:///Chinook.sqlite")

# Open engine in context manager
with engine.connect() as con:
	rs = engine.execute("SELECT * FROM Employee ORDER BY BirthDate")
	df = pd.DataFrame(rs.fetchall())

	# Set the DataFrame's column names
	df.columns = rs.keys()

# Print head of df
print(df.head())
```





