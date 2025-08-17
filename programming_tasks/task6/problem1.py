# ALGORITHM
# 1)Start
# 2)Ask the user to input a password and store it in a
# variable called password
# 3)Define a function called is_strong_password for pwd
# 4)Set digit, upper and special as False by default
# 5)Start with a for loop that goes through each letter
# in pwd
# 6)To check whether password contains any digits set an if
# condition to check if there is any letter in "1234567890"
# 7)If condition is true then return digit is true
# 8)To check whether password contains any uppercase letter
# set an if condition letter.isupper() then return upper is True
# 9)To check whether password contains any special character set a
# condition to check if any letter is in "!@#"
# 10)last condition is to check length of password is
# greater than 8
# 11)If all of the four conditions are satisfied print 
# that password is strong or else weak
# 12)call the function and pass the input string through it
# and store it in a variable called password_valid
# 13)Print password_valid
# 14)End
password = input("Enter a password: ")

def is_valid_password(password):
    digit = False
    upper = False
    special = False
    for letter in password:
        if letter in ("1234567890"):
            digit = True
        if letter.isupper():
            upper = True
        if letter in ("!@#$%&*"):
            special = True

    if len(password) >= 8 and digit and upper and special:
        return "strong"
    else:
        return "weak"
    

password_valid = is_valid_password(password)
print(password_valid)