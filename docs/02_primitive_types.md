# Variables 
Variables is one of the core concepts in programming. Variables are used to store data in computer's memory.  
Example: 
```python
#15_variables.py
students_count = 1000
print(students_count)
```
When you run this code, python intepreter will allocate some memory and store this number. This variable is the reference to that memory location. Variable is like a label to that location. This label can be used anywhere in the program to get access to that memory location and the data stored.  

Now going to types of data, there are several kinds of data. In this chapter you are going to study built-in primitive types in Python. Primitive types can be numbers, booleans and strings

### Numbers
- Whole number is refered to as integers in programming language.
- Numbers with decimal points are called float.  
Example:
```python 
# 15_variables.py
rating = 4.99
```
### Booleans
- Boolean values can either be True or False  
Example:
```python
# 15_variables.py
is_published = True
```
#### Note:
Python is case sensitive language. i.e, Lowercase and Uppercase characters have different meanings. So boolean value should start with uppercase letter.
### String
Strings are basically text and you should use quotes while using texts as string in python.  
Example: 
```python
# 15_variables.py
course_name = "Python programming"
```

# Variable Names
- When writing Python code, it's important to use descriptive and meaningful variable names, like course_name instead of vague names like CN or C1. 
- Avoid "mystical" names that make the code hard to maintain and understand. 
- Short variable names like x, y, or z are only acceptable in specific contexts, such as math or coordinates. 
- Use lowercase letters consistently for variable names and seperate multiple words with underscores to improve readability. 
- Another best practice is to add spaces around the equal signs (=) when assigning values. Writing code without spaces looks messy and ugly. Your code should be clean and well formatted. 
- Autopep8 is the official style guide for python, promoting readability and consistent formatting.

``` python
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python programming"
```

# Strings 
### String Declaration

- Text in Python should be enclosed in quotes — single (' ') or double (" "); both work, but double quotes are more commonly used.

- Triple quotes (''' ''' or """ """) are used for multi-line strings, like email messages or formatted text blocks.
```python
# 17_strings.py
message = """
Hi John, 

This is mosh from codewithmosh


blah blahh balhh...
"""
```

### Getting String Length

- Use the built-in len() function to find the number of characters in a string.

- Example: len(course) returns 18 if course = "Python Programming".
```python
# 17_strings.py
course = "Python programming"
print(len(course))
```

### Functions in Python

- A function is a reusable block of code that performs a task.

- Functions are called using parentheses: function_name(arguments).

- Some functions require arguments (inputs), like len(course).

### Accessing Characters (Indexing)

- Strings are zero-indexed, meaning the first character has index 0.

- Use square brackets [] to access specific characters: course[0] returns 'P'.
```python 
# 17_strings.py
course = "Python programming"
print(course[0])
```
- Negative indexing starts from the end: course[-1] returns 'g'.
```python
# 17_strings.py
course = "Python programming"
print(course[-1])
```
### Slicing Strings

- string[start:end] returns characters from start to end.
```python 
# 17_strings.py

course = "Python programming"
print(course[0:3])
```

- Omitting start starts from the beginning: course[:3] → 'Pyt'.
```python
# 17_strings.py
course = "Python programming"
print(course[:3])
```

- Omitting end slices to the end: course[0:]
```python
# 17_strings.py
course = "Python programming"
print(course[0:])
```

- course[:] returns a copy of the original string.
```python
# 17_strings.py
course = "Python programming"
print(course[:])
```

### Key Reminders

- Use len() for string length.

- Use [] for indexing characters.

- Use [start:end] for slicing.


# Escape Sequences
In Python, text is written using either single quotes (' ') or double quotes (" ").

If you need to include a quote character inside your string (like a double quote in a double-quoted string), it causes a problem because Python thinks the string ends there.

✅ Example of an error: "Python "Programming" ← Python gets confused here.
```python
# 18_escape_sequences
course = "Python "Programming"
print(course)
```

✅ How to Fix It
Use the other type of quote:

'Python "Programming' → No conflict, so this works.
```python
# 18_escape_sequences
course = 'Python "programming"
print(course)
```
- Use a backslash ( \ ) to escape the quote:

"Python \"Programming" → The backslash tells Python to treat the next character as part of the string.
```python
# 18_escape_sequences
course = "Python \"Programming"
print(course)
```

- Escape Characters (Escape Sequences)
The backslash ( \ ) is an escape character, used to give special meaning to the character that follows.

### Common escape sequences:

- \ " → Inserts a double quote inside a double-quoted string.
👉 Example: "He said, \"Hello\"" → Output: He said, "Hello"

- \ ' → Inserts a single quote inside a single-quoted string.
👉 Example: 'It\'s okay' → Output: It's okay

- \ \ → Inserts one backslash (\).
👉 Example: "Path: C:\\Program Files" → Output: Path: C:\Program Files

- \n → Creates a new line in the string.


# Formatted strings

