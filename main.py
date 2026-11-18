def show_balance(balance):
        print("***************************")
        print(f"Your balance is ${balance:.2f}")
        print("***************************")
def deposit(balance):
        print("***************************")
        amount = float(input("Enter how much do you want to deposit: "))
        print("***************************")
        if amount <= 0:
            print("***************************")
            print("You cannot deposit less than  0")
            print("***************************")
            return balance
        else:    
            balance += amount
            print("***************************")
            print(f"Your deposit is ${amount:.2f}")
            print("***************************")
            return balance
            
def withdraw(balance):
        print("***************************")
        amount = float(input("Enter how much do you want to withdraw: "))
        print("***************************")
        if amount > balance:
            print("***************************")
            print("You don't have enough money")
            print("***************************")
            return balance
        elif amount <= 0:
            print("***************************")
            print("Withdraw has to be grater than 0")
            print("***************************")
            return balance 
        else:
            balance -= amount
            print("***************************")
            print(f"Your withdrew ${amount:.2f}")
            print("***************************")
            return balance
    
if __name__ == "__main__":
    balance = 0
    is_running = True

    while is_running:
        print("***************")
        print("Banking Program")
        print("***************")
        print("1.Show Balance\n2.Deposit\n3.Withdraw\n4.Exit")
        print("***************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("**************************")
            print("That is not a valid choice")
            print("**************************")
    
    print("***************************")
    print("Thank you! Have a nice day!")
    print("***************************")