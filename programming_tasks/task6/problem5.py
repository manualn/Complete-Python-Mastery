# 1)Start
# 2)Ask for an input sentence and store it in variable sentence
# 3)Define a function called count_pattern
# 4)Set a dictionary called count where set capital_start, 
# vowel_end and has_digit as zero
# 5)Split the sentence into words and store it in words
# 6)Create a set containing vowels and store it in variable
# named vowels
# 7)Create a set containing digits and store it in digits
# 8)Set a for loop that goes through each word in the sentence
# 9)Set an if condition to check whether first letter of each
# word is uppercase if yes then increase count of capital_start to 1
# 10)Set an if condition to check whether last letter of each word
# is vowel if yes then increase the count of vowel_end by 1
# 11)Set a for loop that goes through each number in the digits
# 12)Set an if condition to check whether any number is there in 
# word if yes then increas the count of has_digit by 1
# 13)Return count
# 14)Call the function count_pattern and pass the sentence through 
# it and store it in variable called result
# 15)Print the result 
# 16)End


sentence = input("Enter a sentence: ")

def count_pattern(sentence):
    count = {
        'capital_start': 0,
        'vowel_end': 0,
        'has_digit': 0
    }
    words = sentence.split()
    print(words)
    vowels = ("aeiouAEIOU")
    digits = ("1234567890")
    for word in words:
        if word[0].isupper():
            count['capital_start'] += 1
        if word[-1] in vowels:
            count['vowel_end'] += 1
        for d in digits:
            if d in word:
                count['has_digit'] += 1

    return count

result = count_pattern(sentence)
print(result)