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

We'll apply the method `.drop_duplicates()` that will make sure to erase those rows that are `complete duplicates`, leaving one copy behind. This method accepts the next arguments:

* `subset`: List of columns names to check for duplication 
* `keep`: Whether to keep `first`, `last`, or `all(False)` duplicate values
* `inplace`: Drop duplicated rows directly inside DataFrame without creating new object (True)

```python
# Drop duplicates
height_weight.drop_duplicates(inplace=True)
```
Then, this would be the remaining duplicate values we already found:

```python
# Output duplicate values
column_names = ['first_name', 'last_name', 'address']
duplicates = height_weight.duplicated(subset = column_names, keep = False)
height_weight[duplicates].sort_values(by = 'first_name')
```

||first_name|last_name|address|height|weight|
|--|--|--|--|--|--|
|28|Desirae|Shannon|14 Vancouver Drive|195|83|
|103|Desirae|Shannon|14 Vancouver Drive|196|83|
|1|Ivor|Pierce|102-3364 Non Road|168|66|
|101|Ivor|Pierce|102-3364 Non Road|168|88|


Now, to eliminate the last duplicates we could use statistical measures to combine each set of duplicated values. We could say that we want to combine each set into one single row, and for that we would need to think in a way to bind the two records.

In case of the `height`, we could say we need the `maximum` value out of the two because it could be the most updated data; in case of the `weight` we could say that we need the `mean / average` between the two values. It's important to say that deciding what to do and choosing which statistical measure to use will depend `entirely on common sense understanding of our data`.

To do what we mentioned, we need to create a `dictionary` called summaries specifying which functions will be parsed, which will instruct the `.groupby()` to return the maximum and mean. We then chain the `.agg()` method that allows us to run a function to the aggregation chain, in this case, it will pass the `summaries` dictionary to the `.groupby()` method to read the functions specified inside. We add the `.reset_index()` to have numbered indices in the final output. Lastly, we verify the duplicates array to see if we still have duplicated rows.

```python
# Group by column names and produce statistical summaries
column_names = ['first_name', 'last_name', 'address']
summaries = {'height': 'max', 'weight': 'mean'}

height_weight = height_weight.groupby(by = column_names).agg(summaries).reset_index()
```
```python
# Make sure aggregation is done
duplicates = height_weight.duplicated(subset = column_names, keep = False)
height_weight[duplicates].sort_values(by = 'first_name')
```

||first_name|last_name|address|height|weight|
|--|--|--|--|--|--|
|||||||
