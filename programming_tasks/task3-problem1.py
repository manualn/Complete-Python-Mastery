# 1.Count Length of a String Without len() 
text = input("enter a word: ")
def count_length(text):
    count = 0
    for ch in text:
        count += 1
    return count       

print(count_length(text))


