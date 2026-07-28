class InvalidPinError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class ATM:
    def __init__(self, realpin, balance):
        self.realpin = realpin
        self.balance = balance
        self.transactions = []
    
    def authenticate_user(self):
        tries = 3
        while tries > 0:
            try:
                pin = int(input("Enter your pin: "))
                if pin != self.realpin:
                    raise InvalidPinError("Your Pin is invalid. Please Try again!. ")

                print("Login Successful. ")
                return True
            
            except ValueError:
                print("Please enter a number only. ")

            except InvalidPinError as e:
                tries -= 1
                print(e)
                print(f"Attemps left: {tries}")

        print("Your account has been locked. ")
        return False

    def show_menu(self):
        print("\nWelcome to the ATM!. ")
        print("*" * 30)

        print("1. Check Balance \n2. Deposit \n3. Withdraw \n4. Transactions \n5. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid choice!. ")
            return None

        return choice

    def check_balance(self):
        print("Your Balance:", self.balance)

    def deposit(self):
        try: 
            amount = int(input("Please enter the amount you want to deposit: "))
            if amount <= 0:
                raise InvalidAmountError("Please enter a valid amount. ")

        except InvalidAmountError as e:
            print(e)
            return

        except ValueError:
            print("Amount should be a number. ")
            return

        self.balance += amount
        self.check_balance()

        self.transactions.append({"Transaction:"  : "Deposit", "Amount:" : amount})


    def withdraw(self):
        try: 
            withdraw = int(input("Please enter the amount you want to deposit: "))
            if withdraw <= 0:
                raise InvalidAmountError("Please enter a valid amount. ")
            if withdraw > self.balance:
                raise InsufficientBalanceError("You do not have enough balance. ")

        except InvalidAmountError as e:
            print(e)
            return
            

        except ValueError:
            print("Amount should be a number. ")
            return

        except InsufficientBalanceError as e:
            print(e)
            return

        self.balance -= withdraw
        self.check_balance()

        self.transactions.append({"Transaction:"  : "Withdraw", "Amount:" : withdraw})

    def exit_atm(self):
        print("Thank you for using our ATM!. ")

    def show_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)
        

    def run(self):
        if not self.authenticate_user():
            return 
        
        while True:
            choice = self.show_menu()

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                self.show_transactions()
            elif choice == 5:
                self.exit_atm()
                break
            else:
                print("\nPlease enter a valid choice. ")

atm = ATM(1234, 1000)
atm.run()
