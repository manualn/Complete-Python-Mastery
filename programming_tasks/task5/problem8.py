#ALGORITHM
# 1) Start
# 2) Input a sentence and store it in a variable called sentence
# 3) Define a function called count_capital_words
# 4) Create an empty list called result
# 5) Split the input sentence and store in a variable called words
# 6) Set a loop that goes through each character in words
# 7) If condition is set in a way that if first letter of the word is uppercase then add it to the empty list result
# 8) Repeat step 7 for the next word
# 9) Return the result
# 10)Call the function count_capital_words and pass the variable sentence through it and store it in a variable called uppercase_words
# 11)Print the length of uppercase_words
# 12)Also print the uppercase_words
# 13)End

sentence = input("Enter a sentence: ")

def count_capital_words(sentence):
    result = []
    words = sentence.split()
    for word in words:
        if word[0].isupper():
            result.append(word)
                
    return result

uppercase_words = count_capital_words(sentence)
print(f"Output: {len(uppercase_words)} capital words")
print(f"Output: {uppercase_words}")
