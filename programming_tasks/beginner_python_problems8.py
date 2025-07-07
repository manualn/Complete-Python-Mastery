# 8. Reverse a Word
x = input("Enter a word: ")
reverse = ""
for i in range(len(x)):
    reverse += x[len(x)-1-i]

print(reverse)