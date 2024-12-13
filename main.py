import random

def ussd_banking():
    print("Welcome to Simple Banking System")
    print("Dial *123# to access the banking menu")

    while True:
        code = input("Enter USSD code: ")
        if code == "*123#":
            print("\nBanking Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            balance = 1000  # Initial balance

            while True:
                try:
                    choice = int(input("\nEnter your choice: "))

                    if choice == 1:
                        print(f"Your balance is ${balance}.")
                    elif choice == 2:
                        deposit = float(input("Enter amount to deposit: "))
                        if deposit > 0:
                            balance += deposit
                            print(f"${deposit} deposited successfully. New balance: ${balance}.")
                        else:
                            print("Invalid amount. Please enter a positive value.")
                    elif choice == 3:
                        withdraw = float(input("Enter amount to withdraw: "))
                        if 0 < withdraw <= balance:
                            balance -= withdraw
                            print(f"${withdraw} withdrawn successfully. New balance: ${balance}.")
                        else:
                            print("Invalid amount. Ensure it's positive and within your balance.")
                    elif choice == 4:
                        print("Exiting... Thank you for using our service.")
                        return
                    else:
                        print("Invalid choice. Please select from the menu.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print("Invalid USSD code. Try again please.")

if __name__ == "__main__":
    ussd_banking()
