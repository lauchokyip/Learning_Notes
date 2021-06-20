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
