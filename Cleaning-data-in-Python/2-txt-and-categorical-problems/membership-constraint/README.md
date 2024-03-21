# Categories and Membership constraints
Categorical data represent data that can be shown as a finite quantity of posibilities. Like a `marriage status`, `household income` or `loan status`. This values often are represented in the machine as consecutive numbers:

|Type of data| Example values| Numeric representation|
|---|---|---|
|Marriage status| unmarried, married|0, 1|
|Household Income category| 0-20K, 20-40K, ...|0, 1, 2,...|
|Loan Status| default, payed, no_loan| 0, 1, 2|

## Problems associated
This type of data could have inconsistencies in form of `data entry errors` like free text or dropdowns, also it could be due to `parsing errors`.

## How do we treat these problems?
To solve this issues we have a variety of ways to solve them. The most simple of them is to `drop the data`. We can attempt to `remap the categories`, or `inferring categories`.

Lets have a DataFrame as an example called `study_data` that contains a list of name, birthday and blood type. Another DataFrame has been created containing the correct possible categories for blood type.
### Study data
```python
study_data = pd.read_csv('study.csv')
```
||name|birthday|blood_type|
|--|--|--|--|
|1|Beth|2019-10-20|B-|
|2|Ignatius|2020-07-08|A-|
|3|Paul|2019-08-12|O+|
|4|Helen|2019-03-17|O-|
|5|Jennifer|2019-12-17|Z+|
|6|Kennedy|2020-04-27|A+|
|7|Keith|2019-04-19|AB+|

### Correct possible blood type

||blood_type|
|--|--|
|1|O-|
|2|O+|
|3|A-|
|4|A+|
|5|B+|
|6|B-|
|7|AB+|
|8|AB-|

If we see the `study_data` table, we can see that there's a `Z+` record which doesn't exist. This is why we have the second where we can extract the correct blood types. It's a good practice to keep a log of all possible values of your categorical data.

## Joins Reminder
There are two main types of joins we need to take in consideration: `anti joins` and `inner joins`. When we join two DataFrames we need to do it on common clumns between them.

`Anti joins`: Takes in all the data from one DataFrame that's not is not contain in another. For example: 

* A `Left Anti Join` between `DataFrame A` and `DataFrame B`, would return the columns of both DataFrames for values only found in A with the common column

* A `Inner Join` of `DataFrame A` and `DataFrame B` would return columns from bouth DataFrames for values `only` found in A and B of the common column between them being joined on.

---
In our example, if we do a `Left Anti join` we would have as result all the data in study with inconsistencies in the blood type.

*(We'lll use tables to show how the distributions are made, but this example gets easier to understand if using a `Venn Diagram`)*

### Left Anti Join
#### Data Return: study_data with Z+ inconsistency (study_data header)

|study_data | joined|categories|
|--|--|--|
|***Z+***|A-|B+|
|***Z+***|O-|B+|
|***Z+***|AB+|AB-|
|***Z+***|A+|AB-|
|***Z+***|O+|B+|
|***Z+***|B-|AB-|
|***Z+***|O+|B+|

### Inner Join
#### Data Return: All rows except those with Z+, B+ and AB- (joined header)
|study_data | joined|categories|
|--|--|--|
|Z+|***A-***|B+|
|Z+|***O-***|B+|
|Z+|***AB+***|AB-|
|Z+|***A+***|AB-|
|Z+|***O+***|B+|
|Z+|***B-***|AB-|
|Z+|***O+***|B+|

Lets do this in Python:

We need to get all inconsistent data in the `blood_type` column of the `study_data`. We can do this by creating a `set` that will hold the inconsistent values by using the method `.difference()` and passing as argument the `blood_type` column from the `correct categories`, therefore generating a difference between one DataFrame and the other one.

```python
inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type'])

print(inconsistent_categories) # {'Z+'}
# As we need to remember, a set will hold a unique value.
# This means if incounters 234 ocurrences of Z+ it will only
# Save one inside the {}
```

Then we need to find all inconsistent rows with this `"filter (inconsistent_categories)"` we've just created. We'll use the `isin()` method that returns a list of `boolean values` using the column `blood_type` from the study_data and finally we can `subset` those values that are `true` for the inconsistent data.

```python
# Get and print rows with incosistent categories
inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)
study_data[inconsistent_rows]
```
||name|birthday|blood_type|
|--|--|--|--|
|5|Jennifer|2019-12-17|Z+|

The last step we need to do is to drop the `inconsistent` rows and keep the one `consistent`. We can use the `~`symbol while subsetting which returns `everything except`inconsistent rows.

```python
# Drop inconsistent categories and get consistent data only
consistent_data = study_data[~inconsistent_rows]
```

### Example

|Membership / Categorical or Constraint | Other Constraint
|--|--|
|A `GPA` column containing a `Z-` grade|A `revenue`column represented as a string|
|A `has_loan`


