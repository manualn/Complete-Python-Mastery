# Lists

In this section, we are looking into data structures in Python, which are really important when building real applications.

- Square brackets are used to define a list of a sequence of objects. In between, you can type any strings, numbers, booleans, or even a list itself.

```python
# 49_lists.py
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
```

Here, `matrix` is a two-dimensional list.

- How to create a list of 100 zeros:

```python
# 49_lists.py
zeros = [0] * 100
print(zeros)
```

- Using `*`, you can repeat the items in a list. Similarly, `+` is used to concatenate multiple lists.

```python
# 49_lists.py
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
```

- If you want to have a list of numbers like 0, 1, 2, 3, ..., 19, you can use the `list` function with `range`:

```python
# 49_lists.py
numbers = list(range(20))
print(numbers)
```

- You can also convert a string to a list of characters:

```python
# 49_lists.py
chars = list("hello world")
print(chars)
```

- The number of items in a list can be obtained using the `len` function:

```python
# 49_lists.py
print(len(chars))
```

# Accessing Items in Lists

You can access individual items in a list using square brackets:

```python
# 50_accessing_items.py
letters = ["a", "b", "c", "d"]
print(letters[0])   # returns first item
print(letters[-1])  # returns last item
```

You can also change the value of an item in a list:

```python
# 50_accessing_items.py
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters)
```

# Slicing Lists

You can do slicing of lists as well:

```python
# 50_accessing_items.py
print(letters[0:3])  # returns items from index 0 to 2
print(letters[:3])   # returns items from start to index 2
```

While slicing, you can also pass a step to return every second or third element:

```python
# 50_accessing_items.py
print(letters[::2])  # returns every second element
```

You can use slicing with numbers too:

```python
# 50_accessing_items.py
numbers = list(range(20))
print(numbers[::2])   # even numbers: 0, 2, 4, ...
print(numbers[::-1])  # reversed list
```

# List Unpacking

Sometimes you may need to separate items from a list and assign them to different variables:

```python
# 51_list_unpacking.py
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
```

There is a cleaner way to achieve the same result, called list unpacking:

```python
# 51_list_unpacking.py
numbers = [1, 2, 3]
first, second, third = numbers
```

Here, we summarized the same code into one line. This is called list unpacking.

The only condition is that the number of variables (first, second, third) should be equal to the number of items in the list.

What if the list has many more items, but you only care about the first two?

```python
# 51_list_unpacking.py
numbers = [1, 2, 3, 4, 4, 4, 4, 4]
first, second, *others = numbers
print(first)
print(others)
```

In the above case, first and second items are unpacked, and the rest will be stored in a separate list called others.

If you only care about the first and last item:

```python
# 51_list_unpacking.py
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *others, last = numbers
print(first, last)
print(others)
```

The asterisk is used while you are packing items into a separate list during unpacking.

# Looping Over Lists

You can loop over lists using a for loop:

```python
# 52_looping_over_lists.py
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)
```

If you want to get the index of each item, use the built-in function `enumerate`, which returns an enumerated object (an iterable of tuples):

```python
# 52_looping_over_lists.py
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)
```

You can unpack the tuple to get both the index and the value:

```python
# 52_looping_over_lists.py
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)
```

The for loop can be used to iterate over lists.

# Adding or Removing Items

You can add and remove items in a list using various methods:

```python
# 53_adding_or_removing_items.py
letters = ["a", "b", "c"]
# Add
letters.insert(0, "d")
letters.append("e")
print(letters)

# Remove
letters.pop(0)
print(letters)
letters.remove("b")
del letters[0:2]
print(letters)
```

- `letters.pop(0)` is used when you know the index of the item to be removed.
- If you don't know the index, use `letters.remove("b")`.
- If you want to remove a range of items, use `del letters[0:3]`.
- The `pop` method will only remove one item from the list.
- To clear all items in the list, use `letters.clear()`.

# Finding Items

Sometimes you may need to find the index of a given object:

```python
# 54_finding_items.py
letters = ["a", "b", "c"]
print(letters.index("a"))
print(letters.index("d"))  # This will raise a ValueError if 'd' is not in the list
```

