items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]
x = list(filter(lambda item: item[1] >= 10, items))
print(x)