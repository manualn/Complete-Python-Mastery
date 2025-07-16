# 2. Count Elements in a List Without len() 
# empty list to add the input numbers
list = [] 

# loop for asking user to input 5 numbers
for i in range(1,6):
    x = int(input("enter a number: "))
    list.append(x)

# define a function to count elements in the list
def count_elements(list):
    count = 0
    for number in list:
        count += 1
    return count       

# print
print(count_elements(list))