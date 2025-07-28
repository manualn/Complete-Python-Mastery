# ALGORITHM
# 1) ask user to input a word
# 2) Define a function char_frequency
# 3) Create an empty dictionary called freq
# 4) create a for loop  that goes through each character in word
# 5) For each char in word, repeat Steps 6–8:
# 6) If char is already in freq, increase its count by 1
# 7) or else, add a new char to freq dictionary with a count of 1
# 8) Go back to Step 5 for the next character
# 9) After the loop ends, store the dictionary in a variable result
# 10) Print output
# 11) End

word = input("Enter a word: ")

def char_frequency(word):
    freq = {}
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

result = char_frequency(word)
print(f"Output: {result}")


