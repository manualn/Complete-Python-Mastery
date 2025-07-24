letters = ["a", "b", "c"]
for letter in letters:
    print(letter)



# to get index
for letter in enumerate(letters):
    print(letter)


# to unpack tuple 
for index, letter in enumerate(letters):
    print(index, letter)

