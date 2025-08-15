# ALGORITHM
# 1)Start
# 2)Ask for input sentence from the user.
# 3)Split the sentence into words.
# 4)Create an empty list called mirrored_words to store reversed
#  words.
# 5)Create a for loop that goes through each word in the sentence:
# 6)Start with an empty string called reversed_word
# 7)Start a for loop that goes through each letter in the word
# 8)Add the letter to the front of the reversed string.
# 9)Append the reversed word to the empty list called mirrored_words.
# 10)Return the joined reversed words back into a single string 
# with spaces.
# 11)Call the function and pass the input sentecne through it and 
# store it in a variable called result.
# 12)Print the result
# 13)End

sentence = input("Enter a sentence: ")

def mirror_words(sentence):
    words = sentence.split()
    mirrored_words = []
    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        mirrored_words.append(reversed_word)

    return " ".join(mirrored_words)

result = mirror_words(sentence)
print(result)