If you try to get the index of a letter that doesn't exist, you will get a ValueError. So, first check if the object exists:

```python
# 54_finding_items.py
letters = ["a", "b", "c"]
if "d" in letters:
    print(letters.index("d"))
```

You can also check how many times a letter appears in the list:

```python
# 54_finding_items.py
print(letters.count("a"))
```

# Sorting Lists

You can sort lists using the `sorted()` function or the `sort()` method:

```python
# 55_sorting_list.py
numbers = [3, 51, 2, 8, 6]
print(sorted(numbers, reverse=True))
```

To sort a list of tuples:

```python
# 55_sorting_list.py
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)
```

Note: `sort()` does not take positional arguments; only keyword arguments can be used.

# Lambda Functions

The code we used in the last section can be made cleaner using a lambda expression. The syntax is:

```python
key = lambda parameters: expression
```

For example, sorting a list of tuples by the second item:

```python
# 56_lambda_functions.py
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

items.sort(key=lambda item: item[1])
print(items)
```

When you run this code, you'll get the same result as before, but the code is more concise.

# Map Function

Suppose you want to transform a list of tuples into a list of numbers (e.g., prices):

```python
# 57_map_functions.py
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

prices = []
for item in items:
    prices.append(item[1])
print(prices)
```

There is a better way to achieve the same result using the `map` function:

- `map()` is a built-in function. It takes two parameters: a function and one or more iterables.
- The map function can take a lambda function and apply it to every item of the iterable.

```python
# 57_map_functions.py
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]
prices = list(map(lambda item: item[1], items))
print(prices)
```

# Filter Function

If you want to filter a list to get the items with price greater than or equal to 10:

```python
# 58_filter_functions.py
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]
x = list(filter(lambda item: item[1] >= 10, items))
print(x)
```

# List Comprehensions

Map and filter functions are very useful in Python and are often used by developers from a functional programming background. However, list comprehensions provide a more Pythonic way:

```python
# 59_list_comprehensions.py
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]
prices = list(map(lambda item:item[1], items))
prices = [item[1] for item in items]
filtered = list(filter(lambda item: item[1]>=10, items))
filtered = [item for item in items if item[1] >= 10]
```

# Zip Function

If you have two lists and want to combine them:

```python
# 60_zip_functions.py
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))
```

The zip function is used to combine multiple lists. Here, the string "abc" is spread across multiple tuples in the resulting list.

# Stacks

A stack is a common data structure that represents a stack of items in the real world. It follows the LIFO (Last In, First Out) principle.

Start with an empty stack:

```python
# 61_stacks.py
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
```

- The `append` method is used to add an item on top of the stack.
- When the user presses the back button, you should remove the last item in the list using `pop`.
- `browsing_session[-1]` returns the last item.

Earlier, we studied about falsy values. The number 0, empty string, and empty list are falsy values. If you apply the `not` operator to an empty list, you'll get boolean `True`:

```python
not []  # True
```

To check whether a stack is empty or not:

```python
# 61_stacks.py
if not browsing_session:
    # stack is empty
else:
    print(browsing_session[-1])
```

# Queues

A queue has a FIFO (First In, First Out) behavior. For example, a queue of people:

```python
# 62_queues.py
[1, 2, 3]
```

In a queue, when removing an item, you have to remove one, then two, then three. Every time we remove an item from the beginning of a list, the other remaining items' positions must be shifted towards the left. In such situations, a `deque` object can be used.

We have to call the `deque` function from the module `collections`:

```python
# 62_queues.py
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

if not queue:
    print("empty")
```

`not` can be used to check whether your list is empty or not.

# Tuples

A tuple is basically a read-only list. It can be used to contain a sequence of objects, but the sequence cannot be modified; you cannot add a new object to it or remove an existing object.

When two objects are separated by a comma, Python considers it as a tuple. Even parentheses are not necessary.

To define an empty tuple, use empty parentheses:

