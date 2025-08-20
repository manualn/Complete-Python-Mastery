# 9.Word-Level Frequency Counter
# 1)Start
# 2)Input a sentence and store it in a variable called sentence
# 3)define a function called word_frequency
# 4)Split the sentence at space and store it in words
# 5)set a empty dictionary and name it as freq
# 6)Start with a for loop that goes through each word
# 7)if the word is in freq add 1 or else add the word and set 
#   the count as one
# 8)Repeat it for the next word
# 9)Return freq
# 10)Call the function word_frequency and pass the sentence through 
#   it and store it in variable called result
# 11)Print the result 
sentence = input("Enter a sentence: ")

def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

result = word_frequency(sentence)
print(f"Output: {result}")