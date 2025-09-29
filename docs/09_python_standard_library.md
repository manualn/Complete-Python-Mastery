# Python Standard Library
Python contains a comprehensive library of packages and modules that provides common features that is needed for building real applications. In this module you will explore python standard library more specifically. Ans also we will see how it works with files and directories, date and time objects, generate random values and send emails etc. 


# Working with Paths

In this chapter, you are going to learn about how to work with files and directories in Python

→ Path class is the foundation to work with files and directories

```python
#86_working_with_paths.py
from pathlib import Path
```

→ New path object can be created in different ways

→ Create an absolute paths like this

```python
#86_working_with_paths.py
Path("C:\\Program Files\\Microsoft")
```

→ When working with long ones, back slashes are ugly, this can be solved by using raw string

Example:

```python
#86_working_with_paths.py
from pathlib import Path
Path(r"C:\\Program Files\\Microsoft")
```

→ You can also create path objects that represents current folder

```python
#86_working_with_paths.py
Path("ecommerce/__init__.py")
```

→ Also you can combine one path with another by using slash. eg:

```python
#86_working_with_paths.py
Path() / Path("ecommerce")
```

→ Also the above combined path can be combined this with another string.
```python
#86_working_with_paths.py
Path() / "ecommerce" / "__init__.py"
```

→ Also we can get the home directory of current user by using a class method of Path class called home.
```python
#86_working_with_paths.py
Path.home()
```

→ To see the comprehensive version of this section search for python 3 pathlib.

Using the path class you can call the exist method to see if this file or directory exists or not
```python
#86_working_with_paths.py
path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)
print(path.stem)
print(path.suffix)
```

→ print(path.name) returns file name
→ print(path.stem) returns file name without extension
→ print(path.suffix) returns the extension of file

→ To get the parent of this path use path.parent

→ path.with_name() to create a new path object based on this existing path. But only name and extensions of the file can be changed.
```python
#86_working_with_paths.py
path = path.with_name("file.txt")
print(path)
print(path.absolute)
```
→ path.absolute is used to get absolute value of path.

Similar to changing name, we can also change suffix by using path.with_suffix()
```python
#86_working_with_paths.py
path = path.with_suffix(".txt")
print(path)
```

# Working with directories

→ Here we have a path objects that represents a directory. A few useful methods are discussed.

→ In terms of booleans, `mkdir` is used to create directory and `rmdir` to remove it.

→ And `rename` is used to rename it to a new name.

```python
# 87_working_with_directories.py
from pathlib import Path
path = Path("ecommerce")
path.exists()
path.mkdir()
path.rmdir()
path.rename("ecommerce 2")
```

→ Now another method is explained next called `iterdir`.

→ This method is used to get the list of files and directories in above path.

```python
# 87_working_with_directories.py
print(path.iterdir())
```

→ when you run the above code the result will be a generator object. we have mentioned about generator objects already.

→ while working with large lists, it will be difficult to store items into memory, so we use generator object, iterate it and get a new value everytime

→ This method returns generator objects because when working with files and directories, it is possible to have a directory with a million files in it.

→ So now we can iterate it over p

```python
# 87_working_with_directories.py
for p in path.iterdir():
    print(p)
```

As you can see in the results, path we got has both the files and directories

→ If you don't have path with million files, you can use the method as a list. Use a list comprehension

```python
# 87_working_with_directories.py
paths = [p for p in path.iterdir()]
print(paths)
```

→ The result is an array of posixpath objects.

→ The path class we have imported is the base class for two different classes, Posixpath and windows path

Posix is the standard use in unix like operating systems.

→ If you are on windows, you can See windows path objects

→ Now we can see list comprehension expression to the next level and apply filtering

```python
# 87_working_with_directories.py
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
```

This method is useful to get the list of files and directories in a path. but there are two limitations

1) we cannot search it by pattern
2) it doesn't search recursively.

→ In such situations, use a different method called glob

→ This method forms a pattern so that we can easily search for all files. Similar to other method this returns a generator.

```python
# 87_working_with_directories.py
path.glob("*.py")
```

→ Now we can change the above expression.

```python
# 87_working_with_directories.py
py_files = [p for p in path.glob("*.py")]
print(py_files)
```
→ In the result, we have a file path that has only one file

→ Recursive glob:

```python
# 87_working_with_directories.py
py_files = [p for p in path.rglob("*.py")]
print(py_files)
```

# Working with files

→ Here we will learn about useful methods of working with files

→ path.exists() is used to check if the file is used

→ path.rename() is used to rename it

→ Also we can delete it by using the unlink method

→ path.stat() returns the information about the files.

→ If you print the stat method, you will get a stacked result of objects with these attributes

like st-mode, st-ino etc.

→ we can also get the last access time in the attribute st-atime

→ st-mtime gives last modified time

