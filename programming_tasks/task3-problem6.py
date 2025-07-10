# 6. Count Vowels in a Word
# input a word
word = input("enter a word: ")
# get the length of the word
l = len(word)

# define a function to count the number of vowels in the word
def count_vowels(word):
    count = 0
    for m in range(l):
        if word[m].lower() in ("a", "e", "i", "o", "u"):
            count += 1
    return count
    
# Print the vowel count
print(f"Vowel count: {count_vowels(word)}")