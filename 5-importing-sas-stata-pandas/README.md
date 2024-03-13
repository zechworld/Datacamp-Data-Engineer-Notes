# Importing SAS / Stata files using Pandas

There's a lot of software dedicated to statistics, and it's important as a Data Scientist to know how to import files from this softwares into a `DataFrame / Python` environment. The most common examples are SAS which stands for `Statistical Analysis System` and is used in *business analytics* and *biostatistics*, and Stata which is a contraction of `Statistics and Data` and is used in *academic social sciences research*, *economics* and *epidemiology*.

## SAS Files uses:
- Advanced analytics
- Multivariate analysis
- Business Intelligence
- Data Management
- Predictive Analytics
- Standard for Computational Analysis

### Importing SAS files
SAS files have the extension `.sas7bdat (dataset file)` and `.sas7bcat (catalog file)`. To import this files we need the package `sas7bdat` and from it the function `SAS7BDAT` (Bare in mind the difference between package and function is upper case and lower case). Then we need to use a context manager using `with` like we have used before, binding the variable file with the path of the file. Finally, we assign the result of the method `to_data_frame()` to a `df_sas` variable.

```python
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file:
	df_sas = file.to_data_frame()
```

### Importing Stata files
Stata files have the extension `.dta`. This files have the advantage that we don't need to setup a context for them to be used. In this case we pass the filename into a function and assign it to a variable.

```python
import pandas as pd
data = pd.read_stata('urbanpop.dta')
```
