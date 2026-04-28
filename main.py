balance = 1000
history = []

def check_balance():
    print("Your balance is:", balance)

def deposit():
    global balance
    amt = int(input("Enter amount to deposit: "))
    balance += amt
    history.append(f"Deposited {amt}")
    print("Money deposited successfully")

def withdraw():
    global balance
    amt = int(input("Enter amount to withdraw: "))
    
    if amt > balance:
        print("Insufficient balance")
    else:
        balance -= amt
        history.append(f"Withdrawn {amt}")
        print("Please collect your cash")

def show_statement():
    print("\nTransaction History:")
    if len(history) == 0:
        print("No transactions yet")
    else:
        for item in history:
            print(item)

# MAIN PROGRAM
while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        show_statement()

    elif choice == "5":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")