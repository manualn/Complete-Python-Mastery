# Replace All Vowels in a Word with '*'
# 1)input a word and store it in variable called word
# 2)define a function called censor_vowels
# 3)set all vowels in a string and store it in variable called vowels
# 4)create an empty string called censored to store the result
# 5)Set a loop for each character char in word
# 6)Check If char in vowels using if function
# 7)If Yes, go to Step 9
# 8)or else, go to Step 10
# 9)Add "*" to censored then Go to Step 11
# 10)Add char to censored
# 11)Repeat Step 6 for the next character
#(if no characters left, go to Step 12)
# 12)Call censored_vowels function and pass word variable through it
# 13)Print censored word
# 14)End


word = input("Enter a word: ")

def censor_vowels(word):
    vowels = "aeiouAEIOU"
    censored = ""

    for char in word:
        if char in vowels:
            censored += "*"
        else:
            censored += char

    return censored

result = censor_vowels(word)
print(f"censored words: {result}")