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

# Generating Random Values

In this section you'll learn to generate random values in python

```python
# 96_generating_random_values.py
import random
random.random()
```

→ random module has a method called random which is used to generate random numbers.

```python
# 96_generating_random_values.py
print(random.random())
```

→ If you run this you will get a floating number.

→ To get random number between 1 and 10

```python
# 96_generating_random_values.py
print(random.randint(1,10))
```

→ Another method called choice that takes an array of numbers and randomly picks one of the numbers from it

```python
# 96_generating_random_values.py
print(random.choice([1, 2, 3, 4]))
```

→ Another similar method called choices that selects multiple values from the array.

```python
# 96_generating_random_values.py
print(random.choices([1, 2, 3, 4], k=2))
```

→ This returns the two random numbers from the original array

→ With the help of this method, you can create a password

```python
# 96_generating_random_values.py
print(random.choices("abcdefghi", k=4))
```

→ By running the above code you will get an array of randomly selected 4 letters.

→ Now we should the random letters into a string

```python
# 96_generating_random_values.py
print("".join(random.choices("abcdefghi", k=4)))
```

→ There is another module called strings which have many interesting attributes

```python
# 96_generating_random_values.py
import string
print(string.ascii_letters)
```

→ This returns a string that includes all the lower and upper case letters we also have:

```python
# 96_generating_random_values.py
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
```

→ so while creating password you can use this method.

```python
# 96_generating_random_values.py
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))
```

→ we also have another method for shuffling an array.

```python
# 96_generating_random_values.py
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
```

# Opening the Browser

→ In this chapter, you will learn how to open a web browser in a python script.

→ This is useful if you're building an automation script that does a bunch of tasks.

→ For example, if you want to build a script to deploy your website. For that, build your website locally on your development machine and then get deployed to a web server

→ For building browser first you have to import webbrowser.

→ This module has a method called open

```python
# 97_opening_the_browser.py
import webbrowser
print("Deployment completed")
webbrowser.open("http://google.com")
```

→ when you run the program, first you will get the sentence printed and then the browser window opens.

# Sending emails

Here you are going to learn how to send emails in python.

→ This is very useful if you have a database of customers

→ For this, you have to import various classes, 1 to create email messages and the other to connect with an smtp server for sending emails.

```python
# 98_sending_emails.py
from email.mime.multipart import MIMEMultipart
```

→ In this package there is a subpackage called mime. Mime stands for multipurpose internet mail extension. This is the standard that defines the format for email messages

→ In this package, there is another sub package that is multi part that exposes a class called mime multipart. With this you can send email messages that includes both html and plain text

→ first step is to setup various headers

```python
# 98_sending_emails.py
message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "testuser@codewithmosh.com"
message["subject"] = "This is a test"
```

→ These headers are supported by MIME multi part objects

→ It has a method called attach, which is mainly used to attach body.

```python
# 98_sending_emails.py
from email.mime.text import MIMEText
message.attach(MIMEText("Body"))
```

→ Now we need to send this using an smtp server, for that import smtplib

→ This module has a method called SMTP, and here we should pass two keyword arguments

```python
# 98_sending_emails.py
import smtplib
smtplib.SMTP(host="smtp.gmail.com", port=587)
```

→ this value we set depends on the smtp server.

```python
# 98_sending_emails.py
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
```

→ starttls is used to put the smtp connection in tls mode.

→ tls stands for transport layer security.

```python
# 98_sending_emails.py
smtp.starttls()
smtp.login("testuser@codewithmosh.com", "today")
```

→ Now finally call smtp and there is a method called send_message and pass the email message object

```python
# 98_sending_emails.py
smtp.send_message(message)
print("sent...")
```

→ To send email, use the send_message method and pass the message object.

```python
# 98_sending_emails.py
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mosh@codewithmosh.com", "today")
    smtp.send_message(message)
    print("Sent...")
```

→ This is how you send emails in python.

→ Now to attach an image to email

```python
# 98_sending_emails.py
from email.mime.image import MIMEImage
message.attach(MIMEImage())
```

→ pass the image and attach it to email object for that:

```python
# 98_sending_emails.py
from pathlib import Path
message.attach(MIMEImage(Path("mosh.png").read_bytes()))
```

