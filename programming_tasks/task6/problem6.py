# ALGORITHM
# 1)Start
# 2)Ask the user to input initial balance and convert into float and store it in balance
# 3)Ask the user to input action either withdraw or deposit and store it in action
# 4)Ask the user to input amount and convert it into float and store it in amount
# 5)Define a function called atm_simulate
# 6)Set an if condition to check whether action is deposit then add the amount to balance
# 7)Print the new balance
# 8)Set an elif condition to check if action is withdrawal then in that set an if condition to
#  check if amount is less than or equal to balance then subtract the amount from balance and 
#  print the new balance or else print insufficient balance and transaction failed.
# 9)Else print invalid action
# 10)return balance
# 11)Call the function and pass the balance, action and amount through it and store it in bal
# 12)End

balance = float(input("Enter a initial balance: "))
action = input("Enter action (withdraw/deposit): ")
amount = float(input("Enter amount: "))

def atm_simulate(balance, action, amount):
    if action.lower() == "deposit":
        balance += amount
        print(f"Deposit successful. New balance: {balance}")
    elif action.lower() == "withdrawal":
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient balance. Transaction failed.")
    else:
        print("Invalid action")

    return balance

    
bal = atm_simulate(balance, action, amount)