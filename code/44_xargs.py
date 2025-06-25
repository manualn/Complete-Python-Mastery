def multiply(x, y):
    return x * y

multiply(2, 3)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))