# 4. Print Only the Vowels from a Word
n = input("enter a word: ")
l = len(n)
for m in range(l):
    if n[m].lower() in ("a", "e", "i", "o", "u"):
        print("found vowel: ", n[m])