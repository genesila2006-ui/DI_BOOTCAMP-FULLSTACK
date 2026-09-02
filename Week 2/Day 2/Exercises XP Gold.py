# Parts I & III: BankAccount Class
class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to perform a deposit.")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Deposit amount must be a positive integer.")
        self.balance += amount
        print(f"Successfully deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to perform a withdrawal.")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive integer.")
        self.balance -= amount
        print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")


# Part II: MinimumBalanceAccount Class
class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to perform a withdrawal.")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive integer.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw ${amount}. Balance cannot fall below minimum limit of ${self.minimum_balance}.")
        
        self.balance -= amount
        print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")


# Part IV: BONUS ATM Class
class ATM:
    def __init__(self, account_list, try_limit):
        # Validate account_list
        if not isinstance(account_list, list) or not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("account_list must contain BankAccount or MinimumBalanceAccount instances.")
        
        self.account_list = account_list

        # Validate try_limit
        try:
            if not isinstance(try_limit, (int, float)) or try_limit <= 0:
                raise Exception("try_limit must be a positive number.")
            self.try_limit = int(try_limit)
        except Exception as e:
            print(f"Validation Error: {e}. Defaulting try_limit to 2.")
            self.try_limit = 2

        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n=== ATM MAIN MENU ===")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option (1-2): ").strip()

            if choice == "1":
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def log_in(self, username, password):
        authenticated_account = None
        for account in self.account_list:
            if account.authenticate(username, password):
                authenticated_account = account
                break

        if authenticated_account:
            print(f"\nLogin successful! Welcome, {authenticated_account.username}.")
            self.current_tries = 0  # Reset tries on successful login
            self.show_account_menu(authenticated_account)
        else:
            self.current_tries += 1
            print(f"Invalid credentials. Attempt {self.current_tries} of {self.try_limit}.")
            if self.current_tries >= self.try_limit:
                print("Maximum login tries reached. Shutting down system.")
                exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n=== ACCOUNT MENU ({account.username}) ===")
            print(f"Current Balance: ${account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit/Log out")
            choice = input("Select an option (1-3): ").strip()

            if choice == "1":
                try:
                    amt = int(input("Enter deposit amount: "))
                    account.deposit(amt)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amt = int(input("Enter withdrawal amount: "))
                    account.withdraw(amt)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                account.authenticated = False  # Log out user
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice. Try again.")


# --- Test Execution ---
if __name__ == "__main__":
    acc1 = BankAccount("alice", "pass123", balance=100)
    acc2 = MinimumBalanceAccount("bob", "secure456", balance=200, minimum_balance=50)

    # Initialize ATM with a list of accounts
    atm = ATM(account_list=[acc1, acc2], try_limit=3)