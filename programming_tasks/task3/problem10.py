# 10. Make a List of Letters from a Word
x = input("Enter a word: ")
letter_list = []
l = len(x)
for i in range(l):
    letter_list.append(x[i])

print(f"letter list: {letter_list}")
