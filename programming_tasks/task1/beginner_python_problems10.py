# 10. Number Repetition Counter
numbers = []

for i in range(1,6):
    num = int(input("enter a number: "))
    numbers.append(num)

search_number = int(input("Enter a number to search: "))


count = 0
for num in numbers:
    if num == search_number:
        count += 1

print(search_number ,"appeared", count ,"times")
