# 9. Count words in a sentence
sentence = input("Enter a sentence: ")

# Define a function to count words in the sentence
def count_words(sentence):
    count = 0
    for word in sentence:
        if (word == " "):
            # When there is a space, it means the 
            # current word is complete
            count += 1 # count it as one
    return count + 1

# Print the result
print(f"Word count: {count_words(sentence)}")

        

