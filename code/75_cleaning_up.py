try:
    file = open("75_cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    file.close()

except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")


try:
    file = open("75_cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
finally:
    file.close()