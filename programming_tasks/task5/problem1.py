#ALGORITHM
# 1) start
# 2) create an empty list to store input
# 3) ask the user to enter 5 words using loop
# 4) Store it in variable words 
# 5) Add it to the empty list
# 6) define a function called filter_words
#    7) Set an empty list called result
#    8) Set a variable called vowels to store vowels
#    9) store the length of words in l
#    10) For each word in the input list words:
#    11) Set a counter vowel_count to 0.
#    12) For each letter in the word:
#    13) If the letter is a vowel increase vowel_count by 1.
#    14) If the word has more than 4 characters and vowel_count is 2 or more:
#    15) Add the word to the result list.
#    16) Return the result list.
# 17) Call the filter_words function and pass words_list
# 18) Print the result
# 19) End


words_list = []
for i in range(1,6):
    words = input(f"enter word {i}: ")
    words_list.append(words)


def filter_words(words):
    vowels = set("aeiouAEIOU")
    result = []

    for word in words:
        vowel_count = 0
        for letter in word:
            if letter in vowels:
                vowel_count += 1
        if len(word) > 4 and vowel_count >= 2:
            result.append(word)

    return result

filtered = filter_words(words_list)


print(f"Words entered: {words_list}")
print(f"Filtered results: {filtered}")
