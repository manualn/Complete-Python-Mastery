# 1. Show How a Sum Builds Up Step-by-Step
n = int(input("enter a number: "))
sum = 0
for i in range(n+1):
    sum += i
    print(f"sum = sum + {i} -> {sum}")

print(f"final sum = {sum}")