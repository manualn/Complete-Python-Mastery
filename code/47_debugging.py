def multiply (*numbers):
    total = 1
    for number in numbers:
        total *= number 
    return total 


print("start")
multiply(1,2,3)