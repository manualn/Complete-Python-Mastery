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

# Xxargs 

In the last lecture, you learned the syntax to pass a variable number of arguments to a function. Now, let's see how to pass a variable number of keyword arguments.

```python
# 45_xxargs.py
def save_user(**user):
    print(user)

save_user(id=1, name="John", age=22)
```

Instead of passing arbitrary positional arguments, here we pass arbitrary keyword arguments. We get multiple key-value pairs in the output:

```
{'id': 1, 'name': 'John', 'age': 22}
```

The object you see in the output is called a dictionary. It's another complex data structure in Python.

When double asterisks (`**`) are used, you can pass multiple key-value pairs as arguments to the function. 

# Scope

Scope is a very important concept in programming. It refers to the region of the code where a variable is defined and accessible.

For example:

```python
# 46_scope.py
def greet(name):
    message = "a"
```

In the above example, you have the `message` variable. The scope of this variable is limited to the `greet` function, and it only exists inside the function. If you try to print the variable outside the function, it will show an error. The scope of `name` and `message` variables is the `greet` function.

These variables are referred to as local variables in this function. Local variables have a very short lifetime. When we run the `greet` function with any name given, the Python interpreter will allocate some memory, and the variables `name` and `message` will reference those memory locations. When we finish executing the `greet` function, eventually these variables get garbage collected, and Python releases the memory.

We also have global variables. A global variable can be used anywhere in the file, and it stays in memory for a longer period.

```python
# 46_scope.py
message = "a"  # global variable

def greet(name):
    global message
    message = "b"

greet("Mosh")
print(message)
# Output will be: b
```

In this example, we use the `global` keyword inside the function to modify the global variable `message`.

> Note: Global variables are generally discouraged. They might have side effects in other functions. Avoid them as much as you can.

# VS Code Tricks (Windows)

- To move the cursor from the beginning to the end of the line: simply press the End key.
- To move to the beginning of the line: press the Home key.
- To move to the beginning of the file: Ctrl + Home.
- To move a line up or down: press Alt + Up or Down arrow.
- To duplicate lines or multiple lines: Shift + Alt + Down arrow.
- To convert lines of code to comment: Ctrl + / (slash).

# VS Code Tricks (Mac)

- To move the cursor from the beginning to the end of the line: Function (fn) + Right arrow.
- To jump to the beginning of the line: Function (fn) + Left arrow.
- To go to the top of the file: Function (fn) + Up arrow.
- To go to the bottom of the file: Function (fn) + Down arrow.
- To move a line: Alt + Up arrow or Alt + Down arrow.

# Exercise: FizzBuzz

```python
# 48_exercise_and_solutions.py
def fizz_buzz(input):
    print(fizz_buzz(5))
```

Your task is to fill the code in between.
If the input we give is divisible by 3, it will return the string "Fizz". If the input is divisible by 5, it will return "Buzz". If the input is divisible by both 3 and 5, it will return "FizzBuzz". If the input is not divisible by 3 or 5, it will return that input number itself.

# Solution

```python
# 48_exercise_and_solutions.py
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(3))
```

# Debugging

Here you are going to study how to find and fix bugs in a program. Let's add a couple of statements after the function in the previous code:

```python
# 47_debugging.py
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    # return total  # (Suppose this line is commented out by mistake)

print("start")
multiply(1, 2, 3)
```

When you run this program, instead of 6 you get 1. So debugging techniques are used to find and fix this bug.

## Debugging in VS Code

- Open the debug panel.
- Select a debugging configuration (e.g., Python, Django, etc.).
- To start debugging, first add a breakpoint by pressing F9. This will run the application up to this point.
- To execute one statement at a time, use F10.
- Use Shift + F11 to step out of the function.

Debugging is an essential skill to find and fix bugs in your code efficiently.

