# MySQL

1) Common commands

| Command | Action |
| --- | --- |
| ALTER | Alter a database or table | 
| BACKUP | Back up a table | 
| CREATE | Create a database | 
| DELETE | Delete a row from a table | 
| DESCRIBE | Describe a table's columns | 
| DROP | Delete a database or table | 
| EXIT | Exit | 
| GRANT | Change user privileges | 
| HELP | Display help | 
| INSERT | Insert data | 
| LOCK | Lock table(s) |
| QUIT | Exit |
| RENAME | Rename a table | 
| SHOW | List details about an object | 
| SOURCE | Execute a file |
| STATUS | Display the current status | 
| TRUNCATE | Empty a table |
| UNLOCK | Unlock table(s) |
| UPDATE | Update an existing record |
| USE | Use a database |

2) Creating a database ***publications***
```
CREATE DATABASE publications;
```
3) Creating users
```
GRANT PRIVILEGES ON database.object TO 'username'@'hostname'
  IDENTIFIED BY 'password';
```
4) Display databases
```
SHOW databases;
```
5) Describe table
```
DESCRIBE table;
```
6) Insert data into the table
```
INSERT INTO table(row1, row2, row3)
  VALUES('foo1', 'foo2', 'foo3');
```
7) Display data from the table
```
SELECT * FROM table;
```
8) Renaming table name ***foo*** to ***bar***
```
ALTER TABLE foo RENAME bar;
```
9) Renaming a column ***bar*** to ***bar1***(required data type to be specified)
```
ALTER TABLE foo CHANGE bar bar1 VARCHAR(16)
```
10) Changing datatype of ***bar*** to ***SMALLINT***
```
ALTER TABLE foo MODIFY bar SMALLINT;
```
11) Adding a new column named ***bar***
```
ALTER TABLE foo ADD bar SMALLINT UNSIGNED;
```
12) Removing a column ***bar***
```
ALTER TABLE foo DROP bar;
```
13) Delete a table ***foo***
```
DROP table foo;
```
