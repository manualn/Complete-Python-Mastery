# 10.Find the Longest Word in a List 
text_list = [] # empty list to add the input words
# enter 5 words
for i in range(1,6):
    text = input(f"enter word {i}: ")
    text_list.append(text)

# define a function to count length of a word
def count_length(text):
    count = 0
    for ch in text:
        count += 1
    return count

# Find the longest word using count_length function
longest_word = text_list[0]
for word in text_list:
    if count_length(word) > count_length(longest_word):
        longest_word = word

# Print the result
print(f"Longest word: {longest_word}")
