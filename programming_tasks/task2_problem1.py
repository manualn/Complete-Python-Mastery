n = int(input("enter a number: "))
sum = 0
for i in range(n+1):
    sum += i
    print(f"sum = sum + {i} -> {sum}")