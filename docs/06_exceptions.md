# Exceptions

While programming, there may occur many mistakes and errors.

These errors are mainly due to mistakes from programmers or due to wrong data and data source.

For example:

```python
# 72_exceptions.py
numbers = [1, 2]
print(numbers[3])
```

When you run this program, you will get index error.

In programming, we refer this kind of error as an exception. An exception is a kind of error that terminates the execution of a program.

Another example:

```python
# 72_exceptions.py
age = int(input("Age: "))
```

It's your job as a programmer to handle these exceptions and prevent your applications from crashing.

# Handling exceptions

Here we are studying how to handle exceptions.

```python
# 73_handling_exceptions.py
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age")

print("Execution continues")
```

From running this program, you will have to not enter an as age, or else you'll get a friendly error message and your application will not crash.

This is about handling exceptions properly.

We can also add else statement here.

```python
# 73_handling_exceptions.py
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")

print("Execution continues.")
```

# Handling different exceptions

If you give an extra line of code in the programs we studied in the last chapter:

```python
# 74_Handling_different_exceptions.py
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
```

This program output will give you error ZeroDivisionError.

To solve this, add different exceptions:

```python
# 74_Handling_different_exceptions.py
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age")
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No exceptions were thrown")
```

Also, if the exception message is same for ValueError and ZeroDivisionError, then the code can be rearranged like this:

```python
# 74_Handling_different_exceptions.py
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
```

# Cleaning up

If a file is opened, it should be closed after the program, or else error may occur. There may be times you need to work with external resources like files, network connections, databases and so on.

Whenever these are used, after you're done you should release them. If not, another process or another program may not be able to open that file.

```python
# 75_cleaning_up.py
try:
    file = open("75_cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    file.close()

except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")

```
In this case, the file may not work in other blocks.

Therefore it can be rewritten as:

```python
# 75_cleaning_up.py
try:
    file = open("75_cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
finally:
    file.close()
```

This finally clause is always executed whether we have an exception or not.

# The with statement

Here we will learn a shorter and cleaner way, without the finally clause. But it won't always work for certain kind of objects.

- with statement is used

```python
# 76_the_with_statement.py
try:
    with open("75_the_with_statement.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
```

Whenever we open file with "with" statement, python will automatically call file close whether you have a final clause or not.

Two magic methods are used here in detail: enter and exit.

When you have to open multiple files:

```python
# 76_the_with_statement.py
try:
    with open("75_the_with_statement.py") as file, open("another.txt") as target:
        print("Files opened")
```

another.txt file doesn't exist; just to show how the program will be.

# Raising exceptions

Here we are studying to raise or throw exceptions in your own code.

Search python 3 built-in exceptions in google and you can see details of exceptions on Python and what they're used for.

```python
# 77_raising_exceptions.py
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
``` 

# Cost of raising exceptions
Raising exceptions comes with a cost. So we could have an alternative way by writing your own functions.

```python
# 78_cost_of_raising_exceptions.py
from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
print("first code ", timeit(code1, number = 10000))

```
Try it another way:
```python
# 78_cost_of_raising_exceptions.py
from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
print("first code ", timeit(code1, number = 10000))

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return none
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("second code ", timeit(code2, number = 10000))
```
In th output you can see our first implementation as well as second implementation.

Second one is four times faster.

So think twice if you want to build functions raising exceptions.