class Bank():
    acc = 10000
    transaction_count = 0

    def deposit(self):
        dep = float(input("Enter deposit amount: "))

        if dep < 100:
            print("Minimum deposit amount is 100.")
        elif dep % 100 != 0:
            print("Deposit should be in multiples of 100.")
        elif dep > 20000:
            print("Maximum deposit amount is 20000.")
        else:
            self.acc += dep
            Bank.transaction_count += 1
            print(f" Total balance: {self.acc}")

    def withdraw(self):
        if Bank.transaction_count >= 3:
            print("You have already completed 3 transactions. Withdrawal is no longer allowed.")
            return

        amo = float(input("Enter withdrawal amount: "))

        if amo < 100:
            print("Minimum withdrawal amount is 100.")
        elif amo % 100 != 0:
            print("Withdrawal should be in multiples of 100.")
        elif amo > self.acc - 500:
            print(f"Insufficient balance. You must maintain a minimum balance of 500.")
        elif amo > 20000:
            print("Maximum withdrawal amount is 20000.")
        else:
            self.acc -= amo
            Bank.transaction_count += 1
            print(f" Current balance: {self.acc}")

    def bal_enquiry(self):
        print(f"Your balance is: {self.acc}")

    def viewOptions(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance enquiry")
            print("0. Exit")
            option = int(input("Enter the option: "))

            if option == 1:
                self.deposit()
            elif option == 2:
                self.withdraw()
            elif option == 3:
                self.bal_enquiry()
            elif option == 0:
                print("Exit.")
                break
            else:
                print("Invalid option. Please try again.")

    def validatepin(self):
        for i in range(3):
            pin = int(input("Enter your PIN: "))
            if pin == 1234:
                print("PIN validated successfully!")
                self.viewOptions()
                break
            else:
                if i < 2:
                    print("Incorrect PIN. Please try again.")
                else:
                    print("Too many incorrect attempts. Exiting.")
                    return

obj = Bank()
obj.validatepin()
