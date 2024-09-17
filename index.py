import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def decorated_message(message):
    print("*********************")
    print(message)
    print("*********************\n")
    
def load_balances():
    if os.path.exists("balances.txt"):
        with open("balances.txt", "r") as f:
            balances = f.readlines()
            balance_1 = float(balances[0].strip())
            balance_2 = float(balances[1].strip())
        return balance_1, balance_2
    else:
        return 0.0, 0.0  #default balance of 0 for both accounts

def save_balances(balance_1, balance_2):
    with open("balances.txt", "w") as f:
        f.write(f"{balance_1}\n")
        f.write(f"{balance_2}\n")

def show_balance(balance):
    decorated_message(f"Your balance is ${balance:.2f}")

def deposit():
    decorated_message("Enter an amount to be deposited: ")
    amount = float(input())
    clear_screen()
    if amount < 0:
        decorated_message("That's not a valid amount")
        return 0
    else:
        decorated_message(f"${amount} successfully deposited")
        return amount

def withdraw(balance):
    decorated_message("Enter amount to be withdrawn: ")
    amount = float(input())
    clear_screen()
    if amount > balance:
        decorated_message("Insufficient funds")
        return 0
    elif amount < 0:
        decorated_message("Amount must be greater than 0")
        return 0
    else:
        decorated_message(f"${amount} successfully withdrawn")
        return amount
    
def transfer(balance):
    decorated_message("Enter the amount to be transferred: ")
    amount = float(input())

    if amount > balance:
        decorated_message("Insufficient funds")
        return 0
    elif amount < 1:
        decorated_message("Amount must be greater than 0")
        return 0
    elif amount > 10000:
        decorated_message("Transfer limit exceeded. Please try again.")
        return 0
    else:
        decorated_message("Amount successfully transferred")
        return amount
    
def sign_in():
    print("*****************************")
    print(" Welcome to the Banking App! ")
    print("     Please Sign In ")
    print("*****************************")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("*********************")

    clear_screen()

    if username == "justin" and password == "software":
        print("Sign-in successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
    
def lock_account(b1, b2):
    save_balances(b1, b2)
    decorated_message("Account locked")
    exit()

def account_options():
    decorated_message("Which account would you like to use?\n"+"1. Account 1\n"+"2. Account 2\n"+"3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        return 1
    elif choice == '2':
        return 2
    elif choice == '3':
        print("Have a nice day!")
        exit()
    else:
        print("Invalid choice. Exiting program.")
        exit()

def main():
    if not sign_in():
        print("Access denied. Exiting program.")
        exit()

    account = account_options()

    balance_1, balance_2 = load_balances()
    is_running = True

    clear_screen()

    while is_running:
        balance = balance_1 if account == 1 else balance_2

        print("*********************")
        print(f" Banking App - Account {account} ")
        decorated_message("1. Show Balance\n"+"2. Deposit\n"+"3. Withdraw\n"+"4. Transfer\n"+"5. Lock Account\n"+"6. Exit")
        choice = input("Enter your choice (1-6): ")

        clear_screen()

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            if account == 1:
                balance_1 += deposit()
            else:
                balance_2 += deposit()
        elif choice == '3':
            if account == 1:
                balance_1 -= withdraw(balance_1)
            else:
                balance_2 -= withdraw(balance_2)
        elif choice == '4':
            if account == 1:
                balance_1 -= transfer(balance_1)
            else:
                balance_2 -= transfer(balance_2)
        elif choice == '5':
            lock_account(balance_1, balance_2)
        elif choice == '6':
            save_balances(balance_1, balance_2)
            is_running = False
        else:
            decorated_message("That is not a valid choice")

    decorated_message("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()
