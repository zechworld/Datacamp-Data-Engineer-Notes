# Querying Relational DB directly with Pandas

After we created the engine with `SQLAlchemy` we can get the results of any particular query we want only using those four lines of code: `connecting`, `executing`, `parsing results into DataFrames`, and `naming columns`. We can still do better than this, and it's using the power of `Pandas` that allows us to reduce four lines of code into one:

### Before Pandas
```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Northwind.sqlite")

with engine.connect() as con:
	rs = engine.execute("SELECT * FROM Orders")
	df = pd.DataFrames(rs.fetchall())
	df.columns = rs.keys()
```

### After Pandas
```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Northwind.sqlite")

df = pd.read_sql_query("SELECT * FROM Orders", engine)
```
