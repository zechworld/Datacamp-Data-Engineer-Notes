# Unique values

When we're doing cleaning of the data another common cleaning problem we encounter is `duplicate values`. This can be spotted or diagnosed when the same exact information is reapeted across multiple rows for some or all columns in our DataFrame.

#### All columns have the same values
|first_name|last_name|address|height|weight|
|---|---|---|---|---|
|Justin|Saddlemyer|Boulevard du Jardin Botanique 3, Bruxelles|193cm|87kg|
|Justin|Saddlemyer|Boulevard du Jardin Botanique 3, Bruxelles|193cm|87kg|
#### All columns have the same values, except the height
In this one, is more likely a data entry error than an actual other person.
|first_name|last_name|address|height|weight|
|---|---|---|---|---|
|Justin|Saddlemyer|Boulevard du Jardin Botanique 3, Bruxelles|193cm|87kg|
|Justin|Saddlemyer|Boulevard du Jardin Botanique 3, Bruxelles|*194cm*|87kg|

## Why do they happen?
* Data entry errors
* Human error
* Bugs and design errors
* Most arise from joining and consolidating data from various resources

## How to find duplicate values?
First lets work with a bigger table or DataFrame and apply the `.head()` to see the head of it.

||first_name|last_name|address|height|weight|
|--|--|--|--|--|--|
|0|Lane|Reese|534-1559 Nam St.|181|64|
|1|Ivor|Pierce|102-3364 Non Road|168|66|
|2|Roary|Gibson|P.O. Box 334, 7785 Nisi Ave|191|99|
|3|Shannon|Little|1244 Maori Jack Road|185|65|

We can spot duplicates really easy with the DataFrame method `.duplicated()`. This will return a `Series` of boolean values `True for Duplicate` and `False for Non-Duplicates`. We can assign a variable that holds the values, and then pass this variable inside the brackets to see exactly which rows are affected.

Relying only in one column been analyzed by this method could lead to misleading results. Its advisable to use two arguments in this method. The `arguments` are:

	* `subset`: List of column names to check por dupication.
	* `keep`: Whether to keep *first, *last* or *all (False)* duplicate values.

```python
# Column Names to check for duplication
column_names = ['first_name', 'last_name', 'address']
duplicates = height_weight.duplicated(subset = column_names, kee
height_weight[duplicates].sort_values(by='first_name')
```

||first_name|last_name|address|height|weight|
|--|--|--|--|--|--|
|22|Cole|Palmer|8366 At, Street|178|91|
|102|Cole|Palmer|8366 At, Street|178|91|
|28|Desirae|Shannon|14 Vancouver Drive|195|83|
|103|Desirae|Shannon|14 Vancouver Drive|196|83|
|1|Ivor|Pierce|102-3364 Non Road|168|66|
|101|Ivor|Pierce|102-3364 Non Road|168|88|
|37|Mary|Colon|4674 Ut Rd.|179|75|
|100|Mary|Colon|4674 Ut Rd.|179|75|
|


