#ALGORITHM
# 1)Start
# 2)Create an empty list named words
# 3)start with a for loop to input 5 words
# 4)Add these words into the empty list words
# 5)Ask user to enter a letter and store it in a variable letter
# 6)Define the function named words_with_letter that takes words and letter as input
# 7)Inside the function create an empty list called result
# 8)Start with a for loop that goes through each word in the words list
# 9)If the letter is found in the word add the word to the result list
# 10)To make it case insensitive convert the letter and word to lower case
# 11)if the letter is not found go to the next word
# 12)return the result
# 13)Call the function and pass the words list and input letter in it and store it in a variable called filtered_list
# 14)Print filtered_list
# 15)End

words = []
for i in range(1,6):
    word = input(f"enter a word {i}: ")
    words.append(word)

letter = input("Enter a letter: ")

def words_with_letter(words, letter):
    result = []
    for word in words:
        if letter.lower() in word.lower():
            result.append(word)
    return result

filtered_list = words_with_letter(words, letter)
print(filtered_list)