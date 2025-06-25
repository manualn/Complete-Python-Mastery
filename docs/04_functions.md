# Defining Functions
We have learned many built-in functions so far such as "print()", "round()" and so on.

Here you are going to learn to write your own functions.

The "def" function is used here.

Name your function meaningful, descriptive and use lowercase letters and an underscore to separate multiple words.

```python
#  39_defining_functions.py
def greet():
    print("Hi there")
    print("Welcome aboard")

greet()
```

Run this program and you will get these sentences as output. 


# Arguments
In the previous chapter, do you know what is the difference between greet function and print function? The difference is that print function takes an input whereas greet function doesn't take any.

Here you are going to learn how to pass inputs like first name and last name to this function.

```python
#  40_arguments.py
def greet(first_name, last_name):
```

The list parameters between parentheses.

When calling this function you should put two values, and these are referred to as arguments. Argument is the most common word used by developers. Many are confused between parameter and argument. Parameter is the input that you define for your function and argument is the actual value for a given parameter.

```python
#  40_arguments.py
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

greet("Mosh", "Hamedani")
greet("John", "Smith")
```

Here greet function should take two parameters. If only one argument is given while running this function, then it will show error saying missing 1 required positional argument. 


# Types of Functions
There are two types of functions:

1) Functions that perform a task
2) Functions that calculate and return a value

**Examples:**

The round() function is an example of a second function:
```python
#  41_types_of_functions.py
round(2.8)
```

Functions that you create fall into both categories:

```python
#  41_types_of_functions.py
def greet(name):
    print(f"Hi {name}")
```

This program is not included in the first category.

It can be rewritten into the second category:
```python
#  41_types_of_functions.py
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Mosh")
```

With the print message implementation we are limited to printing it in the terminal. Here we cannot reuse the greet function in other scenarios.

In the second implementation, it simply returns a value and we can do anything with that. Also we use it in built-in functions and open it for writing.

What if we put `greet("Mosh")` inside print function?

```python
#  41_types_of_functions.py
def greet(name):
    print(f"Hi {name}")

print(greet("Mosh"))
```

We get output as "Hi Mosh" followed by "None".

"None" is the return value of greet function.

In Python all functions by default return the None value. None is an object that represents the absence of a value.

Even though this function returns None, it is still classified as a function that carries out the task. 


# Keyword Arguments
Take another function:

```python
#  42_keyword_arguments.py
def increment(number, by):
    return number + by

result = increment(2, 1)
print(result)
```

Here we don't need this long program. So it can be shortened like this:

```python
#  42_keyword_arguments.py
def increment(number, by):
    return number + by

print(increment(2, 1))
```

Now we can make this code more readable. For that you can use keyword arguments:

```python
#  42_keyword_arguments.py
print(increment(2, by=1))
```

If you're calling a function with multiple arguments, keyword arguments can be used to make it readable. 


# Default Arguments
All parameters defined for a function are required by default.

This parameter below is given a default value:

```python
#  43_default_arguments.py
def increment(number, by=1):
    return number + by

print(increment(2))
```

In this case we have set a default argument. 

# Xargs
```python
#  44_xargs.py
def multiply(x, y):
    return x * y

multiply(2, 3)
```

Here only two parameters can be used.

For if you want to pass one or more or two arguments:

```python
#  44_xargs.py
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))
``` 
