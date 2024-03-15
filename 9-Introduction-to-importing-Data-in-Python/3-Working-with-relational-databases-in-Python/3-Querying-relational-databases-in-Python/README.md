# Querying relational databases in Python

Lets remember a basic line of SQL that allows us to retrieve all columns and all rows from a table. 

```SQL
SELECT * FROM Table_Name
```

## Workflow of SQL querying
We'll follow the next workflow for making our first query using the things we alreay saw:

1. Import the required packages and functions
2. Create the engine
3. Connect to it
4. Query the database and save the results onto a DataFrame
5. Close connection

```python
# Importing the required packages & functions
from sqlalchemy import create_engine
import pandas as pd

# Create the engine: engine
engine = create_engine('sqlite:///Northwind.sqlite')

# Connect to the engine
con = engine.connect()

# Query the DB and store results in DataFrame: rs
rs = con.execute("SELECT * FROM Orders")
df = pd.DataFrame(rs.fetchall())

# Close the connection
con.close()
```

We can print then the head of the exported df

```python
print(df.head())
```

This piece of code will give us a DataFrame with the data exported. But, the column names won't be accurate. To fix this we must set the names using the function `df.columns` before closing the connection:

```python
# Previous code ^

con = engine.connect()
rs = con.execute("SELECT * FROM Orders")

df = pd.DataFrame(rs.fetchall())

# Assign the column names into the DataFrame
df.columns = rs.keys()

con.close()
```

Finally, we can use a `context manager` to open the connection and then closing the connection later. In the next code, the only difference you can see with the code before is that instead of `selecting all with SELECT *` we are now specifying with columns we want to be retrieved, and the function `fetchall()` has been changed for `fetchmany(size=n)` which allows us to select the quantity of rows retrieved by the query.

```python
with engine.connect() as con:
	rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
	df = pd.DataFrame(rs.fetchmany(size=5))
	df.columns = rs.keys()
```
