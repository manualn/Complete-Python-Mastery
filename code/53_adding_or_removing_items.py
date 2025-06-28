letters = ["a", "b", "c"]

Add
letters.insert(0, "-")
letters.append("d")
print(letters)


#Remove
letters = ["a", "b", "c", "d"]
print(letters.pop(0))
print(letters.remove("b"))
del letters[0:3]
print(letters)