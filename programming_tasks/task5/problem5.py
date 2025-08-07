#ALGORITHM
# 1)Start
# 2)Input comma seperated numbers and store it in a variable
# called input_number
# 3)Convert the input numbers into a list of functions
# 4)Define a function second_largest to find second largest number
# 5)Set largest and second as 0
# 6)Start with a for loop that goes through each number in the list
# 7)If the number is bigger than the current biggest, then
# second = largest (previous biggest becomes second biggest)
# and largest = num (new biggest found)
# 8)If it is not equal to largest and larger than the second 
# biggest, second = num
# 9)Return the second
# 10)Call function and pass the numbers list in it and store it in 
# variable called secnd_large
# 11)Print secnd_large
# 12)End

input_number = input("Enter comma-separated numbers: ")

numbers = list(map(int, input_number.split(",")))

def second_largest(numbers):
    largest = 0
    second = 0
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and num > second:
            second = num

    return second

secnd_large = second_largest(numbers)
print(secnd_large)