```python
# 63_tuples.py
point = (1, 2)
print(type(point))

point = (1, 2) + (3, 4)
print(point)

# Multiplication operator
point = (1, 2) * 3
print(point)
```

To convert a list to a tuple, use the `tuple` function:

```python
# 63_tuples.py
point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)
```

Similar to lists, we can access individual items of tuples:

```python
# 63_tuples.py
point = (1, 2, 3)
print(point[0])
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exist")
```

Tuples are immutable; they cannot be mutated or changed.

# Swapping Variables

```python
# 64_swapping_variables.py
x = 10
y = 11
z = x
x = y
y = z
print("x", x)
print("y", y)
```

Output will be:
```
x 11
y 10
```

Here, x is changed to 11 and y is 10. In Python, we can swap the value of two variables using one line of code instead of these three lines:

```python
# 64_swapping_variables.py
x, y = y, x
```

Parentheses are not necessary.

# Arrays

If you're dealing with a large sequence of numbers, Python has a more efficient datatype called array. Arrays take little memory and perform faster.  
- array() - first parameter is called a type code which is strings determines the type objects in your array.  
Search for [python 3 typecode](https://docs.python.org/3/library/array.html) in google to study more about arrays.  
- numbers.append to append a number to the end of list.  
- number.insert to add a number in a specific index.  


To use arrays in Python, first import it from the array module:

```python
# 65_arrays.py
from array import array
numbers = array("i", [1, 2, 3])
numbers[0] = 4.0  
# This will raise an error because arrays are typed
```

- Arrays are typed, so every object should get integers (or the specified type). If you try to put a floating number or any other type of object, you will get an error.
- Use arrays when dealing with large sequences of numbers. Otherwise, use lists and tuples.

# Sets

A set is a very useful data structure in Python, which is a collection with no duplicates:

```python
# 66_sets.py
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)
```

- Curly braces are used while defining sets.
- We can get the union of two sets by using the vertical bar:

```python
# 66_sets.py
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first | second)
```

- To get intersection, use `&` between first and second sets.
- To get difference, use `-` sign.
- `^` symbol is used to get objects that are present in either first or second but not both.
- Items in a set are not sequence, so you cannot access them using an index. So `print(first[0])` will give an error.

```python
# 66_sets.py
print(first & second)
print(first - second)
print(first ^ second)
if 1 in first:
    print("yes")
```

# Dictionaries

A dictionary is a very powerful data structure. It's a collection of key-value pairs:

```python
# 67_dictionaries.py
point = {"x": 1, "y": 2}
```

There is a `dict` function similar to `list()`, `tuple()`, and `set()` functions:

```python
# 67_dictionaries.py
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
print(point)
# We can add a new key
point["z"] = 20
print(point)
```

While reading a value, if we use an invalid key, you will get an error:

```python
# 67_dictionaries.py
print(point["a"])  # KeyError
```

To check existence of a key:

```python
# 67_dictionaries.py
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
```

- Use get method
- Delete method

```python
# 67_dictionaries.py
del point["x"]
print(point)
```

How to loop over a dictionary:

```python
# 67_dictionaries.py
for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

# We can unpack the tuple right here
for key, value in point.items():
    print(key, value)
```

# Dictionary Comprehensions

An empty list is given, then iterating over a range, in each iteration you get x multiplied by 2 and add it to our list:

```python
# 68_dictionary_comprehensions.py
values = []
for x in range(5):
    values.append(x * 2)
```

This code above can be written more simply:

```python
# 68_dictionary_comprehensions.py
values = [x * 2 for x in range(5)]
```

Comprehensions can be not only in lists but also in sets and dictionaries.

If the square brackets are replaced by curly brackets, you will get a set:

```python
# 68_dictionary_comprehensions.py
values = {x * 2 for x in range(5)}
print(values)
```

You can use comprehension expressions to create dictionary objects:

```python
# 68_dictionary_comprehensions.py
values = {}
for x in range(5):
    values[x] = x * 2

# Or using dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(values)
```

Comprehensions for tuples: change curly brackets into parentheses:

```python
# 68_dictionary_comprehensions.py
values = tuple(x * 2 for x in range(5))
print(values)
```

# Generator Expressions

Generator expressions provide a memory-efficient way to work with large data sets or infinite streams of data. Unlike list comprehensions, which generate and store all items in memory, generator expressions generate items on the fly, yielding one value at a time as you iterate over them.

## List Comprehension Example

```python
# 69_generator_expressions.py
values = [x * 2 for x in range(10)]
for x in values:
    print(x)
```

When you run this program, the output will be even numbers from 0 to 18. However, all values are stored in memory at once.

## Why Use Generators?

If you're working with large data sets or infinite streams of data, storing all values in memory can be inefficient or even impossible. In such situations, you can use generator objects.

- Generator objects are iterable just like lists. On each iteration, they generate (yield) a new value.
- They don't store all the values in memory; instead, they generate a new value in each iteration.

## Creating a Generator Expression

To change a list comprehension to a generator expression, replace the square brackets with parentheses:

```python
# 69_generator_expressions.py
values = (x * 2 for x in range(10))
for x in values:
    print(x)
```

## Memory Usage Comparison

You can compare the memory usage of a generator expression and a list comprehension using the `getsizeof` function from the `sys` module:

```python
# 69_generator_expressions.py

from sys import getsizeof

# Generator expression
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))

# List comprehension
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
```

If you use a list comprehension here, you would end up with a list of 100,000 items, which takes much more memory compared to a generator object (which only takes about 120 bytes).

## Summary

- Use generator expressions when you need to iterate over large or infinite data sets without storing all values in memory.
- Use list comprehensions when you need to access all items multiple times or require random access.

# Unpacking Operator

Here you are going to study how the unpacking operator works.

For example:

```python
# 70_unpacking_operator.py
numbers = [1, 2, 3]
print(numbers)
```
The output will be:
```
[1, 2, 3]
```

If you want each number separately without brackets, you can use the unpacking operator:

```python
# 70_unpacking_operator.py
numbers = [1, 2, 3]
print(*numbers)
```
The output will be:
```
1 2 3
```

Another example:

```python
# 70_unpacking_operator.py
values = list(range(5))
print(values)
```
The output will be:
```
[0, 1, 2, 3, 4]
```

In the above, we can use the unpacking operator instead of `list`:

```python
# 70_unpacking_operator.py
values = [*range(5), *"Hello"]
print(values)
```
The output will be:
```
[0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']
```

Using this operator, we can combine multiple lists:

```python
# 70_unpacking_operator.py
first = [1, 2]
second = [3]
values = [*first, "a", *second]
print(values)
```
The output will be:
```
[1, 2, 'a', 3]
```

## Unpacking Dictionaries

You can also use the unpacking operator with dictionaries:

```python
# 70_unpacking_operator.py
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
```
The output will be:
```
{'x': 10, 'y': 2, 'z': 1}
```

We can use unpacking operators `*` and `**` to take out individual values in any operation.


# Exercises

Here is the question: count the frequency of each character in a string.

```python
# 71_exercises.py
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
```

This code will output a dictionary where the keys are characters and the values are the number of times each character appears in the sentence.

## Better Way to Print the Dictionary

When the dictionary is large or you want a more readable output, you can use the `pprint` module (pretty-print) to display the dictionary in a cleaner format:

```python
# 71_exercises.py
from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)
```

The `pprint` function prints the dictionary in a more readable, nicely formatted way, especially when the dictionary is large or has complex data.

Next step is to sort this dictionary by frequency of characters. Here we take out each key value pair and convert it into tuple.

```python
# 71_exercises.py
from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Sort the dictionary by frequency (value)
print(sorted(char_frequency.items(), key=lambda kv: kv[1]))
```

### Output

```
[('h', 1), ('v', 1), ('T', 1), ('q', 1), ('u', 1), ('w', 1), ('m', 2), ('n', 2), ('o', 2), ('s', 3), ('i', 3), (' ', 5), ('t', 3), ('e', 4), ('c', 2), ('a', 2), ('r', 2)]
```