# Creating a database engine in Python

Now we know what a relational database is, we need to make a connection to it. We'll use a SQLite database for the examples. Remember that this is just for mere cases of simplicity and speed, but be aware that the type of RDBMS you choose it's completely bound to what are the specifications and needs of the project you're doing.

There's a lot of packages available for Python to use SQL, like `sqlite3` (which comes natively in python since version 2.0) or `SQLAlchemy`. We'll use the latter due to its adaptability to work with many other RDBMS.

To make a connection using `SQLAlchemy` we need to import the function `create_engine()` and especify a string as argument that indicates the type of database and name of database.

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite://Northwind.sqlite') # [type of DB]://[Name of DB]
```

Also, we would like to know what are the name of the tables inside the database. For this we can use the function `table_names()` from the engine we just created.

```python
table_names = engine.table_names()
print(table_names)

# ['Categories', 'Customers', 'EmployeeTerritories', 'Employees', 'Order Details', 'Orders', 'Products', 'Region', 'Shippers', 'Suppliers', 'Territories']
```