```python
# 19_formatted_strings1.py
first = "Mosh"
last = "Hamedani"
full = first + " " + last 
print(full)
```
Here first and last variable is concatenated. There is better and newer approach other than concatenation.i.e, formatted strings.

```python
# 19_formatted_strings2.py
first = "Mosh"
last = "Hamedani"
full = f"{first} {last}"
print(full)
```
We can call len here:

```python
# 19_formatted_strings2
full = f"{len(first)} {2+2}"
```
In formatted string you can put any valid expression.


# String method
In this chapter, you are going to study about a few essential functions available to work with strings. 
```python 
# 20_string_functions
course = "python programming"
print(len(course))
```
You learned about len function in previous chapters. This function is not only for string but also used generally.  
Few functions that are specific to strings are there in python. You can see the available functions below:

![syntax demo](/images/20_string_methods.png)

### Note:
Everything in python is an object and every object has functions (also called methods) that you can access through dot notation.  

Lets look at some functions: 
- This function is for making all letters uppercase.
```python
# 20_string_methods
course = " python programming "
print(course.upper())
```
- This function if for making all letters lowercase
```python
# 20_string_methods
course = " python programming "
print(course.lower())
```
- This function is to make the first letter capital
```python
# 20_string_methods
course = " python programming "
print(course.title())
```
- This function is to remove white spaces in the string
```python
# 20_string_methods
course = " python programming "
print(course.strip())
```
- This function is to remove white space from the left
```python
# 20_string_methods
course = " python programming "
print(course.lstrip())
```
- This function is to remove white space from the right
```python
# 20_string_methods
course = " python programming "
print(course.rstrip())
```
- This function is to find index 
```python
# 20_string_methods
course = " python programming "
print(course.find("pro"))
```
- This function is to replace letters.
```python
# 20_string_methods
course = " python programming "
print(course.replace("p","j"))
```
- This function is to check whether certain string is present in the given string
```python
# 20_string_methods
course = " python programming "
print("pro" in course)
print("swift" not in course)
```


# Numbers
There are three types of numbers in python.
1. Integers (x = 1)
2. Floats (x= 1.1)
3. Complex numbers (x = 1+2j)

For all these types of numbers, python have standard arithmetic operations that you have studied in maths. 
1. Addition
2. Subtraction
3. Multiplication
4. Division

```python 
# 21_numbers.py
print(10+3)
print(10-3)
print(10*3)
print(10/3)
```
### Divisions are many types:
- If you use slash you get a floating point
- If you want an integer use double slashes
- If you want remainder use modulus 

```python
# 21_numbers.py
print(10//3)
print(10%3)
print(10**3)
```
** is used to get exponent.

- There is a special operator called augmented assignment operator 
```python
# 21_numbers.py
x = 10
x = x+3
or
x+=3 
```
Here addition is used in augmented operator. ANy operator can be used instead.

# Working with numbers
Studying about some built in functions in this chapter.
1. Round  
To round a number  
Example: 
```python 
# 22_Working_with_numbers.py
print(round(2.9))
```
2. ABS  
It returns absolute value of a number.  
Example:
```python
# 22_Working_with_number.py
print(abs(-2.9))
```

- Math module can be used if you want to write a program that involves complex mathematical calculations. 
```python
# 22_Working_with_number.py
import math
print(math.ceil(2.2))
```
Ceil used for ceiling number.  
Go to the link [python 3 math module](https://docs.python.org/3/library/math.html)


# Type conversion
Here you are studying another useful built-in function. The input function is used to get input from the user.

```python
# 23_type_conversion.py
x = input("x: ")
y = x + 1
```

Don't run this code in the code runner extension because it will, by default, run your program in the output window, which is read-only.

So, open your terminal, type "python", and enter a value like 1.
You will get a "TypeError".

When you run "y = x + 1", the expression will look like "1" + 1.

Since these are two very different types, they cannot be concatenated.

Therefore, it has to be converted. So:

```python
# 23_type_conversion.py
# int(x)
# float(x)
# bool(x)
# str(x)
# these all can be used.
```

Let's type:

```python
# 23_type_conversion.py
x = input("x: ")
print(type(x))
# y = 2 + 1
```

"type" is another built-in function used to pass an object or an argument, and it returns its type.

```python
# 23_type_conversion.py
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
```

Anything of these used
-  0
-  ""
- None
- in boolean context are considered false.
- Anything other than this is true.

```python
# 23_type_conversion.py
bool(0)      # False
bool(1)      # True
bool(-1)     # True
bool(5)      # True
bool("a")    # True
bool("False") # True
``` 


# Quiz 2
### Question 1
What are the primitive types in Python?

**Answer:** Strings, numbers, and booleans.

---

### Question 2
```python
# 24_quiz.py
fruit = "Apple"
print(fruit[1])
```
What is the output?

**Answer:** The second character, which is 'p'.

---

### Question 3
```python
# 24_quiz.py
10 % 3
```
What is the result of this expression?

**Answer:** 1

---

### Question 4
```python
# 24_quiz.py
print(bool("False"))
```
What is the output?

**Answer:** True 