→ st-ctime gives the creations time

→ All these time values are in seconds

```python
# 88_working_with_files.py
from pathlib import Path

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(path.stat())
```

→ To modify time to human readable time,

```python
# 88_working_with_files.py
from pathlib import Path
from time import ctime

path = Path("ecommerce/__init__.py")
print(path.stat().st_ctime)
print(ctime(path.stat().st_ctime))
```

→ There are a couple methods for reading data from a file

path.read_bytes()

→ This returns a file contents as bytes object

→ when representing binary data, path.read_text() returns the content of file as string

→ Also we can use built-in functions

with open("__init__.py", "r") as file:
    ...

print(path.read_text())

→ we also have another functions write-text to write some textual data

path.write_text("...")
path.write_bytes("...")

→ when coming to copying a file, these methods cannot be used

For that,

source = Path("ecommerce/__init__.py")
target = Path()/"__init__.py"

To copy this:

target.write_text(source.read_text())

→ This method is little tedious.

To make it easy:

import shutil

shutil.copy(source, target)

This approach is cleaner and easier in path object


# Working with zip files

In this section we are going to learn about how to work with zip files

```python
# 89_working_with_zip_files.py
from pathlib import Path
from zipfile import ZipFile

ZipFile("files.zip", "w")
```

Now we can store it in zip.

```python
# 89_working_with_zip_files.py
zip = ZipFile("files.zip", "w")
```

we have already learned about rglob to recursively find all the files in this directory

Path("ecommerce").rglob("*.*")

As you already know this will return a result as generators you should iterate over it.

```python
# 89_working_with_zip_files.py
for path in Path("ecommerce").rglob("*.*"):
    zip.write(path)

zip.close()
```

If there is any error, to avoid that you should try finally block or with statement.

```python
# 89_working_with_zip_files.py
from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)
```

Run this and you will get a zip file in ecommerce folder

To set file without opening it, to read only we should use another code:

```python
# 89_working_with_zip_files.py
from zipfile import ZipFile

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    zip.getinfo("ecommerce/__init__.py")

    # lets store it in another variable called info.
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)

    # New to extract all files from all zip files
    zip.extractall("extract")
```

# Working with csv files

In this lecture, we will learn how to work with csv files in python

→ First import csv and open a csv file. path function cannot be used to open file. Also close the file after you are done.

```python
# 90_working_with_csv_files.py

import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])  
    # similarly add second row
    writer.writerow([1000, 1, 5])
    writer.writerow([1000, 2, 15])
```

→ csv.writer will give us the file in csv format

→ writerow is to write it in tabular form

→ In that we can pass an array of values. for eg: here we are adding headers as first row.

If you save and run it, you can see data.csv file in your folder that contains these data given. Here we have a table of data each line represents a row. This is a very simple way to store data and transfer it from one machine to another

→ To open the same csv file in read mode, remove the second argument in open function.

→ Instead of csv writer, here we will use csv reader

```python
# 90_working_with_csv_files.py
import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
```

→ for printing row in read mode:

```python
# 90_working_with_csv_files.py
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

→ we have set the reader in a list already. This reader object has a index or a position that is set at the beginning. when we set reader as a list, that position goes to end of the file

→ without print(list(reader)) and run the program you will get three rows. Each row is an array of strings

# Working with JSON files

→ Here we are going to learn how to work with json files in python.

→ JSON stands for JavaScript Object Notation and is a popular way to format data in a human readable way.

→ It's very important to know json because a lot of popular websites provide their data in Json format.

→ firstly import json in python

```python
# 91_working_with_json_files.py
import json

movies = []

# Each movie is essentially a collection of key value pairs.
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993},
]

