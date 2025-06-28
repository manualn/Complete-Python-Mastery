numbers = [1,2,3 ]
first, second, third = numbers
print(first)

numbers = [1,2,3,4,4,4,9]
first, second, *others = numbers
print(first)
print(*others)

first, *others, last = numbers
print(first, last)
print(*others)