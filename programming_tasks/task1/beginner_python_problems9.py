# 9. Sum of Digits 
x = input("enter a number: ")
l= len(x)
sum = 0
for i in range(l):
    sum += int(x[i])

print(sum)