# Introduction to relational databases

One last thing to tackle is how to import data from a database. That's what we are going to do in this section of the Course. But first, we need to know what a `Relational Database` and how it works.

As we saw in the first part of the `Data Engineer Track` a relational database is a type of DB that embrace the relational model. This means it makes relations between the different attributes, generally in the form of tables. The relational database make use of `rows` and `columns`. Rows to store records that fit into the column's attributes.

If we make a quick look back to a structure we already know, we could stablish some relations. We are talking about the `Pandas` data structure we already seen before:

1. `Series`: This is a `one-dimension` structure is like a single column in a spreadsheet.

2. `DataFrame`: This is a `two-dimension` structure that looks like columns and rows in a database.

Then, if we take a look to the relational database we have a identical structure. This is a plus when we want to import data from a DB into Python.

Some of the `Relational Database Management System` more common are:

- `MySQL`
- `SQLite`
- `PostgreSQL`

*Note: Remember that all relational databases are written using a query language called SQL*

Some key points

- Each `row` or `record` in a table represents an `instance` of an entity type
- Each `column` in a table represents an `attribute` or `feature` of an instance
- Every table contains a `primary key` column, which has a `unique entry` for each row.
- There are `relations` between tables
