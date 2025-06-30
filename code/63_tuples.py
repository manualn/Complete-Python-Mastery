point = (1, 2)
print(type(point))

point = (1, 2) + (3, 4)
print(point)

# Multiplication operator
point = (1, 2) * 3
print(point)

point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)


point = (1, 2, 3)
print(point[0])
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exist")