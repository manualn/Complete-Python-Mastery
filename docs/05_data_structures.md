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

