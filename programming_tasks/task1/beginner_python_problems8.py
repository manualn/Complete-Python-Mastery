# 8. Reverse a Word
x = input("Enter a word: ")
l=len(x)
reverse = ""
for i in range(l):
    reverse += x[l-1-i]

print(reverse)