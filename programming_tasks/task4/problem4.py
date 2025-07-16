# 4.Check if a Word is a Palindrome
# Ask to input word
x = input("enter a word: ")

# Define a function to check palindrome
def palindrome(x):
    l = len(x)  # Take the length of word
    for i in range(l):
        if (x[i] != x[l-1-i]): # Check the characters from start and end
            return False # If any mismatch return false
    return True # Otherwise Its a palindrome
        
# Print the result
print(f"Output: {palindrome(x)}")