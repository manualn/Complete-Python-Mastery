# ALGORITHM
# 1)Start
# 2)Ask the user to input a password and store it in a
# variable called pwd
# 3)Define a function called is_valid_password for pwd
# 4)Set digit and upper as False by default
# 5)Start witha for loop that goes through each letter
# in pwd
# 6)To check whether password contains any digits set an if
# condition to check if there is any letter in "1234567890"
# 7)If condition is true then return digit is true
# 8)To check whether password contains any uppercase letter
# set an if condition letter.isupper() then return upper is True
# 9)Third condition is to check length of password is
# greater than 6
# 10)If all of the three conditions are satisfied return
# True or else False
# 11)call the function and pass the input string through it
# and store it in a variable called valid_pwd
# 12)Print valid_pwd
# 13)End

pwd = input("Enter a password: ")

def is_valid_password(pwd):
    digit = False
    upper = False
    for letter in pwd:
        if letter in "1234567890":
            digit = True
        if letter.isupper():
            upper = True

    if len(pwd) >= 6 and digit and upper:
        return True
    else:
        return False
    

valid_pwd = is_valid_password(pwd)
print(valid_pwd)