# Templates

→ html is mainly used in building templates. html is the language of the web. webpages are used to present content

→ Here you are going to learn how to create templates in python.

→ Firstly create a template in your folder.

→ Name the template according to the purpose.

→ There is a simple technique to create an html template: press exclamation mark + tab

→ when sending email, we don't need any text in the head section

→ To define a parameter, start with a dollar sign and give that parameter a name.

```html
<!DOCTYPE html>
<html lang="en">
<head></head>
<body>
  Hi $name, this is our test email
</body>
</html>
```

→ Now go back to python code

```python
# 99_templates.py
from string import Template
from pathlib import Path

template = Template(Path("template.html").read_text())
message.attach (MIMEText(template.substitute(), "plain"))
```

→ Here you can pass two parameters for template. Now to make the code neat.

```python
# 99_templates.py
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
```

→ This email message is pretty simple, this doesn't use any html

→ Now add a string around the name. Now run the application

→ See one more time you can see the name is bold. This is the benefit of using html over plain text

# Command line Arguments

Here we will know more about python program that expands command line arguments. We can add additional arguments in a command line. For example, in a file name argument, you can add the name of a user, email, password etc.

For that first import sys module. This module has an attribute called argv short for argument variables.

```python
# 100_command_line_arguments.py
import sys
print(sys.argv)
```

→ first item that will get printed is always the name of our python program

→ All arguments are represented as separate items.

→ If you want to get the length of array and if it is equal to one then the user has not supplied any arguments.

```python
# 100_command_line_arguments.py
if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("password", password)
```


# Running External Programs

In this session you are going to learn how to call external programs from your python scripts, basically how to run any of the operating system commands as well as external programs.

with this module you can observe a child process
```python
# 101_running_external_programs.py
    import subprocess
```

→ A process is basically an instance of a running program

→ In the subprocess module we have a bunch of functions or methods like call, check-call, and check-output etc.
```python
# 101_running_external_programs.py
    subprocess.call
    subprocess.check_call
    subprocess.check_output
    subprocess.Popen
```

→ These methods are helper methods to create an instance of the

popen class process.

run method is used to run external program. The first argument of this method is an array of strings

```python
# 101_running_external_programs.py
import subprocess
subprocess.run(["ls", "-l"])
```

→ Now let's look at the return value of this method

```python
# 101_running_external_programs.py
import subprocess
result = subprocess.run(["ls","-l"])
print(type(result))
```

→ If you run the program, you'll get an instance of this class

→ Now rename it as completed

```python
# 101_running_external_programs.py
import subprocess
completed = subprocess.run(["ls","-l"])
print(completed.args)
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)
print("stdout", completed.stdout)
```

The run method takes quite a few keyword arguments and all of these have default values. Now you're going to use captured output. If you set this to true, when you run this program, the output will not be printed on the terminal

```python
# 101_running_external_programs_keyword_args.py
import subprocess
completed = subprocess.run(["ls", "-l"], capture_output=True)
```

→ now lets add more arguments

```python
# 101_running_external_programs_keyword_args.py
import subprocess
completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
```

→ now when you run the program, you'll no longer see a b prefix.

→ create another file called other.py. This is a complicated python script that we will call as part of running our main script

```python
# other.py
print("Here is a complicated script")
```

→ now to back to previous file

```python
# 101_running_external_programs_keyword_args.py
import subprocess
completed = subprocess.run(["python3", "other.py"], capture_output=True, text=True)
```

→ now you run this programs and you can see the other script is executed.

```python
# 101_running_external_programs_keyword_args.py
import subprocess
completed = subprocess.run(["false"], capture_output=True, text=True, check=True)
```

→ If you run this, you will get returncode as 1

```python
# 101_running_external_programs_keyword_args.py
if completed.returncode != 0:
    print(completed.stderr)
```

→ If you run this , the class will be in the subprocess module,

To check for errors like this, you can wrap this code in a try block and then add the except clause

```python
# 101_running_external_programs_keyword_args.py
import subprocess

try:
    completed = subprocess.run(["false"], capture_output=True, text=True, check=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
```

→ So this is all about running external programs in your python script

