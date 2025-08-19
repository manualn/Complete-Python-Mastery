# 1) Start
# 2) input a number and convert it into integer and store it in a variable called n
# 3) define a function prime_status for n
# 4) Inside the function Create an empty list called primes
# 5) create a for loop for num in range between 2 and n then return True and store it in variable called
#    is_prime
# 6) Create a for loop in range 2 and num to try dividing num by all numbers before it
# 7) Then set an if condition inside the loop if divisible, it's not a prime
# 8) If its not a prime then return false then stop checking the number
# 9) If num is still marked as prime then add num to the primes list
# 10)Set a dictionary named result containing prime and twin_prime
# 11)If n is there in primes list then result["prime"] is True
# 12)If n-2 and n+2 is there in primes list then result["twin_prime"] is true
# 13)Return result
# 14)Call the function and pass the input number through it and store it in variable called final_result
# 15)Print the final_result

n = int(input("enter a number: "))

def is_prime(num):
    if num < 2:
        return False

    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

def prime_status(n):
    result = {"prime": False, "twin_prime": False}

    if is_prime(n):
        result["prime"] = True

        if is_prime(n - 2) or is_prime(n + 2):
            result["twin_prime"] = True

    return result

final_result = prime_status(n)
print(final_result)