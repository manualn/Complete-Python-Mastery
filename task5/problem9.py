#ALGORITHM
# 1)Start
# 2)Create an empty list named words
# 3)start with a for loop to input 5 words
# 4)Add these words into the empty list words
# 5)Define the function named longest_word_length that takes the 
# words list as input
# 6)Inside the function, use the max() function with key=len to 
# find the longest word in the list.
# 7)Return the longest word from the function.
# 8)Call the function longest_word_length and pass  list 
# words and store it in a variable longest_word.
# 9)Print longest_word
# 10)Print the length of longest word
# 11)End

words = []
for i in range(1,6):
    word = input(f"Enter a word{i}: ")
    words.append(word)

def longest_word_length(words):
    longest = max(words, key=len)
    return longest

longest_word = longest_word_length(words)
print(longest_word)
print(f"length of longest word is {len(longest_word)}")