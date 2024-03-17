# Data type constrains

Lets us remember the Data Science Workflow

1. Access Data
2. Explore and process data
3. Extract insights
4. Report insights

If data is not cleaned, presenting duplicates, mis-pellings, data type parsing errors, legacy systems or whatever other error we will compromise the insights and integrity of reports.

Before preparing any analysis, we should make sure our variables have the correct data type. We make sure of this using some attributes and methods from Pandas package.

Lets imagine we are reading information from a `csv` file and then seeing the head to have a look of the data types the file contains:

```python
import pandas as pd

sales = pd.read_csv('sales.csv')
sales.head(2) # For sake of the example we'll read the first two records
```

|       | SalesOrder ID | Revenue | Quantity |
|-------|---------------|---------|----------|
|   0   |     43659     |  23153$ | 12       |
|   1   |     43660     |  1457$  |  2       |

We can see that the revenue column has a `$` sign. If we want to calculate the total revenue we'll get a mismatch in the data types. We can check this using the attribute `dtypes` from the DataFrame:

```python
sales.dtypes
```

|---|---|
|SalesOrderID | int64 |
|Revenue| object |
|Quatity | int64





