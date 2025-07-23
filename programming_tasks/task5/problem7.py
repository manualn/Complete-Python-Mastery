#ALGORITHM
# 1) Start
# 2) input a number and convert it into integer and store
#    it in a variable called n
# 3) define a function find_primes for n
# 4) Inside the function Create an empty list called primes
# 5) create a for loop for num in range between 2 and
#    n then return True and store it in variable called
#    is_prime
# 6) Create a for loop in range 2 and num to try 
#    dividing num by all numbers before it
# 7) Then set an if condition inside the loop if divisible,
#    it's not a prime
# 8) If its not a prime then return false then stop checking
#    the number
# 9) If num is still marked as prime then add num to
#    the primes list
# 10)Then return primes
# 11)Call the function and pass the number n in it and store 
#    it in variable called prime_numbers
# 12)print prime_numbers
# 13)End

n = int(input("Enter a number: "))

def find_primes(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes

prime_numbers = find_primes(n)
print(prime_numbers)