# Now call json.dumps and pass movies variable in that
data = json.dumps(movies)
print(data)
```

→ This is an example of json data.

Now instead of printing it on terminal, we are going to create path object.

```python
# 91_working_with_json_files.py
from pathlib import Path
Path("movies.json").write_text(data)
```

→ Now you learned how to write data in json file

→ If you get a json file from somewhere and you want to read it in python

```python
# 91_working_with_json_files.py
import json
from pathlib import Path

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0])
print(movies[0]["title"])
```

→ json.loads is used to load the dictionary.

→ This array of dictionaries can be printed.

# Working with a SQLite Database

→ In this lecture, we are learning how to work with SQLite in Python.

→ SQLite is a very lightweight database that we use for storing data on an application.

→ Its technology of small applications like the apps that we run on phones and tablets. It allows us to easily store our data in structure format with a table of rows and columns.

→ Import sqlite3 module first

```python
# 92_working_with_sqlite_databases.py
import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)
```

→ this movies object is printed and see if everything worked.

→ If you own this, the result will be a list of dictionaries.

→ To store this list in a database use sqlite3.

→ sqlite3.connect("db.sqlite3")

→ If the given file name doesn't exist, this method will create it.

→ This will return a connection object, and it should be closed.

→ better approach is to use with statement

```python
# 92_working_with_sqlite_databases.py
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies"
```

→ Here we are creating a string in command assuming we have a table called movies and add values with 3 question marks.

```python
# 92_working_with_sqlite_databases.py
command = "INSERT INTO Movies VALUES(?,?,?)"
```

→ This question marks are placeholders for values that are going to be supplied in the next step.

Next we are going to iterate over movies.

```python
# 92_working_with_sqlite_databases.py
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()
```

→ to get tuple of movie values this command can be used

→ If you run the above code, you will get an operational error.

Because here we are dealing with an empty database, this database doesn't have any tables

→ Search for db browser for sqlite in Google to know more about creating a new database

→ There you can add column names for your table

→ Now go back to the program and run again. there will be no error

→ And now go to back the db browser and select the movies. You can see the movie names are stored in a structured format

Now we can look at how to read data from database

```python
# 92_working_with_sqlite_databases.py
import sqlite3

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
```

→ Dont need to iterate here for reading data.

```python
# 92_working_with_sqlite_databases.py
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    movies = cursor.fetchall()
    print(movies)
```

→ If you run the above, you will get the list of titles

→ These are the basics of creating a database in python.

→ To study about database first be familiar with the sql programming language

# Working with Timestamps

Here we are going to work with date and time in python

There are two modules working with date and time.

1) Time module
 - gives us time stamp

2) Date-time module
 - which gives us date time objects with attributes like year, month and so on

→ In this lecture, we are going to learn time module

```python
# 93_working_with_timestamps.py
import time
time.time()
```

Time module has a method called time that returns the current date time as a time stamp.

```python
# 93_working_with_timestamps.py
import time
print(time.time())
```

the result will be a floating point number, which represents the number of seconds.

→ These time stamps are not human readable, so its used to perform calculations

→ For example to send email to 2000 recipients

```python
# 93_working_with_timestamps.py
import time

def send_emails():
    for i in range(10000):
        pass

start = time.time()
send_emails()
end = time.time()

duration = end - start
print(duration)
```

→ The result will be the time taken to execute this function.

→ We can also use the time module to calculate time taken to execute some piece of code

# Working with DateTimes

In this lecture, you are going to learn how to work with date time objects in Python.

→ Import datetime firstly and there is a method called datetime

```python
# 94_working_with_datetimes.py
import datetime
datetime.datetime(2018, 1, 1)
```

→ In datetime method you can pass the hour, minute, and year as well.

```python
# 94_working_with_datetimes.py
from datetime import datetime
dt = datetime(2018, 1, 1)
```

→ This code is more neat than the first one

```python
# 94_working_with_datetimes.py
datetime.now()
```

→ It is used to get the current date time

→ datetime.strptime is for parsing or converting a date time string.

→ This is particularly useful when we get input from the user or read it from the file.

```python
# 94_working_with_datetimes.py
from datetime import datetime
dt = datetime.now()
datetime.strptime
```

→ In all these scenarios, date time are represented as strings, and we need to convert them to date time objects

→ You can study about parsing date and its date format, search for python 3 strptime in google.

In that page, you can see the directives.

→ If you use a lowercase y, that represents a two digit year

```python
# 94_working_with_datetimes.py
import time
from datetime import datetime

dt = datetime.strptime("2018/01/01", "%Y/%m/%d")

dt = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m/%d"))
```

→ We also have a method for formatting date time, ie dt.strftime(). This method opposite of strptime. So with this method we convert a string into a date time.

→ You can also compare dates

```python
# 94_working_with_datetimes.py
from datetime import datetime
import time

dt1 = datetime(2018,1,1)
dt2 = datetime.now()
print(dt2 > dt1)
```

# Working with Time Deltas

→ To get time duration, timedelta is used.

```python
# 95_working_with_time_deltas.py
from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
```

→ If you run the code above, you'll get the difference between those two dates.

→ timedelta object has a few interesting attributes

```python
# 95_working_with_time_deltas.py
print("days", duration.days)
print("seconds", duration.seconds)
```
→ There is another method called total seconds. This is a method not an attribute.
```python
# 95_working_with_time_deltas.py
print("total-seconds", duration.total_seconds())
```

→ The result of the above code will be durations represented as seconds.

→ You can also add a time delta object to a date time object.

```python
# 95_working_with_time_deltas.py
from datetime import datetime, timedelta
dt1 = datetime(2018, 1, 1) + timedelta(1)
print(dt1)
```

→ The result printed will be 2018-01-02

→ Now you may be wondering what is 1 in timedelta(1). For clarity, you can set the keyword argument, for example:

```python
# 95_working_with_time_deltas.py
timedelta(days=1, seconds=1)
```