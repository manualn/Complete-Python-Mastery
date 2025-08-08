# 7.Find All Words with More Vowels Than Consonants

# 1) start
# 2) create an empty list to store input
# 3) ask the user to enter 5 words using loop
# 4) Store it in variable words 
# 5) Add it to the empty list
# 6) define a function called vowel_dominant_words
# 7) Set a variable called vowels to store vowels
# 8) Set a variable called consonants to store consonants
# 9) Set vowel_count and consonants_count to zero
# 10)start a for loop that goes through each character in word
# 11)Set an if condition to check if the character is in vowel list and
#    if yes then count 1 and add it to vowel_count
# 12)Set an elif condition to check if the character is in consonants
#    list and if yes then count 1 and add it to consonants_count
# 13)Compare the vowel_count and consonants_count
# 14)Set an empty list and name it vowel_dominant_list
# 15)Then set a for loop that goes through each word in the words_list
# 16)if vowel_dominant_words are there then add it to the empty list
# 17)Print the vowel_dominant_wordlist
# 18)End

words_list = []
for i in range(1,6):
    words = input(f"enter word {i}: ")
    words_list.append(words)

def vowel_dominant_words(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    vowel_count = 0
    consonants_count = 0

    for char in word:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonants_count += 1

    return vowel_count > consonants_count

vowel_dominant_wordlist = []
for word in words_list:
    if vowel_dominant_words(word):
        vowel_dominant_wordlist.append(word)

print(vowel_dominant_wordlist)