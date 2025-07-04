x = input("Enter a word: ")
x = x.replace(" ", "")
x = x.replace(".", "")
x = x.replace(",", "")
x = x.lower()
l = len(x)
palindrome = True

for i in range(l):
    if (x[i] != x[l-1-i]):
        palindrome = False
        break
    
if (palindrome == True):
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")