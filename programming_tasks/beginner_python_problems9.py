# 9. Sum of Digits 
x = input("enter a number: ")
sum = 0
for i in range(len(x)):
    sum += int(x[i])

print(sum)