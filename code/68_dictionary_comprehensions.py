values = []
for x in range(5):
    values.append(x * 2)


values = [x * 2 for x in range(5)]
print(values)


# 68_dictionary_comprehensions.py
values = {}
for x in range(5):
    values[x] = x * 2

# Or using dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(values)


values = tuple(x * 2 for x in range(5))
print(values)