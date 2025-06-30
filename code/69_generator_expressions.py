values = [x * 2 for x in range(10)]
for x in values:
    print(x)


values = (x * 2 for x in range(10))
for x in values:
    print(x)


from sys import getsizeof

# Generator expression
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))

# List comprehension
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))