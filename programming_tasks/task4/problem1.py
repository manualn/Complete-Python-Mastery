# 1.Count Length of a String Without len() 
# input a word
text = input("enter a word: ")
# define a function 
def count_length(text):
    count = 0
    for ch in text:
        count += 1
    return count       
#print length of the word
print(count_length(text))


