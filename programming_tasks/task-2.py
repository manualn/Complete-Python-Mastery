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
    print("x is a palindrome")
else:
    print("x is not a palindrome")