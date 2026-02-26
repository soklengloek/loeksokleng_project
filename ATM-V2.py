balance = 1000
def check_balance():
    print("Your Balance :", balance)
def deposit():
    global balance
    amount = float(input("Enter deposit amount : "))
    balance += amount
    print("Deposit successful")
def withdraw():
    global balance
    amount = float(input("Enter withdraw amount : "))
    if amount <= balance:
        balance -= amount
        print("Withdraw successful")
    else:
        print("Insufficient balance")
def atm_menu():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Choose option : "))
        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")
atm_menu()
