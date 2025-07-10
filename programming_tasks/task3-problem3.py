# 3. Count Digits in an Integer (No Strings Allowed)
# input a number
num = int(input("enter a number: "))

# define a function to count digits
def count_digits(num):
    if num == 0:
        return 1
    count = 0
    while num>0:
        num = num // 10
        count += 1
    return count

print(count_digits(num))
