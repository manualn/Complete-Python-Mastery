# ALGORITHM
# 1)Start

# 2)Create an empty list lst to store numbers.

# 3)Repeat steps 4–5 for i from 1 to 10:
# 4)Ask the user to enter a number.
# 5)Convert the input to an integer and append it to lst.
# 6)Add the numbers to the empty list
# 7)Define a function classify_numbers that:
# 8)Create a dictionary counts with keys: "even" = 0,"odd" = 0, 
#  "positive" = 0, "negative" = 0

# 9)Start with the For loop that goes through each number in lst:
# 10)Set an if condition such that If number % 2 == 0, 
#  add the count of "even" by 1, else add the count of "odd" by 1.
# 11)Another if condition such that If number > 0, add the count of 
#  "positive" by 1.
# 12)Or Else if number < 0, increment "negative" by 1.
# 13)Return counts.

# 14)Call classify_numbers(lst) and pass the list through it and 
#  store it in result
# 15)Print the result.
# 16)End


lst = []
for i in range(1,10):
    num = int(input(f"Enter number {i}: "))
    lst.append(num)

def classify_numbers(lst):
    counts = {
        'even': 0,
        'odd': 0,
        'positive': 0,
        'negative': 0
    }

    for num in lst:
        if num % 2 == 0:
            counts['even'] += 1
        else:
            counts['odd'] += 1
        
        
        if num > 0:
            counts['positive'] += 1
        elif num < 0:
            counts['negative'] += 1
        

    return counts

result = classify_numbers(lst)
print(result)