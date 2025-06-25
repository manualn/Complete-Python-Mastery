# Comparison operators
Comparison operators are used to compare values.  
Example:
```python
# 25_comparison_operators.py
10 > 3
10 >= 3
10 < 20
10 <= 20
10 == 10
10 == "10"
10 != "10"
```
- The output will be boolean values

```python
# 25_comparison_operators.py
"bag" > "apple" # True
"bag" == "BAG" # False

ord("b") # 98
```
- 98 is numerical representation of 'b'


# Conditional statements
```python
# 26_conditional_statements.py
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")
```
- An if statement is used when we have to program for any given conditions.
- When you use an if statement, always terminate it with a colon.  
- Remove the indentation to indicate the end of the if block.  
- If you have multiple conditions, use an elif statement.  
- And you can also have an else statement.


# Ternary Operator
The ternary operator is a conditional operator, that helps you for concisely expressing if-else statements in a single line of code

```python
# 27_ternary_operator.py
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)
```

- This can also be written in another way:

```python
# 27_ternary_operator.py
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
```

So, what we have here is called a Ternary operator. 


# Logical Operators
There are three logical operators in Python.

These operators are used to model more complex conditions.

- and
- or
- not

```python
# 28_logical_operators.py
high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
```

Here "or" can be given instead of "and".

Also "not" is used:

```python
# 28_logical_operators
high_income = False
good_credit = True
student = False

if not student:
    print("Eligible")
else:
    print("Not eligible")
```

We want neither high_income or good_credit should be true to be true so use parenthesis. Code given:

```python
# 28_logical_operators
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
``` 

# Short circuit evaluations
```python
# 29_short_circuit_evaluations
high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("eligible")
```

Result of the above if expression will always be false because one of the argument is false.

This is called short circuiting.

If "and" is changed to "or", then the expression becomes true.

In Python logical operators are short circuiting. 


# Chaper 30 - Chaining Comparison Operators
This is very powerful technique for writing clear code.

```python
# 30_chaining_comparison_operators.py
# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("eligible")
```

We write this same rule in maths like this:  
18 <= age < 65

This expression can be written same in Python. Rewrite it the above code as:

```python
# 30_chaining_comparison_operators.py
age = 22
if 18 <= age < 65:
    print("eligible")
```

This is called chaining comparison operators. 


# Quiz 3
```python
# 31_quiz.py
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
```

Answer: letter "c" will be printed on the terminal 


# For loops
At times you may need to repeat a task a number of times for that 'for' loop can be used.

```python
# 32_for_loops.py
print("Sending a message")
```

If you want to repeat this code multiple times use for loop.

```python
# 32_for_loops.py
for number in range(3):
    print("Attempt")
```

To know more about number, you can change the above code:

```python
# 32_for_loops.py
for number in range(3):
    print("Attempt", number)
```

Also try

```python
# 32_for_loops.py
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
```

Output will be
Attempt 1 .
Attempt 2 ..
Attempt 3 ...

Range function generates starting from 0 till the given number. To avoid that we can change the above code like this:

```python
# 32_for_loops.py
for number in range(1, 4):
    print("Attempt", number, number * ".")
```

Output will be same.

```python
# 32_for_loops.py
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
```

Output will be:
Attempt 1 .
Attempt 3 ...
Attempt 5 .....
Attempt 7 .......
Attempt 9 .........

"range(1, 10, 2)" here 1 is start, (1, 10) is range and 2 is the difference. 


# Chapter 33 For else
```python
# 33_for_else.py
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
```

Change "successful" to "false" and you can see the output varies.

For else is the combination of for loop with else clause. 


# Nested loops
Here one loop is put inside another loop.

```python
# 34_nested_loops.py
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
```

Output will be:
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
...

Here you can see two loops, first one is outer loop and second one is inner loop.  
In the first iteration x=0 and y=0.  
In the second iteration x=0 and y=1.  
In the third iteration x=0 and y=2.  
Now again going back to outerloop this repeats x=1 and y=0, x=1 and y=1. 


# Iterables
type() -> type of an object can be determined.

type(range()) -> range function returns the type of object in range.

```python
# 35_iterables.py
print(type(5))
print(type(range(5)))
```

A range object is iterable, which means you can use it in a for loop.  
Example: "for x in range(5):"

Ranges are not the only iterable objects in python, strings are also iterable.
Example:
```python
# 35_iterables.py
for x in "python":
    print(x)
```

Lists are also iterable.
Example:
```python
# 35_iterables.py
for x in [1, 2, 3, 4]:
    print(x)
``` 


# While loops
A while loop is used to repeat something as long as a given condition is true.

Example:
```python
# 36_while_loops.py
number = 100
while number > 0:
    print(number)
    number = number // 2
```

Here you are evaluating a condition and repeating tasks.

```python
# 36_while_loops.py
command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)
```

This code is to create a simple interactive program that keeps taking input from the user and repeating it until the user types "quit".

If you type "QUIT" instead of "quit", it will not work. As you learned before, python is case sensitive, so lowercase and uppercase have different numerical presentations.

If you want to run the program with "QUIT" also, change the code like this:

```python
# 36_while_loops.py
command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)
```

OR

Use command.lower() 


# Infinite loops
An infinite loop is a loop that runs forever. If the code you studied in the last chapter is changed in the given way:

```python
# 37_infinite_loops.py
command = ""
while True:
    command = input(">")
    print("ECHO", command)
```

Here "True" is always true, therefore this while loop will run forever.

So to jump out from this loop you need a "break" statement. For an infinite loop, there is no need to define the command.

Therefore:

```python
# 37_infinite_loops.py
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
```

You should be aware of infinite loops because they run forever and you should always know a way to jump out of it. If the program runs forever, it can cause issues with consuming memory and your program may run out of memory. 


# Exercise
**Question:**
Write a program to display even numbers from 1 to 10 and after that print this message: "We have 4 even numbers."

**Answer:**
```python
# 38_exercise.py
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")
``` 

