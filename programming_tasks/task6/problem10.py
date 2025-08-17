# 1)Start
# 2)Ask the user to input a sentence and store it in variable sentence
# 3)Define a function called most_common_char
# 4)Replace the spaces between words
# 5)Set an empty dictionary called freq
# 6)Set a for loop that goes through each character in the sentence
# 7)If char in freq then increase the count of freq[char] by one
# 8)Or else set freq[char] as one
# 9)To get the most frequent letter use the max function and store it in freq_letter
# 10)Return freq_letter
# 11)Call the function and pass sentence through the function and store it in result
# 12)Print the result
# 13)End

sentence = input("Enter a sentence: ")

def most_common_char(sentence):
    sentence = sentence.replace(" ", "")

    freq = {}
    for char in sentence:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    freq_letter = max(freq, key=freq.get)
    return freq_letter

result = most_common_char(sentence)
print(result)
