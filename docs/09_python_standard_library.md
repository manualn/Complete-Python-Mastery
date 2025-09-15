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


