# Import Data

We can import data from multiple sources like:

- Flat files: .txt .csvs
- Navite files: Excel Spreadsheets, Stata, SAS, MATLAB files
- Relational Database: SQLite PostgreSQL

## Flat files
This files can be classified into two types of files that differ
in how they organize the data they carry:

	1. Plain Text: This category holds items like a novel, book, or a simple
	text file.

	2. Records: This category holds items like a table that could be inside a
	csv file, rows could be passengers and columns a feature (gender, cabin, etc).

To generate a connection with a file we need to use the **Python** function. For this
we need to assign a filename to a string variable, then use the **open** function and 
assign the **mode** argument with the letter 'r' (This ensure that we can only *read*).

```python
filename = 'huck_finn.txt'
file = open(filename, mode='r') # 'r' is to read
text = file.read()
file.close()
```

Is good practice to close the connection with a file, that's why we use the `file.close()` in the code. We can avoid to write the close function every time we open a file using a `with` statement. This will create a context where commands can be executed while the file is open, as the clause is closed the file will no longer be open. This is why the `with` statement is called a **Context Manager** binding a variable with the context manager construct. It's best practice to use this **approach** as we never have to concern to close the files again.

```python
with open ('huck_finn,txt', 'r') as file:
	print(file.read())
```

### Records & Plain Text

We'll work with csv now. But first we need to clarify what a *flat file* is, they are basically text files that doesn't contain a structured relationship, hence is not related to a relational database. Flat files have *records (rows)* and *attribute (columns)*.

Getting back to CSV files, this files are an _acronym_ for **Comma Separated Values** which in simple words means that the values in each row are separated by commas. In the other hand, the **plain text** files are files that have characters or sequences of them other than comas, such as a tab.

We have to decide what type of file we are importing. If they consist entire of numbers and we want to store them as a **NumPy Array** we should use **NumPy Package**, or if we want to store data in a DataFrame, we should use the **Pandas Package**.

